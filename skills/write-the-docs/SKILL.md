---
name: write-the-docs
disable-model-invocation: true
description: "Write or edit project documentation. Use when writing a README, design doc, module doc, or task record."
---

# Write the Docs

## Voice and structure

From the [Microsoft Writing Style Guide’s top ten style tips](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice):

> Shorter is always better.

> Write like you speak. Read your text aloud. Avoid jargon and overly complex or technical language.

> Lead with what's most important. Front-load keywords for scanning.

> Give customers just enough information to make decisions confidently. Prune every excess word.

> Most of the time, start each statement with a verb. Edit out you can when it isn't necessary. Avoid weak phrasing like there is, there are, and there were.

Add code examples only where needed to understand or use the thing. Follow the [Google developer documentation style guide’s highlights](https://developers.google.com/style/highlights): second person ("you") and active voice, conditions before instructions, sentence-case headings, numbered lists for sequences, bullets for unordered items, description lists for key-value pairs, code font for symbols, bold for UI labels, descriptive link text, unambiguous dates, alt text, and no pre-announced unshipped features. Defer spelling, punctuation, and contractions to the repo's convention.

Run the sentence-level checks from [Google Technical Writing One](https://developers.google.com/tech-writing/one), Words and Active voice:

> * Only use a pronoun *after* you've introduced the noun; never use the pronoun before you've introduced the noun.
> * Place the pronoun as close as possible to the referring noun. In general, if more than five words separate your noun from your pronoun, consider repeating the noun instead of using the pronoun.
> * If you introduce a second noun between your noun and your pronoun, reuse your noun instead of using a pronoun.

> Use the active voice most of the time. Use the passive voice sparingly.

Convert passive voice (`form of be` + past participle) to active (actor + verb + target) when the actor matters; prefer precise verbs over *be*, *occur*, and *happen* and delete *There is*/*There are* openers ([clear sentences](https://developers.google.com/tech-writing/one/clear-sentences)); keep one term per thing and spell an acronym out on first use; split multi-idea sentences into single-idea ones and refactor embedded enumerations into bulleted or numbered lists ([short sentences](https://developers.google.com/tech-writing/one/short-sentences)).

## Module docs and records

From the [Google timeless documentation page](https://developers.google.com/style/timeless-documentation) and [Nygard, Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Decision:

> In contrast, timeless documentation focuses on how the product works right now—not on how it has changed from previous versions, and not how it might change in the future.

> If a decision is reversed, we will keep the old one around, but mark it as superseded.

Keep rollout stages and future plans in task or issue trackers, not module docs; append new decision or task entries rather than rewriting history, and leave decision records to their owners. Re-read every added or edited sentence against these rules before finishing. When the material or audience the document needs is missing or conflicting, name the gap and sync with the user instead of guessing.
