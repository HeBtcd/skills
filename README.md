<img src="asset/poster.svg">

# Skills

## Install

```sh
claude plugin marketplace add HeBtcd/skills && claude plugin install skills@hebtcd
```

```sh
cp -r skills/is-this-a-thing ~/.claude/skills/ # or copy a folder: Claude Code
cp -r skills/is-this-a-thing ~/.agents/skills/ # agents-compatible harnesses
```

## The moments

| Skill | Description |
|---|---|
| [read-between-the-lines](skills/read-between-the-lines/SKILL.md) | Read between the lines: infer the unspoken goal from context and check the workspace before asking the user. Use when a message is short, vague, or corrective. |
| [give-me-options](skills/give-me-options/SKILL.md) | Ask the smallest, easiest-to-answer question that unblocks a decision by giving concrete options to compare. Use when intent or preference remains unresolved after checking context and a question is owed. |
| [play-it-back](skills/play-it-back/SKILL.md) | Reflective listening: restate the user's goal and the problem behind it, so they can confirm or correct it. Use when about to act on an ambiguous request, or the literal ask may not be the real goal. |
| [what-are-we-assuming](skills/what-are-we-assuming/SKILL.md) | Examine the assumptions a judgment or plan depends on. Use when premises go unstated, when a judgment is challenged, or when the request itself may be a solution rather than the problem (XY problem). |
| [be-more-ambitious](skills/be-more-ambitious/SKILL.md) | Raise the ambition of a task spec before doing it. Use when a task reads like a deliverables list, or the user asks for a deeper or more ambitious version of a prompt. |
| [is-this-a-thing](skills/is-this-a-thing/SKILL.md) | Find the established name and original source of a concept, rule, or practice. Use when an idea may already exist under a standard name, including before writing a new Skill or building an unfamiliar capability from scratch. |
| [deep-research](skills/deep-research/SKILL.md) | Find decision-relevant evidence such as field reports, real-world failure cases, and tested alternatives where generic summaries fall short. Use when a research question is substantive, or standard recommendations fail to settle an important decision. |
| [when-in-rome](skills/when-in-rome/SKILL.md) | Match the nearest existing implementations and the house style before writing new code in a codebase that already has conventions. Use when adding a feature, function, test, or file to an established repository. |
| [functional-programming](skills/functional-programming/SKILL.md) | Functional programming design: model domains with algebraic data types so invalid states cannot be constructed, build pipelines from small pure functions over immutable values, keep side effects in a thin outer shell, and refactor by equational reasoning. Use when modeling a domain, untangling state and branching, or refactoring logic toward provable correctness. |
| [let-it-crash](skills/let-it-crash/SKILL.md) | Design or review failure-path contracts and ownership. Use when deciding who owns a check, auditing error handling, or checking whether a breach could pass unnoticed. |
| [open-from-day-one](skills/open-from-day-one/SKILL.md) | Keep a repo or artifact ready to go public or change hands at any moment: a stranger on a clean machine can build, run, change, release, and take it over without asking you. Use when shaping a project, checking repo hygiene, or preparing work for outsiders or future maintainers. |
| [performance-engineering](skills/performance-engineering/SKILL.md) | Workload cost modeling, profiling, and optimization. Use when something is too slow or allocation-heavy, when a workload's cost must be modeled, or when a claimed speedup needs proof. |
| [slim](skills/slim/SKILL.md) | Simplify an artifact from the design down: a smaller decomposition, a smaller replacement, or a measured share of removable parts. Use when something is bloated: slim it, cut it down, simplify it, or minimize a failing repro. |
| [show-your-math](skills/show-your-math/SKILL.md) | Derive quantities and defaults from constraints, separating derivation from calibration and preference. Use when a number or default needs defending, or the user asks to see the working (show your work). |
| [write-the-docs](skills/write-the-docs/SKILL.md) | Write or edit project documentation. Use when writing a README, design doc, module doc, or task record. |
| [for-the-audience](skills/for-the-audience/SKILL.md) | Turn messy working materials into a self-contained document written for the audience that was not in the room. Use when threads, notes, or review back-and-forth must become a document. |
| [plain-language](skills/plain-language/SKILL.md) | Shorten and clarify text in plain language while preserving its exact meaning. Use when text is too long, jargon-dense, or overwrought for its reader, such as specs, instructions, docs, or UI copy. |
| [managing-up](skills/managing-up/SKILL.md) | Report finished work or escalate a decision to a delegator who did not follow the work. Use when an agent reports back, requests a decision, or answers a review. |
| [review-the-pr](skills/review-the-pr/SKILL.md) | Code review for agent-written pull requests: machines verify what they can, context checks cover what the diff cannot carry, and a person signs the risk. Use when asked to review, approve, or sign off on a PR produced faster than anyone can read, or when the reviewer is also an agent. |
| [straight-answer](skills/straight-answer/SKILL.md) | Audit a reply before accepting or sending it. Use when an agent argues against the user's position, answers criticism, drafts an objection or caveat, or a reply reads defensive, padded or mis-calibrated. |
| [prove-it-wrong](skills/prove-it-wrong/SKILL.md) | Stop proving yourself right: try to break the claim until it fails or earns trust. Use when an agent has convinced itself by piling up supporting reasons, before accepting a self-built conclusion or a fix that merely 'should work'. |
| [hebtcd-skill-creator](skills/hebtcd-skill-creator/SKILL.md) | Write or refactor a Skill. Use when creating, splitting, renaming or pruning one. |

## License

[MIT](LICENSE)
