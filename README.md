<img src="asset/logo.svg">

# Skills

My skills for working with coding agents. Pick the ones you need.

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills).

## Installation

<summary><strong>Paste this into your agent</strong></summary>

```text
Use the skills CLI to install from https://github.com/HeBtcd/skills.git; ask which skills, agent, and scope, preserve local edits, and report the install paths.
```

## Skills

### Engineering

- [ablate-it](skills/engineering/ablate-it/SKILL.md): Compare designs and controlled removals to simplify without changing authorized behavior.
- [functional-programming](skills/engineering/functional-programming/SKILL.md): Design with value semantics, composable functions, explicit effects, and types encoding legal states and operations.
- [heap-allocations](skills/engineering/heap-allocations/SKILL.md): Locate C# heap allocations with evidence, coverage limits, and proposed collection.
- [performance-engineering](skills/engineering/performance-engineering/SKILL.md): Analyze workload resource costs and propose behavior-preserving optimizations.
- [primitives](skills/engineering/primitives/SKILL.md): Find basic operations that combine to build the required capability.

### Productivity

- [are-we-done](skills/productivity/are-we-done/SKILL.md): Check requirement coverage and evidence against completion criteria.
- [ask-last](skills/productivity/ask-last/SKILL.md): Resolve dependencies, prune infeasible paths, and expose conflicts before asking consequential questions.
- [check-premises](skills/productivity/check-premises/SKILL.md): Check consequential premises with unclear support before relying on them.
- [clean-copy](skills/productivity/clean-copy/SKILL.md): Extract reader-facing content from material mixed with production instructions and notes.
- [clean-history](skills/productivity/clean-history/SKILL.md): Prepare or organize a task’s Git changes into coherent commits.
- [counterexample](skills/productivity/counterexample/SKILL.md): Seek the smallest admissible counterexample before costly proof or checking.
- [critically](skills/productivity/critically/SKILL.md): Use a subagent to challenge claims or solutions when requested.
- [data-flow](skills/productivity/data-flow/SKILL.md): Trace implementation reads, transformations, writes, and outputs in compact tables.
- [delegate](skills/productivity/delegate/SKILL.md): Delegate bounded work with explicit roles, ownership, isolation, and return routes.
- [divergent-thinking](skills/productivity/divergent-thinking/SKILL.md): Generate distinct possibilities before evaluation when existing framing constrains exploration.
- [go-with-the-grain](skills/productivity/go-with-the-grain/SKILL.md): Match new structure to an established example.
- [hands-off](skills/productivity/hands-off/SKILL.md): Assign design and implementation to a stronger specialist; verification to a weaker manager.
- [hands-on](skills/productivity/hands-on/SKILL.md): Keep design and verification with a stronger manager; bound a weaker model’s implementation.
- [is-that-right](skills/productivity/is-that-right/SKILL.md): Recheck challenged judgments against context, evidence, alternatives, and a minimal distinguishing check.
- [is-this-a-thing](skills/productivity/is-this-a-thing/SKILL.md): Find the narrowest established concept matching a locally described mechanism.
- [metacognitively](skills/productivity/metacognitively/SKILL.md): Request an independent critic of how the agent forms, retains, or revises judgments.
- [minimal-model](skills/productivity/minimal-model/SKILL.md): Find the smallest complete model meeting the task’s requirements.
- [now-what](skills/productivity/now-what/SKILL.md): Choose the next action under incomplete evidence and costly delay.
- [prove-infeasible](skills/productivity/prove-infeasible/SKILL.md): Before commitment, check consequential doubts about a path’s compatibility with established constraints.
- [says-who](skills/productivity/says-who/SKILL.md): Find authority or derivation for behavior-changing choices, including defaults and omissions.
- [study-comparatively](skills/productivity/study-comparatively/SKILL.md): Compare mechanisms under shared questions and comparable conditions, explaining consequential similarities and differences.
- [take-stock](skills/productivity/take-stock/SKILL.md): Assess progress from sourced decisions, results, open questions, and dependencies.
- [to-table](skills/productivity/to-table/SKILL.md): Render data as compact key-value tables, splitting complex structures.
- [what-i-said](skills/productivity/what-i-said/SKILL.md): Establish or update user-confirmed requirements for design, delegation, or implementation.
- [what-name](skills/productivity/what-name/SKILL.md): Name a skill, module, type, or concept.
- [who-owns-this](skills/productivity/who-owns-this/SKILL.md): Identify who can define and maintain behavior-changing rules, facts, representations, and lifecycle decisions.
- [with-docs](skills/productivity/with-docs/SKILL.md): Turn supplied material or work results into reader-ready documentation.

### Personal

- [comment-code](skills/self/comment-code/SKILL.md): Write or audit consequential contract, invariant, and rationale comments.
- [format-csharp](skills/self/format-csharp/SKILL.md): Format C# with compact guards, expressions and types, braced work, grouped members, and verbatim backslash strings.
- [just-throw](skills/self/just-throw/SKILL.md): Replace redundant error prose with typed failures and diagnostics in guards, exceptions, validation, or logs.

### Work in progress

- [retro](skills/wip/retro/SKILL.md): Explain a task failure and propose an evidence-backed skill correction.
- [reverse-engineering](skills/wip/reverse-engineering/SKILL.md): Explain opaque binary/runtime behavior with evidence limits and proposed distinguishing observations.
- [runtime-probes](skills/wip/runtime-probes/SKILL.md): Specify debugger probes, capture conditions, and recovery; assess collected results.
