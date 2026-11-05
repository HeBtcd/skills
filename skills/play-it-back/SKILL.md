---
name: play-it-back
disable-model-invocation: true
description: "Read the message, then play it back: infer the unspoken goal from context and workspace before asking, restate the user's goal and the problem behind it, and complete the statement to well-structured form so the root cause surfaces or the missing cell names the one question worth asking. Use when a request is short, vague, or corrective, or the literal ask may not be the real goal."
---

# Play It Back

Use [reflective listening](https://en.wikipedia.org/w/index.php?title=Reflective_listening&oldid=1364180587) (Carl Rogers, *Client-Centered Therapy*, 1951; Rogers and Farson, *Active Listening*, 1987):

> Reflective listening is a communication strategy in which a listener improves their understanding of a speaker's idea by offering that understanding back to the speaker in order to confirm that the idea has been understood correctly.

Read before you play back: every message advances a question already on the table ([Roberts, Information structure in discourse](https://doi.org/10.3765/sp.5.6)):

> A move m is Relevant to the question under discussion q, i.e., to last(QUD(m)), iff m either introduces a partial answer to q (m is an assertion) or is part of a strategy to answer q (m is a question). Cooperative speakers strive to make their utterances Relevant, in keeping with the goals of the game.

An example, comparison, or correction sets the direction — treat its incidental details as context, not requirements; a pushback rejects that proposal, not a vote for the opposite extreme; a back-reference recovers the earlier question and goal. Check the files, git history, and conversation for facts you can look up yourself before asking; if intent stays ambiguous, ask the smallest concrete question that settles the fork.

Play back two things in plain sentences: the outcome the user wants and the problem it solves. Mark what you inferred versus heard directly; if they gave only *how* without *why*, mark the goal as unconfirmed. Stop and wait for confirmation before acting.

## Playback as completion

Restating is not only verification — a problem well stated is half solved (*formulation is often more essential than its solution*, Einstein and Infeld, *The Evolution of Physics*, 1938; [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging), Hunt and Thomas, *The Pragmatic Programmer*, 1999). Before answering, complete the statement into its well-structured form: inputs, expected, actual, constraints.

- If completing it exposes the root cause, the question was the solution — give it directly instead of restating.
- If it does not, the cell you could not fill is the one question worth asking. A problem that cannot be stated apart from its solution is a [wicked problem](https://doi.org/10.1007/BF01405730) (Rittel and Webber, 1973) and needs a different path, not a better paraphrase.

Drill the statement down to mechanism, not first symptom ([five whys](https://en.wikipedia.org/wiki/Five_whys), Toyota): an answer that only renames the symptom is a premise to check, not a root cause.
