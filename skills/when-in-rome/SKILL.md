---
name: when-in-rome
disable-model-invocation: true
description: "Match the nearest existing implementations and the house style before writing new code in a codebase that already has conventions. Use when adding a feature, function, test, or file to an established repository."
---

# When in Rome

Match local convention and depart only with a stated reason ([PEP 8](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)):

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

Check codified project rules and linter configs, then find the closest existing implementations in the same layer. Copy their design decisions (naming, file placement, error propagation, test setup, helpers, comment assumptions), not surface literals. If no prior pattern exists, flag that you are introducing a new one.

When eras conflict, prefer the same module over a distant one, newer over legacy, and common over one-off; name the exemplar you modeled on, and call out any deliberate departure with its reason. When conventions conflict beyond these preferences, name the gap and sync with the user instead of guessing.
