---
name: witnessed-commit
description: "Write a git commit as a claim with witnesses: the diff convicts the what, cited evidence convicts the why, and trailers carry enumerable claims. Use when writing, amending, or reviewing a commit message."
---

# Witnessed Commit

A commit message is a claim about a change: a claim a consumer will treat as fact must carry its witness, and unwitnessed claims belong at the boundary as views. The diff is the territory; the message is the map. Six moments, in the order the work meets them.

## Unit: what does this commit contain?

Willison's commit recipe, [The Perfect Commit](https://simonwillison.net/2022/Oct/29/the-perfect-commit/):

> Each commit should change a single thing.

> The goal is have something that can be easily reviewed, and that can be clearly understood in the future when revisited using tools like `git blame` or git bisect.

Anna Shipman in the GDS guide, [Working with Git](https://gds-way.digital.cabinet-office.gov.uk/standards/source-code/working-with-git.html):

> is self-contained
> only includes changes that achieve a specific step
> should be in a logical order

> As Anna Shipman describes it, they should tell a story.

The claim sizes the commit, not the edit. Both directions fail the same way: a fragment ("wip", "forgot the test", "address review") is a claim that cannot stand alone; a boulder is a diff carrying claims its subject never named. The sweet spot is the smallest unit that stands alone and the largest one honest subject can cover: the subject names the change without a conjunction, the diff contains no orphan changes, and the commit reads complete with its tests and docs. Spray while you work if you must; curate (amend, squash, rebase) before the record.

## Subject: the what-claim

GDS on the subject line, [Working with Git](https://gds-way.digital.cabinet-office.gov.uk/standards/source-code/working-with-git.html):

> A good commit message briefly summarises the "what" for scanning purposes [...]

> Commit messages should start with a one-line summary no longer than 50 characters [...] write these in the imperative mood, as if you are issuing a command to the repository.

Write one line the `git show` output can convict: read the subject, predict the diff, compare. Every verb in the subject names a change that physically exists in the diff; a verb the diff does not perform is a failed claim.

## Body: the evidence block

GDS on the body carrying why, [Working with Git](https://gds-way.digital.cabinet-office.gov.uk/standards/source-code/working-with-git.html):

> If the "what" in the message is not enough, the diff is there as a fallback. This is not true for the "why" of a change - this can be much harder or impossible to reconstruct [...]

ZeroExp's case for the why-message, [Write Commit Messages That Explain Why for Future Readers](https://zeroexp.dev/library/commit-messages-why):

> the diff is the what, so the message answers why now, why this way and what was ruled out. Include numbers when you have them, the symptom that triggered the change (an error text people can search for) [...]

The body discloses only what the diff cannot: a verbatim error string a searcher can grep, a measured number, the symptom observed before the fix. A sentence that explains how the change works restates the diff; a sentence that narrates the reasoning is a view and moves to the linked issue or design doc. Anything `git show` already proves (paths touched, tests added) is derivable noise. When nothing non-derivable exists, the body stays empty.

## Trailers: resolvable values only

the [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers) reference:

> A trailer in its simplest form is a key-value pair with a colon as a separator. [...] The trailer block is by definition at the end of the commit message.

A trailer survives when its value points outside the diff's reach: `Fixes: #412` (GitHub acts on it, the platform is the witness), `Link:`/`Refs:` to an issue thread, a decision record, a doc section the reader cannot infer from the change itself, `Co-authored-by:` on the kernel's precedent. A path inside the repo (`Refs: tests/x.mjs`) is derivable noise: `git show --name-only` already proves it. A classification key (`Intent:`, `Type:`) asserts a label nothing can convict. Both read as structure and pay as prose.

## Views: what leaves the record

Hyrum's Law itself, [hyrumslaw.com](https://www.hyrumslaw.com):

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

Every sentence you write becomes a dependency. Speculation, apology, and narration are views: they belong at the boundary (the linked issue, the PR body, the discussion) where they can be rebuilt, not inside the record. `Refs:` reaches the boundary without copying it.

## Review: every claim, one witness

Walk the message claim by claim:

- **Subject**: would `git show` convict it? Verbs matched against the diff.
- **Body**: does each sentence cite evidence a stranger could check: measurement, verbatim error, document, rejected alternative with its disqualifier?
- **Trailers**: does each value resolve to a checkable artifact rather than a label?

A claim with no witness moves to the boundary or is cut.

## Reference: shape of a witnessed commit

```text
Observe ref/out args as writes through references

`out x` handed the callee a write channel past signature-level
reads; ref mutations never reached the event stream.
```
