# skills-in-progress

The HeBtcd skill collection. Every folder under `skills/` is a self-contained Skill; `skills/hebtcd-skill-creator/SKILL.md` is the meta-skill that defines what a Skill is (pointer in front of an ordered basis of Things) and the rules every change obeys. Read it before editing any `SKILL.md`.

## Layout

- `skills/<name>/SKILL.md` is the source of truth.
- `~/.agents/.generated/<name>/SKILL.md` is the installed copy: identical content plus a `metadata: {"opencode/autoinvoke": "false"}` line inserted at line 2, inside the frontmatter. Regenerate it after every skill edit.
- `README.md` carries one row per skill: name linked to its `SKILL.md`, description column matching the frontmatter `description` (parenthetical or trailing appendages may be set off with punctuation per the prose style).
- `.claude-plugin/plugin.json` lists every promoted skill path. `.scratch/` is gitignored scratch space (audits, clean-room rewrites, working notes); never reference it from tracked files.

## Prose style

- No em-dashes anywhere in prose: `SKILL.md` seams, headings, lead-ins, frontmatter, `README.md`, this file. Where a sentence reaches for one, rewrite with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never a blind character substitution. Verbatim block quotes (`>` lines) keep the source's own punctuation.
- Links point at the copy an agent can actually fetch and diff (archive.org scans, transcriptions, mirrors); the canonical title and year live in the attribution text.

## Verify

`claude plugin validate . --strict` after touching `.claude-plugin/`. After any basis change in a skill: sync README row, `.generated` copy, and `plugin.json`; then fetch each linked source and diff every block quote against the original.
