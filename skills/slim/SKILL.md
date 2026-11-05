---
name: slim
disable-model-invocation: true
description: "Simplify an artifact from the design down: a smaller decomposition, a smaller replacement, or a measured share of removable parts. Use when something is bloated: slim it, cut it down, simplify it, or minimize a failing repro."
---

# Slim

From Aquinas's formulation of Ockham's razor ([SEP, Simplicity](https://plato.stanford.edu/entries/simplicity/)):

> If a thing can be done adequately by means of one, it is superfluous to do it by means of several; for we observe that nature does not employ two instruments where one suffices [...]

The motive: code is inventory, not wealth — every line carries maintenance, review, and porting cost, so deletion is debt repayment ([Poppendieck & Poppendieck, *Lean Software Development*](https://www.poppendieck.com/), 2003; [Atwood, The Best Code is No Code At All](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/)). The same principle at write time is YAGNI: never take on liability for a speculative need. The borrowing side is [technical debt](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) (Ward Cunningham, 1992): a shortcut is a loan whose interest lands on future maintainers — prudent debt is recorded, reversible, and has a repayment trigger; reckless debt is invisible and compounding, so audit it first.

Pick the deliverable: **smaller decomposition** (Mode B from essence/accident sort), **smaller replacement** (Mode B), or **measured share** (Mode A).

## Simplify the design before its parts

Separate essential from accidental complexity ([Brooks, No Silver Bullet](https://doi.org/10.1109/MC.1987.1663532), IEEE Computer 20(4), 1987):

> Following Aristotle, I divide them into essence — the difficulties inherent in the nature of software — and accidents — those difficulties that today attend its production but are not inherent.

Before cutting an abstraction, extension seam, or branch, reconstruct *why* it was put there ([Chesterton's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence), G. K. Chesterton, *The Thing*, 1929): whenever a cut narrows capability, removes a deliberate seam, or touches ambiguous intent, synchronize with the user first.

## Phase 1 — baseline, confirmed

Establish what the artifact is for and pin its current behavior as the spec before the first cut — characterization tests (Feathers, *Working Effectively with Legacy Code*, 2004), the oracle — the check deciding whether the artifact still fulfills its promise ([Barr et al., The Oracle Problem in Software Testing](https://doi.org/10.1109/TSE.2014.2372785), §6; [value engineering](https://en.wikipedia.org/wiki/Value_engineering)) — plus the counting unit and baseline commit. What is load-bearing is a product decision: present the baseline to the owner and get sign-off before cutting.

## Phase 2 — the procedure

Delete a candidate part, run the oracle, keep passing cuts (and strip their orphaned tests, configs, adapters, fixtures, and docs), revert failing cuts, and flag unexercised parts as untested rather than removable. Resolve every inconsistency toward the side with no consumers (`coined: two-sided deletion`): an unimplemented claim nobody relies on is deleted, not built (redocumentation, Chikofsky & Cross 1990; code as design, Reeves 1992); orphaned code dies only after the consumer graph proves it dead.

Never weaken the oracle (specification gaming), never leave scope, and if no trustworthy oracle exists, stop and say so.

## Mode A: measured share

Halve candidate sets rather than cutting one by one, reporting the result as a proven lower bound because greedy halving lands in a local minimum ([Zeller and Hildebrandt, ddmin](https://doi.org/10.1109/32.988498)); on nested structures, strip coarsest to finest ([Misherghi and Su, HDD](https://www.cs.ucdavis.edu/~su/publications/icse06-hdd.pdf)):

> While removing two or more changes at once may result in an even smaller, still failing test case, every single change on its own is significant in reproducing the failure.

> In particular, we apply the original Delta Debugging algorithm to each level of a program's input, working from the coarsest to the finest levels.

When entry points are unknown, delete everything and restore until green. Report a graduated table (zero-loss removable share first, then optional-feature trade-offs for the owner to decide) with commands, oracle, untested parts, surviving core, and failed cuts.

## Mode B: smaller replacement

List required behavior, constraints, scope, and intended seams (asking the user on ambiguity); measure the baseline, sketch a clean-sheet replacement, and challenge every layer, dependency, state field, and branch across full lifecycle cost. Drop dominated options, surface real trade-offs without invented weights, keep only proven simplifications within scope, and stop when returns diminish; let the fixed oracle, not the focusing illusion, judge the win ([Daniel Kahneman, Lex Fridman Podcast #65](https://lexfridman.com/daniel-kahneman/)).
