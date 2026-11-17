# AGENTS.md

Agent skills live under `skills/<bucket>/<name>/SKILL.md` (source of truth): `personal/` holds this collection's own doctrine and tooling, `moments/` holds the rest, indexed by moment of need. Read `skills/personal/hebtcd-skill-creator/SKILL.md` before editing any skill.

## Rules

- Keep prose plain and free of em-dashes.
- When a skill changes, keep `README.md` and `.claude-plugin/plugin.json` in sync.
- Run `claude plugin validate . --strict` after editing `.claude-plugin/`.
