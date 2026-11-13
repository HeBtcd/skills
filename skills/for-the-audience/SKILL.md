---
name: for-the-audience
disable-model-invocation: true
description: "Turn threads, notes, and review back-and-forth into a self-contained document for the audience that was not in the room. Use when a pile of working materials must stand alone for readers who lack the backstory: will a stranger be able to read it?"
---

# For the Audience

Working materials are written to the room that produced them; a document is written to the audience that was not in it. Eight moments, in the order the work meets them.

## 1. Writer-based: what the materials are

Linda Flower, [Writer-Based Prose: A Cognitive Basis for Problems in Writing](https://mwover.com/wp-content/uploads/2018/05/flower-writer-based-prose.pdf) (College English 41(1), 1979):

> In function, Writer-Based prose is a verbal expression written by a writer to himself and for himself. It is the record and the working of his own verbal thought. In its structure, Writer-Based prose reflects the associative, narrative path of the writer's own confrontation with her subject. In its language, it reveals her use of privately loaded terms and shifting but unexpressed contexts for her statements.

> In contrast, Reader-Based prose is a deliberate attempt to communicate something to a reader. To do that it creates a shared language and shared context between writer and reader. It also offers the reader an issue-centered rhetorical structure rather than a replay of the writer's discovery process.

> Good writing, therefore, is often the cognitively demanding transformation of the natural but private expressions of Writer-Based thought into a structure and style adapted to a reader.

The thread and the notes replay the order in which the room discovered things; the document must be rebuilt around the reader. Find the privately loaded terms and the unexpressed contexts: each marks a place where the room's knowledge was doing the work.

## 2. Audience: what the reader needs minus what they have

Google's Technical Writing course, [Audience](https://developers.google.com/tech-writing/one/audience):

> good documentation = knowledge and skills your audience needs to do a task − your audience's current knowledge and skills

> In other words, make sure your document provides the information that your audience needs but doesn't already have.

> Write down a list of everything your target audience needs to learn to accomplish goals.

> Experts often suffer from the curse of knowledge, which means that their expert understanding of a topic ruins their explanations to newcomers. As experts, it is easy to forget that novices don't know what you already know.

Name who reads this and list what the document owes them; the room's shared knowledge is invisible to the writer, so inventory it rather than trust memory of it.

## 3. The lead: the outcome first, details by weight

Wikipedia, [Inverted pyramid (journalism)](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)):

> The widest part at the top represents the most substantial, interesting, and important information that the writer means to convey, illustrating that this kind of material should head the article, while the tapering lower portion illustrates that other material should follow in order of diminishing importance.

> First, readers can leave the story at any point and understand it, even if they do not have all the details.

> The opposite, the failure to mention the most important, interesting or attention-grabbing elements of a story in the opening paragraphs, is called burying the lead

Move what the room concluded to the opening; arrange what follows so the reader can stop anywhere and still carry the point away.

## 4. The ground: the context the room stood on

Malte Ubl, [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), on the sections that bring a reader up to speed:

> This section gives the reader a very rough overview of the landscape in which the new system is being built and what is actually being built. [...] The goal is that readers are brought up to speed but some previous knowledge can be assumed and detailed info can be linked to. This section should be entirely focused on objective background facts.

> Note, that non-goals aren't negated goals like "The system shouldn't crash", but rather things that could reasonably be goals, but are explicitly chosen not to be goals.

> [...] this section is one of the most important ones as it shows very explicitly why the selected solution is the best given the project goals and how other solutions, that the reader may be wondering about, introduce trade-offs that are less desirable given the goals.

Restore the background facts the room took for granted; fence the territory with goals and the chosen-not-to goals; name the rejected paths the reader would otherwise re-propose.

## 5. The record: the decision and everything it costs

Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):

> One of the hardest things to track during the life of a project is the motivation behind certain decisions. A new person coming on to a project may be perplexed, baffled, delighted, or infuriated by some past decision. Without understanding the rationale or consequences, this person has only two choices: **Blindly accept the decision.** [...] **Blindly change it.** [...] It's better to avoid either blind acceptance or blind reversal.

> **Decision** This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …"

> **Status** A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its replacement.

> **Consequences** This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them affect the team and project in the future.

> We will write each ADR as if it is a conversation with a future developer.

State what the room decided in full sentences, list every consequence including the ones that embarrass it, and mark what is still open so the record does not read as settled where it is not.

## 6. The voice: one document, not a transcript

The c2 Wiki's conventions for refactoring discussion into document, [ConvertThreadModeToDocumentMode](https://kidneybone.com/c2/wiki/ConvertThreadModeToDocumentMode):

> Replace a thread mode conversation with a monologue that says the same thing and preserving as much of the original text as possible. Change the 1st person singular to 1st or 3rd person plural. Remove the inline attributions and put them at the end under "Contributors:".

> You need to synthesize the discussion in a way that is acceptable to most of the participants. [...] Discussions most need to be summarized when they get long, which usually means there are a lot of different opinions, making them hard to summarize.

> It is a GoodThing to present in the Wiki both ideas as clearly and persuasively as possible. Do not attempt to make the Wiki pronounce only your truth.

And on why, the same Wiki's [DocumentMode](https://kidneybone.com/c2/wiki/DocumentMode):

> A good DocumentMode comment is easier for newcomers to understand than a ThreadMode one. Threads are full of transient misunderstandings and special cases. The important points don't stand out well. And they are full of egos.

> If you write a comment and someone else queries one of your points or wants something clarified, don't write a 3rd comment: rewrite your original to make it clearer. And then delete the question so only your first comment remains.

Synthesize the voices into one unsigned voice; fold each answered question back into the text it clarified rather than leaving the exchange standing; move surviving disagreements into the rejected paths of moment 4.

## 7. The language: self-contained, terms before use

Wikipedia's guideline [Make technical articles understandable](https://en.wikipedia.org/wiki/Wikipedia:Make_technical_articles_understandable):

> Articles should be self-contained as much as possible, rather than relying on excessive links to explain unfamiliar concepts.

> Explain technical terms and expand acronyms when they are first used.

> Check to make sure that technical terms are not used before they are defined.

Expand the room's abbreviations and handles on first use; define every term before it carries weight; make each reference resolve inside the document or to a place the reader can open. The thread, the meeting, the private channel are all closed to them.

## 8. The test: read it as the stranger

George Gopen and Judith Swan, [The Science of Scientific Writing](https://web.archive.org/web/20231222113350/https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) (American Scientist, 1990):

> It does not matter how pleased an author might be to have converted all the right data into sentences and paragraphs; it matters only whether a large majority of the reading audience accurately perceives what the author had in mind.

> When old information does not appear at all in a sentence, whether in the topic position or elsewhere, readers are left to construct the logical linkage by themselves. Often this happens when the connections are so clear in the writer's mind that they seem unnecessary to state; at those moments, writers underestimate the difficulties and ambiguities inherent in the reading process.

Hand the draft to someone who was not in the room, or read it as that person; every stall marks an unexpressed context to restore.
