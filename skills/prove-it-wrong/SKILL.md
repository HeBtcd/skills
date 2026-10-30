---
name: prove-it-wrong
disable-model-invocation: false
description: "Stop proving yourself right: try to break the claim until it fails or earns trust. Use when an agent has convinced itself by piling up supporting reasons, before accepting a self-built conclusion or a fix that merely 'should work'."
---

# Prove It Wrong

From [Popper, Science: Conjectures and Refutations](https://archive.org/details/conjecturesrefut0000popp):

> It is easy to obtain confirmations, or verifications, for nearly every theory — if we look for confirmations.

> Confirmations should count only if they are the result of risky predictions [...]

> A theory which is not refutable by any conceivable event is non-scientific. Irrefutability is not a virtue of a theory (as people often think) but a vice.

State the claim sharply enough to name the concrete observation that would falsify it, then attack it with [Platt, Strong Inference](https://doi.org/10.1126/science.146.3642.347) (Science 1964) and [Chamberlin, The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754) (Science 1890, repr. 1965):

> Strong inference consists of applying the following steps to every problem in science, formally and explicitly and regularly:
> 1) Devising alternative hypotheses;
> 2) Devising a crucial experiment (or several of them), with alternative possible outcomes, each of which will, as nearly as possible, exclude one or more of the hypotheses;
> 3) Carrying out the experiment so as to get a clean result;
> 4) Recycling the procedure, making subhypotheses or sequential hypotheses to refine the possibilities that remain [...]

> Any conclusion that is not an exclusion is insecure and must be rechecked.

> Love was long since represented as blind, and what is true in the personal realm is measurably true in the intellectual realm.

Put rival hypotheses on the table and test where their predictions split. For universal claims ("all inputs, replays, or orderings"), encode the invariant (round-trip inversion, idempotency, conservation/monotonicity, authorization bounds, reference equivalence) and hunt counterexamples across the input space with property-based testing ([Claessen and Hughes, QuickCheck](https://doi.org/10.1145/351240.351266), ICFP 2000).

Count a passing test only when it had a real chance to fail, and build the strongest case that your conclusion is wrong in a fresh context that did not produce it; the context that piled up the confirmations will keep finding them, and an attacker with no stake in the answer is the only honest one. If both sides argue equally well, evidence is insufficient. Report what you attacked, what broke and replaced it, what survived, and what remains untested.
