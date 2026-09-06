---
name: heap-allocations
disable-model-invocation: true
description: Locate C# heap allocations with evidence, coverage limits, and proposed collection.
---

For each suspected allocation, give location, cause, triggering path, and evidence. Distinguish static findings from measured frequency or bytes; allocation alone does not justify removal.

When further evidence would change a finding, propose `scripts/scan.py` here (`--help`; absolute input paths). It requires Python 3.10+ and a .NET SDK, downloads/caches [ReflectionIT.ClrHeapAllocationAnalyzer 3.2.4](https://www.nuget.org/packages/ReflectionIT.ClrHeapAllocationAnalyzer/3.2.4), and in project mode executes build targets and updates normal build outputs. Prefer the project's references and language settings.

The scanner replaces `CustomAfterMicrosoftCommonTargets` without chaining it. Check build configuration; if that import is required, use source or existing analyzer output. `complete: false` means failure.

Cross-check source, callees, and available target-compiler IL or measurements. Empty output does not prove zero allocations. Return supported findings, coverage limits, unresolved suspicions, and proposed collection separately from evidence.
