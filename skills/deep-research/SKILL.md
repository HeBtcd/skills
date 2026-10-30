---
name: deep-research
disable-model-invocation: true
description: "Find decision-relevant evidence such as field reports, real-world failure cases, and tested alternatives where generic summaries fall short. Use when a research question is substantive, or standard recommendations fail to settle an important decision."
---

# Deep Research

Treat the conventional answer as one candidate to test; if you reframe the question, verify it still solves the user's problem first.

## Match the evidence class to the question

- **Docs and specs**: author intent and interfaces ("what is it supposed to do?"); silent on production behavior.
- **Lab reports**: controlled benchmark capability ("can it do X at all?").
- **Field reports**: postmortems, incident reviews, experience reports, active repos' commit logs and issue trackers, carrying unpredicted failures, workarounds, and real cost ("does it hold up in practice?").
- **Derivative write-ups**: secondhand summaries with the failures stripped out.

Answering a production question from official docs is a category error.

## Follow leads and extract what changes a judgment

Use [Bates’s berrypicking](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html): chase citations, footnotes, practitioner output, and adjacent fields, letting each finding reshape the query. Probe cases with the [Critical Decision Method](https://www.gary-klein.com/cdm) for:
- **Unexpected failures**: what broke (a "field report" with zero failures is marketing or untested).
- **Dead ends**: what they tried and discarded.
- **Metrics**: what operators watch in production.
- **Mechanisms**: the gate or script that prevented recurrence, not a rule asking for care.

Any single report is a sample of one; extract the conditions under which it held, and corroborate or test claims that swing the decision.

## Verify and leave a trace

Vet sources with [SIFT](https://hapgood.us/2019/06/19/sift-the-four-moves/):

> The four moves: Stop, Investigate the source, find better coverage, trace the original context.

Apply the same bar to counterevidence, separate measured facts from war stories and inference, link every load-bearing claim ([Aravind Srinivas on source-backed answers, Lex Fridman Podcast #434](https://lexfridman.com/aravind-srinivas-transcript/)), and distrust sources that flatter your hypothesis ([Dave Smith, Lex Fridman Podcast #464](https://lexfridman.com/dave-smith-transcript/)). Stop when new leads stop changing the answer; lead with the decision, the evidence that settled it, its conditions, and open unknowns. When the evidence a decision needs is missing or conflicting, name the gap and sync with the user instead of guessing.

Record your own run so future runs inherit it ([Google SRE, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)):

> The cost of failure is education.

> An unreviewed postmortem might as well never have existed.
