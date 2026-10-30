---
name: managing-up
disable-model-invocation: true
description: "Report finished work or escalate a decision to a delegator who did not follow the work. Use when an agent reports back, requests a decision, or answers a review."
---

# Managing Up

Named after [Gabarro and Kotter's Managing Your Boss](https://hbr.org/2005/01/managing-your-boss); weigh every update against the delegator's attention ([Horvitz, Jacobs and Hovel, Attention-Sensitive Alerting](https://erichorvitz.com/priorities.pdf)):

> We present models and inference procedures that balance the context-sensitive costs of deferring alerts with the cost of interruption.

> A system should relay information about a message when the net value of the alert (NEVA) is positive.

## What the report carries

1. **Outcome first**: what changed and the proof, with file or commit links; never a command log.
2. **Plain mechanism**: define unavoidable terms in a short clause or state what they do.
3. **Verified vs believed**: separate tool/test proof from assumptions, and proposed/written/tested/signed-off states.
4. **Named gaps**: call out anything you cannot explain simply, or close it first.

Account for every deliverable; label partial work with what is missing and the next step, and state the denominator of any percentage. Restore context briefly (goal, constraints, key choices, what the result unlocks), organized around what the delegator decides or uses next, with direct links to artifacts and outputs.

## Interrupt, escalate, or answer review

Interrupt only when waiting spoils the outcome or closes an option; otherwise batch by consequence. Escalate only owner-level choices (goal changes, out-of-scope cost/risk) in completed staff-work form (US Army doctrine, unsourced): the choice, recommendation, evidence, alternative consequence, and your next step once answered.

On review, surface any trade-off that breaks the agreed goal, clear up misunderstandings with context or a side-by-side comparison, and once the delegator decides, disagree and commit ([Jeff Bezos, Lex Fridman Podcast #405](https://lexfridman.com/jeff-bezos-transcript/)).

---

From [Feynman, Cargo Cult Science](http://calteches.library.caltech.edu/51/2/CargoCult.htm) (Caltech commencement 1974):

> The first principle is that you must not fool yourself—and you are the easiest person to fool.

Plain wording is not pretending the problem is simple ([Jordan Ellenberg, Lex Fridman Podcast #190](https://lexfridman.com/jordan-ellenberg/)), and a smooth explanation without verifiable substance leaves zero understanding ([Grant Sanderson on the Feynman effect, Lex Fridman Podcast #118](https://lexfridman.com/grant-sanderson-2/)).
