---
name: deep-research
disable-model-invocation: true
description: "Research a decision against field evidence: postmortems, incident reports, and real-world failure cases. Use when the question is what actually happens in production and standard recommendations or generic summaries fail to settle an important decision. Not for naming lookups or codebase questions."
---

# Deep Research

Six moves for finding decision-relevant evidence in the field's own record (reports and failure cases where generic summaries fall short) in the order the work meets them.

## 1. The question: the anatomy evidence can answer

Name the decision first, then build the question so the record can answer it: the [PICO process](https://en.wikipedia.org/wiki/PICO_process), evidence-based practice's question anatomy from Richardson (1995):

> a mnemonic used in evidence-based practice [...] to frame and answer a clinical or health care related question, though it is also argued that PICO "can be used universally for every scientific endeavour in any discipline with all study designs". [...] The PICO framework is also used to develop literature search strategies [...]

> * **P** – Patient, problem, or population
> * **I** – Intervention
> * **C** – Comparison, control, or comparator
> * **O** – Outcome(s) [...]

Map the anatomy to the decision: the population is systems shaped like yours, the intervention is the practice under consideration, the comparison is its live alternative, and the outcome is what happened: the incidents, costs, and failure modes that would flip the decision.

## 2. The corpus: hunt the grey literature

Field evidence lives where publishing is not the producer's business. The National Library of Medicine's [Grey Literature](https://www.ncbi.nlm.nih.gov/sites/books/NBK518722/) guidelines, on the Luxembourg Convention:

> that which is produced on all levels of government, academics, business and industry in print and electronic formats, but which is not controlled by commercial publishers

> This category broadly includes reports, theses and dissertations, conference proceedings, standards, technical documentation, datasets, preprints, web content, and government documents.

Hunt the production instances: postmortems and incident repositories, conference talks and transcripts, issue trackers and mailing lists, technical reports and white papers.

## 3. The hunt: let each find rewrite the query

Real searches evolve. Marcia Bates, [The Design of Browsing and Berrypicking Techniques for the Online Search Interface](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html) (1989):

> In real-life searches in manual sources, end users may begin with just one feature of a broader topic, or just one relevant reference, and move through a variety of sources. Each new piece of information they encounter gives them new ideas and directions to follow and, consequently, a new conception of the query. At each stage they are not just modifying the search terms used in order to get a better match for a single query. Rather the query itself (as well as the search terms used) is continually shifting, in part or whole. This type of search is here called an evolving search.

> [...] the query is satisfied not by a single final retrieved set, but by a series of selections of individual references and bits of information at each stage of the ever-modifying search. A bit-at-a-time retrieval of this sort is here called berrypicking.

Six moves, chosen by the lead the last find produced:

> **Footnote chasing** (or "backward chaining") [...] following up footnotes found in books and articles of interest, and therefore moving backward in successive leaps through reference lists.

> **Citation searching** (or "forward chaining"). One begins with a citation, finds out who cites it by looking it up in a citation index, and thus leaps forward.

> **Journal run**. Once, by whatever means, one identifies a central journal in an area, one then locates the run of volumes of the journal and searches straight through relevant volume years.

> **Area scanning**. Browsing the materials that are physically collocated with materials located earlier in a search is a widely used and effective technique.

> **Subject searches in bibliographies and abstracting and indexing (A & I) services**. Many bibliographies and most A & I services are arranged by subject.

> **Author searching.** [...] uses an author name to see if the author has done any other work on the same topic

> It is part of the nature of berrypicking that people adapt the strategy to the particular need at the moment; as the need shifts in part or whole, the strategy often shifts as well [...]

## 4. The source: leave the site to read it

Each find is a stranger until vetted. Sam Wineburg, [To navigate the dangers of the web, you need critical thinking - but also critical ignoring](https://theconversation.com/to-navigate-the-dangers-of-the-web-you-need-critical-thinking-but-also-critical-ignoring-158617), The Conversation:

> She evaluated the site by leaving it. Fact checkers engage in what we call lateral reading, opening up new tabs across the top of their screens to search for information about an organization or individual before diving into a site's contents.

> Only after consulting the open web do they gauge whether expending attention is worth it.

> By dwelling on an unfamiliar site, imagining ourselves smart enough to outsmart it, we squander attention and cede control to the site's designers.

Vet who produced the report (the organization's funding and history, the author's seat) by what the rest of the web says about them, before the contents earn your time.

## 5. The incident: ask how

A failure report is a narrative of conditions, not a verdict on a person. John Allspaw, [The infinite hows](https://www.oreilly.com/radar/the-infinite-hows/), O'Reilly Radar:

> In order to learn (which should be the goal of any retrospective or post-hoc investigation) you want multiple and diverse perspectives. You get these by asking people for their own narratives. Effectively, you're asking "how?"

> Asking "how?" gets you to describe (at least some) of the conditions that allowed an event to take place, and provides rich operational data.

> When it comes to decisions and actions, we want to know how it made sense for someone to do what they did. And make no mistake: they thought what they were doing made sense. Otherwise, they wouldn't have done it.

> Human error becomes a starting point, not a conclusion. (Dekker, 2009)

Mine each report for the conditions (the defaults, deadlines, dashboards, and pressures that made the failing action sensible) because those are the conditions your decision will run under.

## 6. The verdict: count the silent cases, then take the outside view

The record shows the cases that produced a report. Wikipedia, [Survivorship bias](https://en.wikipedia.org/wiki/Survivorship_bias):

> Survivorship bias or survivor bias is a statistical error which results from concentrating on entities that passed a selection process over those that did not. This can lead to incorrect conclusions because of incomplete data.

> During World War II, the statistician Abraham Wald described methods of estimating the vulnerability of various parts of an aircraft based on damage to surviving planes. [...] Given that there was only data from surviving aircraft, this work directly addresses the issue of survivorship bias.

> the advice business is a monopoly run by survivors. When something becomes a non-survivor, it is either completely eliminated, or whatever voice it has is muted to zero (David McRaney)

> [...] Nassim Taleb called the data obscured by survivorship bias "silent evidence".

Name the silent evidence (the deployments that failed quietly and shipped no postmortem, the successes nobody wrote up) and discount the record accordingly.

Then let the found cases outvote the plan. Kahneman and Tversky's method, Wikipedia, [Reference class forecasting](https://en.wikipedia.org/wiki/Reference_class_forecasting):

> Reference class forecasting is so named as it predicts the outcome of a planned action based on actual outcomes in a reference class of similar actions to that being forecast.

> People tend to underestimate the costs, completion times, and risks of planned actions, whereas they tend to overestimate the benefits of those same actions. Such error is caused by actors taking an "inside view", where focus is on the constituents of the specific planned action instead of on the actual outcomes of similar ventures that have already been completed.

> Reference class forecasting for a specific project involves the following three steps:
> 1. Identify a reference class of past, similar projects.
> 2. Establish a probability distribution for the selected reference class for the parameter that is being forecast.
> 3. Compare the specific project with the reference class distribution, in order to establish the most likely outcome for the specific project.

Return the verdict on the decision's terms: the modal outcome in the found reference class, the failure modes that recur across independent reports, and the silent cases the record cannot show.
