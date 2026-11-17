<img src="assets/poster.svg" alt="HeBtcd Skills">

# HeBtcd Skills

Reusable engineering and communication skills for AI coding agents (Claude Code, Codex, Cursor, OpenCode). Each skill triggers at a specific moment of work so the agent stops guessing and follows a tested method.

## Install

**Claude Code plugin**

```sh
claude plugin marketplace add HeBtcd/skills && claude plugin install skills@hebtcd
```

**Any agent harness**

```sh
npx skills add HeBtcd/skills
```

## Skills

| Skill | Use when |
|---|---|
| [play-it-back](skills/moments/play-it-back/SKILL.md) | A prompt is vague, corrective, or names a solution instead of the problem. |
| [what-are-we-assuming](skills/moments/what-are-we-assuming/SKILL.md) | A plan or judgment rests on unstated premises. |
| [is-this-a-thing](skills/moments/is-this-a-thing/SKILL.md) | An idea might already have a name, or a quote needs attribution checked. |
| [deep-research](skills/moments/deep-research/SKILL.md) | A decision depends on primary-source production evidence, not summaries. |
| [when-in-rome](skills/moments/when-in-rome/SKILL.md) | Writing code in an existing repo that already has its own conventions. |
| [functional-programming](https://github.com/HeBtcd/lambda-ray/tree/main/skills/functional-programming/SKILL.md) | Modeling domains in types and pushing side effects to the edges (moved to lambda-ray). |
| [name-the-witness](skills/personal/name-the-witness/SKILL.md) | Attaching checkable proof to state claims and keeping unverified claims at the boundary. |
| [let-it-crash](skills/moments/let-it-crash/SKILL.md) | Auditing failure paths for detection, recovery, and restart limits. |
| [open-from-day-one](skills/moments/open-from-day-one/SKILL.md) | Making a repo buildable, testable, and handoff-ready for a stranger. |
| [performance-engineering](skills/moments/performance-engineering/SKILL.md) | Estimating, profiling, or proving a performance cost or speedup. |
| [slim](skills/moments/slim/SKILL.md) | Shrinking a bloated doc, feature, or bug repro to its minimum core. |
| [show-your-math](skills/moments/show-your-math/SKILL.md) | Defending or recording where a number, default, or estimate came from. |
| [write-the-docs](skills/moments/write-the-docs/SKILL.md) | Drafting or syncing a README, design doc, ADR, or changelog. |
| [for-the-audience](skills/moments/for-the-audience/SKILL.md) | Turning messy threads into a standalone doc for outside readers. |
| [plain-language](skills/moments/plain-language/SKILL.md) | Cutting jargon and bloat from specs, instructions, or UI copy. |
| [managing-up](skills/moments/managing-up/SKILL.md) | Reporting finished work or escalating a decision to someone without context. |
| [review-the-pr](skills/moments/review-the-pr/SKILL.md) | Reviewing a huge diff or sweeping a codebase for a defect class. |
| [straight-answer](skills/moments/straight-answer/SKILL.md) | Stripping defensiveness and padding from a reply before sending. |
| [prove-it-wrong](skills/moments/prove-it-wrong/SKILL.md) | Trying to falsify your own diagnosis or plan before trusting it. |
| [hebtcd-skill-creator](skills/personal/hebtcd-skill-creator/SKILL.md) | Creating or restructuring a skill in this repo. |
| [walk-states](skills/personal/walk-states/SKILL.md) | Proving a change works using concrete before/after states instead of action logs. |

## License

[MIT](LICENSE)
