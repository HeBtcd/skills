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
| [play-it-back](skills/play-it-back/SKILL.md) | Play back the real goal before acting on the literal ask. Use when a user's message is short or vague, when the user corrects your last attempt, or when a request names a solution instead of the problem it solves. |
| [what-are-we-assuming](skills/what-are-we-assuming/SKILL.md) | Surface the unstated premises under a request, judgment, or plan, and answer a challenged judgment at its strongest. Use when a request may name a solution instead of the real problem, when a conclusion or plan may rest on premises no one stated, or when a judgment is being challenged. |
| [is-this-a-thing](skills/is-this-a-thing/SKILL.md) | Trace an idea to the name it already has, or a quotation, rule, or method to the person who actually coined it. Use when an idea may already exist under an established name, or when an attribution needs checking before you repeat it. |
| [deep-research](skills/deep-research/SKILL.md) | Deep research that settles a decision with production evidence: frame an answerable question, hunt the primary record, weigh competing explanations, report calibrated findings. Use when an important decision rides on what actually happens in production and standard recommendations or generic summaries will not settle it. |
| [when-in-rome](skills/when-in-rome/SKILL.md) | Match an established codebase's own conventions when adding code to it. Use when about to write or change code in a project that already has its way of doing things: read the code around the change, let local precedent outrank general style rules, trace odd conventions to their reasons, run the project's own tools, and package each logical change on its own. |
| [functional-programming](skills/functional-programming/SKILL.md) | Functional design: model the domain in types, keep state essential, parse at the boundary, push side effects to the edges, refactor by substitution, write laws as properties, and convict idioms that hurt by design. Use when modeling a domain, untangling state and branching, deciding where side effects live, refactoring toward correctness, or judging whether an FP idiom earns its ceremony. |
| [let-it-crash](skills/let-it-crash/SKILL.md) | Audit failure paths under the let-it-crash doctrine: who detects a failure, who recovers it, who must be correct, and when restarts give up. Use when deciding who validates what on failure paths, auditing error handling, or checking whether a failure could pass unnoticed. |
| [open-from-day-one](skills/open-from-day-one/SKILL.md) | Shape a project so a stranger on a clean machine can build, run, change, release, and take it over without asking you: README, one-step build, self-testing code, CONTRIBUTING, changelog, semver, license, bus factor. Use when starting a repo, open-sourcing one, or auditing what your departure would strand. |
| [performance-engineering](skills/performance-engineering/SKILL.md) | Estimate, profile, and verify performance cost. Use when something is too slow or allocation-heavy, when cost must be estimated before building, or when a claimed speedup needs evidence. |
| [slim](skills/slim/SKILL.md) | Reduce a bloated artifact or a failing repro to its essential minimum. Use when code, a feature set, or a document is over-built and the question is what can go, or when a bug reproduction needs shrinking to the smallest case that still fails. |
| [show-your-math](skills/show-your-math/SKILL.md) | Defend a number, default, or estimate by showing where it came from: trace the reason it was set, rebuild the derivation, weigh it against similar finished cases, state the precision it earns, and record the source where it lives. Use when a figure is challenged on review, or when writing down a value that will have to stand later. |
| [write-the-docs](skills/write-the-docs/SKILL.md) | Write or re-cut a project document in its established form: README, design doc, decision record (ADR), or changelog. Use when a project needs a document drafted, or an existing one brought back in step with the thing it describes. |
| [for-the-audience](skills/for-the-audience/SKILL.md) | Write up scattered discussion as a self-contained document for readers who were not in the room. Use when turning threads, notes, and review back-and-forth into a decision record, postmortem, proposal, or summary that must stand alone for outside or future readers. |
| [plain-language](skills/plain-language/SKILL.md) | Rewrite a spec, instruction, doc, or UI copy into plain language, preserving exact meaning. Use when the text is too long, jargon-dense, or overwrought for its reader. |
| [managing-up](skills/managing-up/SKILL.md) | Report finished work or escalate a decision to a delegator who did not follow it. Use for status reports, delivered work, approval requests, and decision asks addressed to a boss, client, or stakeholder who lacks the context to judge them. |
| [review-the-pr](skills/review-the-pr/SKILL.md) | Review or sign off on a pull request produced faster than anyone can read it. Use when asked to approve a diff too big to read line by line, or to sweep a codebase for every instance of a defect class. |
| [straight-answer](skills/straight-answer/SKILL.md) | Audit a draft reply before it is sent. Use when the draft argues against the user's position, answers criticism, or reads defensive, padded, or mis-calibrated. |
| [prove-it-wrong](skills/prove-it-wrong/SKILL.md) | Falsify a self-built diagnosis or plan whose confirmations keep piling up: find what would make it break, then make the attempt. Use when supporting reasons abound, it should work, and every check seems to confirm. |
| [hebtcd-skill-creator](skills/hebtcd-skill-creator/SKILL.md) | Compose a Skill as an ordered basis of Things behind a trigger pointer. Use when deciding whether a capability, a recurring move, or a named concept deserves a Skill of its own, or when an existing Skill's basis needs re-cutting. |

## License

[MIT](LICENSE)
