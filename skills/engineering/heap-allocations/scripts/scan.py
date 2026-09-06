"""Locate explicit and implicit C# allocations with a pinned Roslyn analyzer; emit JSON."""
import argparse
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlparse
from urllib.request import urlopen, url2pathname
import xml.etree.ElementTree as ET
import zipfile

PACKAGE = "reflectionit.clrheapallocationanalyzer"
VERSION = "3.2.4"


def analyzer():
    cache = Path(tempfile.gettempdir()) / "codex-heap-allocations" / VERSION
    dll = cache / "ReflectionIT.ClrHeapAllocationAnalyzer.dll"
    if not dll.exists():
        url = f"https://api.nuget.org/v3-flatcontainer/{PACKAGE}/{VERSION}/{PACKAGE}.{VERSION}.nupkg"
        with urlopen(url, timeout=60) as response:
            package = response.read()
        with zipfile.ZipFile(io.BytesIO(package)) as archive:
            candidates = [p for p in archive.namelist() if p.startswith("analyzers/") and p.endswith(".dll")]
            if len(candidates) != 1:
                raise RuntimeError(f"Expected one analyzer DLL, got {candidates}")
            cache.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=cache, delete=False) as staging:
                staging.write(archive.read(candidates[0]))
            os.replace(staging.name, dll)
    return dll


def source_path(uri):
    return str(Path(url2pathname(urlparse(uri).path) if uri.startswith("file:") else unquote(uri)).resolve())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="One .csproj, or one or more .cs files")
    parser.add_argument("--project", type=Path, help="Compile this project, report only the input .cs files")
    parser.add_argument("--framework", help="Project target framework; standalone default: net8.0")
    parser.add_argument("--lang-version", help="Standalone C# version; default: compiler default")
    parser.add_argument("--reference", action="append", type=Path, default=[], help="Standalone assembly reference (repeatable)")
    args = parser.parse_args()
    inputs = [p.resolve(strict=True) for p in args.inputs]
    project = args.project.resolve(strict=True) if args.project else None
    if len(inputs) == 1 and inputs[0].suffix == ".csproj" and project is None:
        project, inputs = inputs[0], []
    if any(p.suffix != ".cs" for p in inputs):
        parser.error("Use one .csproj or .cs files; for a solution, run each relevant project")
    if project and (args.reference or args.lang_version):
        parser.error("Project mode uses the project's references and language version")
    dll = analyzer()
    with tempfile.TemporaryDirectory(prefix="heap-allocations-") as folder:
        temp = Path(folder)
        if project is None:
            root = ET.Element("Project", Sdk="Microsoft.NET.Sdk")
            props = ET.SubElement(root, "PropertyGroup")
            for key, value in {"TargetFramework": args.framework or "net8.0", "EnableDefaultCompileItems": "false", "Nullable": "enable"}.items():
                ET.SubElement(props, key).text = value
            if args.lang_version:
                ET.SubElement(props, "LangVersion").text = args.lang_version
            items = ET.SubElement(root, "ItemGroup")
            for path in inputs:
                ET.SubElement(items, "Compile", Include=str(path))
            for path in args.reference:
                path = path.resolve(strict=True)
                item = ET.SubElement(items, "Reference", Include=path.stem)
                ET.SubElement(item, "HintPath").text = str(path)
            project = temp / "Scan.csproj"
            ET.ElementTree(root).write(project, encoding="unicode")
        # Run immediately before Csc; keep the input project's normal imports intact.
        root = ET.Element("Project")
        target = ET.SubElement(root, "Target", Name="HeapAllocationScan", BeforeTargets="CoreCompile")
        items = ET.SubElement(target, "ItemGroup")
        ET.SubElement(items, "Analyzer", Include=str(dll))
        props = ET.SubElement(target, "PropertyGroup")
        ET.SubElement(props, "ErrorLog").text = str(temp / "$(MSBuildProjectName)-$(TargetFramework).sarif") + ",version=2.1"
        targets = temp / "Scan.targets"
        ET.ElementTree(root).write(targets, encoding="unicode")
        command = ["dotnet", "build", str(project), "--no-incremental", "--nologo", "-v:q",
                   f"-p:CustomAfterMicrosoftCommonTargets={targets}", "-p:RunAnalyzers=true",
                   "-p:RunAnalyzersDuringBuild=true", "-p:TreatWarningsAsErrors=false"]
        if args.framework:
            command += ["-p:TargetFramework=" + args.framework]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                env={**os.environ, "DOTNET_CLI_UI_LANGUAGE": "en-US"})
        findings, errors = [], []
        selected = {os.path.normcase(str(p)) for p in inputs}
        reports = list(temp.glob("*.sarif"))
        loaded = False
        for report in reports:
            for run in json.loads(report.read_text(encoding="utf-8-sig")).get("runs", []):
                loaded |= any(r.get("id", "").startswith("HAA") for r in run.get("tool", {}).get("driver", {}).get("rules", []))
                for entry in run.get("results", []):
                    rule = entry.get("ruleId", "")
                    if rule.startswith(("AD", "CS803")) or entry.get("level") == "error":
                        errors.append(entry)
                    if not rule.startswith("HAA"):
                        continue
                    location = (entry.get("locations") or [{}])[0].get("physicalLocation", {})
                    uri = location.get("artifactLocation", {}).get("uri", "")
                    path = source_path(uri) if uri else None
                    if selected and (path is None or os.path.normcase(path) not in selected):
                        continue
                    findings.append({"file": path, "line": location.get("region", {}).get("startLine"),
                                     "column": location.get("region", {}).get("startColumn"),
                                     "rule": rule, "message": entry["message"]["text"]})
        ok = result.returncode == 0 and loaded and not errors
        print(json.dumps({"complete": ok, "analyzer": f"{PACKAGE}@{VERSION}", "findings": findings}, ensure_ascii=False, indent=2))
        if not ok:
            print(result.stdout + result.stderr, file=sys.stderr)
            if not loaded:
                print("No allocation analyzer rules in compiler report; analysis is incomplete.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
