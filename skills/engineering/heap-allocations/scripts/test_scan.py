"""Check allocation findings and scan failures; requires the same SDK/network access as scan.py."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def scan(*args):
    result = subprocess.run([sys.executable, str(HERE / "scan.py"), *map(str, args)], capture_output=True, text=True)
    return result, json.loads(result.stdout)


with tempfile.TemporaryDirectory(prefix="allocation-check-") as folder:
    folder = Path(folder)
    result, report = scan(HERE / "Smoke.cs")
    assert result.returncode == 0 and report["complete"], result.stderr
    assert {"HAA0301", "HAA0601", "HAA0603"} <= {f["rule"] for f in report["findings"]}
    assert all(f["line"] in (5, 7) for f in report["findings"]), report
    source = folder / "A.cs"
    source.write_text("public class A { public object Box(int n) => n; public object Create() => new object(); public int[] Array() => new int[1]; }", encoding="utf-8")
    other = folder / "B.cs"
    other.write_text("public class B { public object Box(int n) => n; }", encoding="utf-8")
    project = folder / "Example.csproj"
    content = '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net8.0</TargetFramework></PropertyGroup></Project>'
    project.write_text(content, encoding="utf-8")
    result, report = scan(project)
    assert result.returncode == 0 and report["complete"], result.stderr
    assert {Path(f["file"]).name for f in report["findings"]} == {"A.cs", "B.cs"}, report
    assert {"HAA0501", "HAA0502", "HAA0601"} <= {f["rule"] for f in report["findings"]}, report
    result, report = scan(source, "--project", project)
    assert result.returncode == 0 and report["complete"], result.stderr
    assert report["findings"] and all(Path(f["file"]) == source for f in report["findings"]), report
    assert project.read_text(encoding="utf-8") == content
    source.write_text("public class A { MissingType x; }", encoding="utf-8")
    result, report = scan(source)
    assert result.returncode == 2 and not report["complete"], (result, report)
print("PASS: closure, delegate, boxing, explicit object/array, noncapturing control, project, file filter, failed compilation")
