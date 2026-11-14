---
name: for-the-audience
disable-model-invocation: true
description: "Write up scattered discussion as a self-contained document for readers who were not in the room. Use when turning threads, notes, and review back-and-forth into a decision record, postmortem, proposal, or summary that must stand alone for outside or future readers."
---

# For the Audience

A pile of threads, notes, and review back-and-forth becomes a document a stranger can read end to end. Seven moments, in the order the work meets them.

## 1. Audience analysis: the reader was not in the room

Google, [Technical Writing One](https://developers.google.com/tech-writing/one/audience):

> good documentation = knowledge and skills your audience needs to do a task − your audience's current knowledge and skills

> In other words, make sure your document provides the information that your audience needs but doesn't already have.

> Begin by identifying your audience's **role**(s).

> Roles, by themselves, are insufficient for defining an audience. That is, you must also consider your audience's *proximity* to the knowledge. [...] experienced engineers typically know vastly more about their current project than new engineers on the same project.

> Write down a list of everything your target audience needs to learn to accomplish goals. [...] If you are writing a design spec, then your list should focus on information your target audience should learn rather than on mastering specific tasks.

> Writing to meet your audience's needs requires unselfish empathy. You must create explanations that satisfy your audience's curiosity rather than your own.

Write down the reader's role, their proximity to the matter, and the list of things this document must teach them; that list measures every candidate the pile offers.

## 2. Affinity diagram: sort the pile into themes

Wikipedia, [Affinity diagram](https://en.wikipedia.org/wiki/Affinity_diagram):

> The **affinity diagram** is a business tool used to organize ideas and data. [...] the term affinity diagram was devised by Jiro Kawakita in the 1960s and is sometimes referred to as the **KJ Method**.

> It is also frequently used in contextual inquiry as a way to organize notes and insights from field interviews. It can also be used for organizing other freeform comments, such as open-ended survey responses, support call logs, or other qualitative data.

> The affinity diagram organizes ideas with following steps:
> 1. Record each idea on cards or notes.
> 2. Look for ideas that seem to be related.
> 3. Sort cards into groups until all cards have been used.

> The process requires becoming deeply immersed in the data, which has benefits beyond the tangible deliverables.

Give every claim, question, decision, and objection in the pile its own card, and sort until the clusters name the document's sections.

## 3. Inverted pyramid: the answer heads the page

Journalists write for readers who were not at the event. Wikipedia, [Inverted pyramid (journalism)](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)):

> The **inverted pyramid** is a metaphor used by journalists and other writers to illustrate how information should be prioritised and structured in prose [...] It is a way to communicate the basics about a topic in the initial sentences.

> The widest part at the top represents the most substantial, interesting, and important information that the writer means to convey, illustrating that this kind of material should head the article, while the tapering lower portion illustrates that other material should follow in order of diminishing importance.

> It is sometimes called a **summary news lead** style, or **bottom line up front** ([BLUF](https://en.wikipedia.org/wiki/BLUF_(communication))). The opposite, the failure to mention the most important, interesting or attention-grabbing elements of a story in the opening paragraphs, is called burying the lead.

> This system also means that information less vital to the reader's understanding comes later in the story, where it is easier to edit out for space or other reasons.

Open the document with the point the pile reached, and let every later section matter less than the one before it.

## 4. Make things easy for your readers: the page supplies the room

Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/you-are-what-you-write.html):

> *Make things easy for your readers.* There's a ton of information floating around in any active open source project, and readers cannot be expected to be familiar with most of it—indeed, they cannot always be expected to know how to become familiar. Wherever possible, your posts should provide information in the form most convenient for readers.

> If you have to spend an extra two minutes to dig up the URL to a particular thread in the mailing list archives, in order to save your readers the trouble of doing so, it's worth it. If you have to spend an extra 5 or 10 minutes summarizing the conclusions so far of a complex thread, in order to give people context in which to understand your post, then do so.

> [...] when there is a choice between *N* people making an effort and one person doing so, the project prefers the latter.

> *Construct the Subject lines of new mails carefully.* The Subject line is the most important line in your mail, because it allows each other person in the project to decide whether or not to read more.

Fogel again, on [the archives](https://producingoss.com/en/growth.html):

> If a project's formal guidelines are its statutory law, the archives are its common law: a record of all decisions made and how they were arrived at.

> [...] you should include pointers to them when you re-raise the topic, so people can see for themselves a) that they went nowhere, and b) that you did your homework, and therefore are probably saying something now that has not been said before.

Put what the reader needs on the page in its most convenient form, link the threads the page stands on, and title it so a stranger can tell whether to read on.

## 5. Architecture decision record: what the argument settled

Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):

> One of the hardest things to track during the life of a project is the motivation behind certain decisions. A new person coming on to a project may be perplexed, baffled, delighted, or infuriated by some past decision.

> Without understanding the rationale or consequences, this person has only two choices: **Blindly accept the decision.** [...] **Blindly change it.** [...] It's better to avoid either blind acceptance or blind reversal.

> Each record describes a set of forces and a single decision in response to those forces.

> **Context** This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.

> **Decision** This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …"

> **Status** A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its replacement.

> **Consequences** This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones.

> The whole document should be one or two pages long. We will write each ADR as if it is a conversation with a future developer.

Turn each argument the pile settled into a record of its forces, its "we will" decision, its status, and all of its consequences; mark what the pile left open as proposed.

## 6. Curse of knowledge: hunt the room's shorthand

Wikipedia, [Curse of knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge):

> The **curse of knowledge**, also called the **curse of expertise** or **expert's curse**, is a cognitive bias that occurs when a person who has specialized knowledge assumes that others share in that knowledge.

> [...] a knowledgeable person cannot accurately reconstruct what a person, be it themselves or someone else, without the knowledge would think, or how they would act.

> The curse of knowledge is a difficult bias to correct. For instance, the cognitive bias does not reduce when you tell people about it or ask them to think more about the other's perspective. Financial incentives were equally ineffective in reducing the bias.

Read the draft listing every name, term, and referent the pile defined but the page does not, and give each a definition or a link at first use.

## 7. Cognitive walkthrough: try it on someone who was not there

Wikipedia, [Cognitive walkthrough](https://en.wikipedia.org/wiki/Cognitive_walkthrough):

> The **cognitive walkthrough** method is a usability inspection method used to identify usability issues in interactive systems, focusing on how easy it is for new users to accomplish tasks with the system.

> A cognitive walkthrough starts with a task analysis that specifies the sequence of steps or actions required by a user to accomplish a task, and the system responses to those actions. The designers and developers of the software then walk through the steps as a group, asking themselves a set of questions at each step.

> * **Will the user try to achieve the effect that the subtask has?**
> * **Will the user notice that the correct action is available?**
> * **Will the user understand that the wanted subtask can be achieved by the action?**
> * **Does the user get appropriate feedback?**

> The walkthrough method does not test real users on the system. The walkthrough will often identify many more problems than you would find with a single, unique user in a single test session

Run the walkthrough with a reader who never saw the pile: hand them the draft, record where they stall, and repair the page at those points.
