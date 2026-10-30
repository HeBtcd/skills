---
name: performance-engineering
disable-model-invocation: true
description: "Workload cost modeling, profiling, and optimization. Use when something is too slow or allocation-heavy, when a workload's cost must be modeled, or when a claimed speedup needs proof."
---

# Performance Engineering

Ground optimization in a cost model and measurements ([Brunnert et al., Performance-oriented DevOps: A Research Agenda](https://research.spec.org/fileadmin/user_upload/documents/wg_devops/endorsed_publications/SPEC-RG-2015-001-DevOpsPerformanceResearchAgenda.pdf), §3.2, surveying Balsamo et al. 2004 and Woodside et al. 2007).

Pin down the workload, input scale, hardware, budget (latency, throughput, memory), and invariants first. Measure before guessing; separate back-of-the-envelope estimates from measurements, and average cost from tail cost. Optimize mechanisms (memory layout, locality, allocations, thread coordination) and count full-system cost when work shifts across paths. Preserve ownership, lifetimes, and reentrancy when introducing zero-copy views or pools.

Benchmark baseline and candidate under identical conditions. Call a change a strict win only when it improves a target metric and regresses none; trade-offs on the [Pareto](https://en.wikipedia.org/wiki/Pareto_efficiency) frontier belong to the user, and behavior changes are reported separately. Treat competitor numbers as data points, not ceilings, and use automated benchmark loops over large tuning spaces ([David Heinemeier Hansson on the sub-one-minute install, Lex Fridman Podcast #501](https://lexfridman.com/dhh-2-transcript/)). When the workload data the model needs is missing or conflicting, name the gap and sync with the user instead of guessing.

## Heap allocations

Catalog explicit and hidden allocations across happy, startup, and error paths separately: boxing, closure captures, generator/iterator state machines, variadic arrays, formatting, and library calls (via static tools like the [Roslyn CLR Heap Allocation Analyzer](https://github.com/microsoft/RoslynClrHeapAllocationAnalyzer) or escape analysis). Verify the analysis pass completed cleanly under real compiler flags, chase unanalyzed calls into emitted code or profiler traces on hot paths, and report trigger, lifetime, owner, and runtime frequency separately from static call sites.
