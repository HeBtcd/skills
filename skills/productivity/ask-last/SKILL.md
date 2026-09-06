---
name: ask-last
disable-model-invocation: true
description: Resolve dependencies, prune infeasible paths, and expose conflicts before asking consequential questions.
---

# Ask Last

Before asking, propagate existing answers through dependent choices and resolve factual unknowns from available evidence. Ask only consequential questions, prioritizing one that settles dependencies; propagate each answer before asking more.

Close branches only for supported reasons; reopen when those reasons change. Drop branch-specific questions, retain shared dependencies. Unknown feasibility is not infeasibility.

Give conflicting constraints and sources to their responsible owner; never silently relax them. Otherwise finish when required decisions are settled, or return remaining questions and affected choices.
