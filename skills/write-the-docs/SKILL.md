---
name: write-the-docs
disable-model-invocation: true
description: "Write or edit project documentation: the README, the design doc, the module doc, the decision record, the changelog. Use when a project document needs writing or re-cutting: naming which kind it is, drafting it for the reader who needs it, or checking that it still tells the truth."
---

# Write the Docs

Project documentation is a small set of named documents, each answering a question the code cannot. Seven moments, in the order the work meets them.

## 1. Kind: which of the four is this document?

Daniele Procida's [documentation system](https://documentation.divio.com/), now Diátaxis:

> There is a secret that needs to be understood in order to write good software documentation: there isn't one thing called *documentation*, there are four.

> They are: *tutorials*, *how-to guides*, *technical reference* and *explanation*. They represent four different purposes or functions, and require four different approaches to their creation.

Procida, [Diátaxis](https://diataxis.fr/):

> Diátaxis solves problems related to documentation *content* (what to write), *style* (how to write it) and *architecture* (how to organise it).

Name which of the four the document is before writing it; the need decides its content, its style, and where it lives.

## 2. README: the file written first

Tom Preston-Werner, [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development):

> Write your Readme first.

> First. As in, before you write any code or tests or behaviors or stories or ANYTHING.

> By restricting your design documentation to a single file that is intended to be read as an introduction to your software, RDD keeps you safe from DDD-turned-waterfall syndrome by punishing you for lengthy or overprecise specification.

> The Readme should be the single most important document in your codebase; writing it first is the proper thing to do.

What it answers: [Make a README](https://www.makeareadme.com/):

> A README is a text file that introduces and explains a project. It contains information that is commonly required to understand what the project is about.

> It's an easy way to answer questions that your audience will likely have regarding how to install and use your project and also how to collaborate with you.

> It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

How much detail: Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/getting-started.html), on the principle of scaled presentation:

> the degree of detail presented at each stage should correspond to the amount of time and effort put in by the reader at that stage. More effort should always result in more reward.

> Newcomers, on the other hand, need all these things. Fortunately, they don't need them all at once.

## 3. Design doc: write down the trade-offs

Malte Ubl, [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/):

> The design doc documents the high level implementation strategy and key design decisions with emphasis on the trade-offs that were considered during those decisions.

> Design docs are informal documents and thus don't follow a strict guideline for their content. Rule #1 is: Write them in whatever form makes the most sense for the particular project.

> The design doc is *the place to write down the trade-offs* you made in designing your software. Focus on those trade-offs to produce a useful document with long-term value.

> This section lists alternative designs that would have reasonably achieved similar outcomes. The focus should be on the trade-offs that each respective design makes and how those trade-offs led to the decision to select the design [...]

> Design docs should be sufficiently detailed but short enough to actually be read by busy people.

The check, same source:

> If a doc basically says "This is how we are going to implement it" without going into trade-offs, alternatives, and explaining decision making (or if the solution is so obvious as to mean there were no trade-offs), then it would probably have been a better idea to write the actual program right away.

## 4. Module doc: explain to human beings

Donald Knuth, [Literate Programming](http://literateprogramming.com/knuthweb.pdf), The Computer Journal 27(2), 1984:

> Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.

> The practitioner of literate programming can be regarded as an essayist, whose main concern is with exposition and excellence of style.

> He or she strives for a program that is comprehensible because its concepts have been introduced in an order that is best for human understanding, using a mixture of formal and informal methods that reinforce each other.

A module doc is this essay at file scale: what the module is for, its concepts in the order a reader needs them.

## 5. Decision record: the why, one file at a time

Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):

> Documents that assist the team itself can have value, but only if they are kept up to date. Large documents are never kept up to date. Small, modular documents have at least a chance at being updated.

> We will keep a collection of records for "architecturally significant" decisions: those that affect the structure, non-functional characteristics, dependencies, interfaces, or construction techniques.

> Each record describes a set of forces and a single decision in response to those forces.

Its format, same source:

> **Context** This section describes the forces at play, including technological, political, social, and project local. [...] **Decision** This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …" [...] **Consequences** This section describes the resulting context, after applying the decision.

> We will write each ADR as if it is a conversation with a future developer.

> If a decision is reversed, we will keep the old one around, but mark it as superseded.

## 6. Changelog: the record of what changed

Olivier Lacan, [Keep a Changelog](https://keepachangelog.com/en/1.1.0/):

> A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

> To make it easier for users and contributors to see precisely what notable changes have been made between each release (or version) of the project.

> * Changelogs are *for humans*, not machines.
> * There should be an entry for every single version.
> * The same types of changes should be grouped.
> * Versions and sections should be linkable.
> * The latest version comes first.
> * The release date of each version is displayed.

> * `Added` for new features.
> * `Changed` for changes in existing functionality.
> * `Deprecated` for soon-to-be removed features.
> * `Removed` for now removed features.
> * `Fixed` for any bug fixes.
> * `Security` in case of vulnerabilities.

> Keep an `Unreleased` section at the top to track upcoming changes.

## 7. Check: the document still tells the truth

Anne Gentle, [Docs Like Code](https://www.docslikecode.com/about/):

> Treating docs like code is:
> * [...] keeping docs close to code or in the same system as code, with a source file concept and an output for deliverables.
> * [...]
> * Applying software development tools and techniques to documentation about software, application programming interfaces (APIs), or other technical topics.
> * [...]
> * Valuing technical accuracy and consistency.

Python documentation, [doctest - Test interactive Python examples](https://docs.python.org/3/library/doctest.html):

> The `doctest` module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown.

> To check that a module's docstrings are up-to-date by verifying that all interactive examples still work as documented.

> To write tutorial documentation for a package, liberally illustrated with input-output examples. [...] this has the flavor of "literate testing" or "executable documentation".

A document that fails a reader lands on the moment that failed (a broken install step falsifies the README, a missing rationale is a record never written) and when no moment owns the failure, the project is missing a document.
