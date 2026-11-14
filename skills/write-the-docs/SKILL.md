---
name: write-the-docs
disable-model-invocation: true
description: "Write or re-cut a project document in its established form: README, design doc, decision record (ADR), or changelog. Use when a project needs a document drafted, or an existing one brought back in step with the thing it describes."
---

# Write the Docs

A project document is a promise to a reader who was not in the room. Seven moments, in the order the work meets them. The four format moments are branches; only the one matching your document fires.

## 1. The need: name the job this document does

Diátaxis, [diataxis.fr](https://diataxis.fr/):

> Diátaxis identifies four distinct needs, and four corresponding forms of documentation - *tutorials*, *how-to guides*, *technical reference* and *explanation*. It places them in a systematic relationship, and proposes that documentation should itself be organised around the structures of those needs.

> Diátaxis solves problems related to documentation *content* (what to write), *style* (how to write it) and *architecture* (how to organise it).

Name the need this document serves before drafting; it settles what belongs in it and what links out.

## 2. The README: the project's front page

Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/getting-started.html), ch. 2:

> [...] the degree of detail presented at each stage should correspond to the amount of time and effort put in by the reader at that stage. More effort should always result in more reward.

> [...] the next thing people will look for is a quick description or mission statement, so they can decide (within 30 seconds) whether or not they're interested in learning more.

> The description should be concrete, limiting, and above all, short.

> [...] it's okay to assume a minimally informed reader with a baseline level of technical preparedness.

> There should be a brief list of the features the software supports (if something isn't completed yet, you can still list it, but put "*planned*" or "*in progress*" next to it), and the kind of computing environment required to run the software.

> *The front page must make it unambiguously clear that the project is open source.*

> Don't be afraid of looking unready, and never give in to the temptation to inflate or hype the development status.

> Visitors usually want to know how to reach the human beings involved with the project.

> You can treat them as a checklist. [...] go down the list and make sure you've got each item covered, or at least that you're comfortable with the potential consequences if you've left one out.

Answer the newcomer's questions in the order they arrive: what it is, what it does, how real it is today, where to get it, where to talk.

## 3. The design doc: trade-offs before code

Malte Ubl, [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/):

> [...] relatively informal documents that the primary author or authors of a software system or application create before they embark on the coding project. The design doc documents the high level implementation strategy and key design decisions with emphasis on the trade-offs that were considered during those decisions.

> The design doc is *the place to write down the trade-offs* you made in designing your software.

> [...] non-goals aren't negated goals like “The system shouldn’t crash”, but rather things that could reasonably be goals, but are explicitly chosen not to be goals.

> This section lists alternative designs that would have reasonably achieved similar outcomes. The focus should be on the trade-offs that each respective design makes and how those trade-offs led to the decision to select the design that is the primary topic of the document.

> Design docs should be sufficiently detailed but short enough to actually be read by busy people.

> A clear indicator that a doc might not be necessary are design docs that are really *implementation manuals*. If a doc basically says “This is how we are going to implement it” without going into trade-offs, alternatives, and explaining decision making [...] then it would probably have been a better idea to write the actual program right away.

> If the designed system hasn’t shipped yet, then definitely update the doc.

> [...] changes are often isolated into new documents. [...] Links to such amendments from the original doc can be immensely helpful for the poor future maintenance programmer trying to understand their target system through design doc archaeology.

Write it before the code, around the trade-offs: context and scope, goals and non-goals, the design, alternatives considered, cross-cutting concerns.

## 4. The decision record: forces and a single decision

Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):

> We will keep a collection of records for "architecturally significant" decisions: those that affect the structure, non-functional characteristics, dependencies, interfaces, or construction techniques.

> Each record describes a set of forces and a single decision in response to those forces.

> We will keep ADRs in the project repository under doc/arch/adr-NNN.md [...] ADRs will be numbered sequentially and monotonically. Numbers will not be reused.

> **Title** These documents have names that are short noun phrases. [...]

> **Context** This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.

> **Decision** This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …"

> **Status** A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its replacement.

> **Consequences** This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones.

> The whole document should be one or two pages long. We will write each ADR as if it is a conversation with a future developer.

> If a decision is reversed, we will keep the old one around, but mark it as superseded. (It's still relevant to know that it *was* the decision, but is *no longer* the decision.)

Give each significant decision its own record: title, context, decision, status, consequences; a reversed decision gets superseded, never rewritten.

## 5. The changelog: the curated version history

Olivier Lacan, [Keep a Changelog](https://keepachangelog.com/en/1.1.0/):

> A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

> The purpose of a changelog entry is to document the noteworthy difference, often across multiple commits, to communicate them clearly to end users.

> * Changelogs are *for humans*, not machines.
> * There should be an entry for every single version.
> * The same types of changes should be grouped.
> * Versions and sections should be linkable.
> * The latest version comes first.
> * The release date of each version is displayed.
> * Mention whether you follow [Semantic Versioning](https://semver.org/).

> * `Added` for new features.
> * `Changed` for changes in existing functionality.
> * `Deprecated` for soon-to-be removed features.
> * `Removed` for now removed features.
> * `Fixed` for any bug fixes.
> * `Security` in case of vulnerabilities.

> Keep an `Unreleased` section at the top to track upcoming changes.

> If you do nothing else, list deprecations, removals, and any breaking changes in your changelog.

> Call it `CHANGELOG.md`. Some projects use `HISTORY`, `NEWS` or `RELEASES`.

On rewriting one, the same source answers:

> Sure. There are always good reasons to improve a changelog.

> [...] having a good changelog means having a consistently updated changelog.

Log an entry for every version, newest first, dated, with changes grouped under the six types and landed work tracked under Unreleased.

## 6. The prose: every word tells

William Strunk, [The Elements of Style](https://www.gutenberg.org/files/37134/37134-h/37134-h.htm), ch. III:

> Vigorous writing is concise. A sentence should contain no unnecessary words, a paragraph no unnecessary sentences, for the same reason that a drawing should have no unnecessary lines and a machine no unnecessary parts. This requires not that the writer make all his sentences short, or that he avoid all detail and treat his subjects only in outline, but that he make every word tell.

> Make definite assertions. Avoid tame, colorless, hesitating, non-committal language. [...] the reader is dissatisfied with being told only what is not; he wishes to be told what is.

> The active voice is usually more direct and vigorous than the passive: [...]

Run the cut pass: every word in the doc earns its place in the reader's job, and every statement says what is.

## 7. The test: every page is page one

Mark Baker, [Every Page is Page One](https://www.everypageispageone.com/2011/08/09/every-page-is-page-one-topics-are-everywhere/):

> Whether a reader finds information by searching, or by surfing links on other pages, or even by browsing the landing page of a website, the page they arrive at is page one for them.

> The essential characteristic of an Every Page is Page One topic is that it stands alone [...]

> An Every Page is Page One topic:
> * is self-contained
> * has a specific and limited purpose
> * establishes its context
> * stays on one level
> * often conforms to a type
> * assumes that the reader is qualified
> * is as long as it needs to be
> * is the smallest unit of reference

Read the finished doc as the stranger who just landed on it: it establishes its own context, does one job, and matches the shape its section above promises.
