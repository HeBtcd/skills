---
name: hebtcd-skill-creator
disable-model-invocation: true
description: "Write or refactor a Skill. Use when creating, splitting, renaming or pruning one."
---

# Hebtcd Skill Creator

## Earn the Skill

Start from an observed model failure on a real task ([Anthropic, Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills); [Anthropic, Lessons from building Claude Code: How we use skills](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/)):

> Identify specific gaps in your agents' capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

> A skill that restates what Claude would do by default adds context without adding value.

> we noticed they cluster into nine categories. The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent.

> Most of our best skills began as a few lines and a single gotcha, then got better because people kept adding to them as Claude hit new edge cases.

Apply Ockham's razor, *entia praeter necessitatem non esse multiplicanda* ([SEP, Simplicity](https://plato.stanford.edu/entries/simplicity/)): one Skill per trigger moment; fold into an existing Skill when the moment is already owned, and before deleting an obsolete Skill, reconstruct the failure it was written for and confirm the successor covers it. Aim at the layer the failure lives in; polishing a mechanical loop fixes nothing when the missing piece is judgment.

A **Thing** is a method or concept with an established name and checkable source: keep its established name in `SKILL.md` for `grep`, never invent house jargon, and mark any unlinked well-known term `unsourced`.

## Frontmatter, invocation, and routing

A Skill is a `kebab-case` folder holding one `SKILL.md` file with one `# Title` heading.

Every `SKILL.md` starts with `name` (matching the folder), `disable-model-invocation`, and `description` (what it does, when it fires, and user trigger phrases, tight since it loads on every turn) ([Anthropic, Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)):

> the description field is not a summary, it's a description of when to trigger this skill.

> Pay special attention to the name and description of your skill. Claude will use these when deciding whether to trigger the skill in response to its current task.

Set `disable-model-invocation: false` only when all three hold: (1) silent failure mode, (2) narrow trigger moment, and (3) zero extra conversation turns. Every other Skill sets `true`.

## Naming

Search existing practice before naming. Use a broad discipline name only when that single umbrella covers every Thing inside; when combining peer Things, use a natural phrase for the moment of need and keep individual technical terms inside the body as sourced anchors. Provenance lives on the Skill: spoken phrases in `description`, borrowed titles cited in `SKILL.md`, and new names marked `coined`.

## Quotes and locators

Link each mechanism to its primary source, adding a chapter, section, page, or timestamp on long sources:

- **Block quote (`>`)** verbatim when the original wording carries the rule, marking omissions with `[...]`. Put the link in the lead-in; consecutive quotes from the same source inherit it.
- **Locator link** on the concept words (`[Bates's berrypicking](url)`) or a compact end-of-sentence parenthetical (`([Author, Title](url), section/year)`) when only the mechanism matters; use last names for academics, org names for standards, and full names for podcast guests (`[Guest, Lex Fridman Podcast #NNN](url)`).

Write connecting prose only for gaps the quotes leave, and write it thin: a sentence that can be deleted without losing a mechanism is padding.

## Give information, not marching orders

State the goal, failure modes, and constraints rather than a rigid script ([Anthropic, Lessons from building Claude Code: How we use skills](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills)):

> Give Claude the information it needs, but give it the flexibility to adapt to the situation.

> The highest-signal content in any skill is the Gotchas section. These sections should be built up from common failure points that Claude runs into when using your skill.

Add rules only for observed failures ([David Heinemeier Hansson relaying Claude Code's Boris, Lex Fridman Podcast #501](https://lexfridman.com/dhh-2-transcript/)), and extract invariant mechanisms rather than incidental surface (rhetorical numbers, single-domain examples, repo file names, industry quirks).

Destructive or normalizing instructions carry a fence, [Chesterton's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence): reconstruct why material was written before deleting, folding, or rewriting it, and leave the owner's calls (ambiguous cases, scope, taste, irreversible choices) to the owner. Enumerated lists are open lists under a falsifiable test, not closed taxonomies; when a Skill could be over-applied, state what it is not in one line.

Never name a sibling Skill or outside tool; describe the behavior directly so the folder works copied alone.

A Skill that works from information carries the sync state: when what it needs is missing or conflicting, it names the gap and syncs with the user instead of guessing.

## Layout and debugging

Keep everything in `SKILL.md` until it outgrows a single read ([Anthropic, Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)):

> Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable.

> When the SKILL.md file becomes unwieldy, split its content into separate files and reference them.

Debug against the model on real tasks ([Anthropic, Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills); [Amanda Askell on prompt engineering, Lex Fridman Podcast #452](https://lexfridman.com/dario-amodei-transcript/), chapters Talking to Claude and Prompt engineering):

> Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts.

> As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

> I try and almost see myself from the position of the model and be like, what is the exact case that I would misunderstand or where I would just be like, I don't know what to do in this case.

> try to have empathy for the model. Read what you wrote as if you were a kind of person just encountering this for the first time

> What could I have said that would make you not make that error? Write that out as an instruction

## Sync and verification

On add, rename, split, or retirement, update `name`, every index the collection keeps (each index entry carrying the same trigger wording as the `description`), and every `grep` match; run the collection's validator when it ships one. Before finishing, fetch each linked source and diff every block quote in `SKILL.md` against the original.

When this file's conventions drift from stock Skills, surface the drift and confirm the retrofit before editing stock.
