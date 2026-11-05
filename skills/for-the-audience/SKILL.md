---
name: for-the-audience
disable-model-invocation: true
description: "Turn messy working materials into a self-contained document written for the audience that was not in the room. Use when threads, notes, or review back-and-forth must become a document."
---

# For the Audience

Start from the [audience page of Google Technical Writing](https://developers.google.com/tech-writing/one/audience):

> In other words, make sure your document provides the information that your audience needs but doesn't already have.

The failure this guards against is the [curse of knowledge](https://doi.org/10.1086/261609) (Camerer, Loewenstein & Weber, JPE 97(5), 1989): knowing a thing makes you unable to simulate not knowing it, so a doc silently assumes the reader's missing facts. The counter-procedure is the field's own term, audience analysis — enumerate who reads it, what they already have, and what they need next.

Reconstruct what is true today against actual code or output; when a later message corrects an earlier one, update only what that correction touches. Structure around the reader's path (prerequisites, inputs, steps, verification), keeping real caveats and never inventing requirements to fill a template.

Fold lasting corrections into the text and delete the back-and-forth, dead ends, one-off instructions, and compliance-only filler (route tool-only blocks to configs, fixtures, or logs; keep "why not X" only when it changes reader action; put the build narrative in a separate report unless writing a retrospective).

Verify from a newcomer's state using only the document and its links, flagging missing facts instead of guessing. Settle competing drafts by asking which reader the document serves, and test on a fresh reader when possible.
