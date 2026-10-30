---
name: read-between-the-lines
disable-model-invocation: true
description: "Read between the lines: infer the unspoken goal from context and check the workspace before asking the user. Use when a message is short, vague, or corrective."
---

# Read Between the Lines

Work the two steps in order; stop as soon as the message is clear.

## 1. Infer what the message serves

Every message advances a question already on the table ([Roberts, Information structure in discourse](https://doi.org/10.3765/sp.5.6)):

> A move m is Relevant to the question under discussion q, i.e., to last(QUD(m)), iff m either introduces a partial answer to q (m is an assertion) or is part of a strategy to answer q (m is a question). Cooperative speakers strive to make their utterances Relevant, in keeping with the goals of the game.

- An example, comparison, or correction sets the direction; treat its incidental details as context, not requirements.
- A pushback rejects that proposal; it does not vote for the opposite extreme.
- A back-reference recovers the earlier question and goal.

State any consequential inferred goal out loud so the user can correct it.

## 2. Look before you ask

Check the files, git history, and conversation before asking a fact you can look up yourself. If intent stays ambiguous, ask the smallest concrete question (a small set of options) that settles the fork.
