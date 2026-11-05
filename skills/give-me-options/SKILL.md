---
name: give-me-options
disable-model-invocation: true
description: "Ask the smallest, easiest-to-answer question that unblocks a decision by giving concrete options to compare. Use when intent or preference remains unresolved after checking context and a question is owed."
---

# Give Me Options

Ask only what unblocks the next decision ([Boutilier, A POMDP Formulation of Preference Elicitation Problems](https://cdn.aaai.org/AAAI/2002/AAAI02-037.pdf)):

> An optimal decision can usually be made without full knowledge of a user's preferences.

Offer a small set of concrete options or examples that isolate the trade-off while holding everything else equal.

Ask which difference matters, and let the user reject every option. Treat incidental example details as provisional, apply the answer directly, and if you store the preference, save the options compared, the pick, and the context. When the user does not know what to ask next, suggest concrete follow-up questions alongside the answer.
