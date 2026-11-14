---
name: hebtcd-skill-creator
disable-model-invocation: true
description: "Compose a Skill as an ordered basis of Things behind a trigger pointer. Use when deciding whether a capability, a recurring move, or a named concept deserves a Skill of its own, or when an existing Skill's basis needs re-cutting."
---

# Hebtcd Skill Creator

A Skill is a pointer in front of an ordered basis of Things. Six moments, in the order the work meets them.

## 1. Whether: is there a Thing here, and is it one Skill?

Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/getting-started.html):

> Always look around to see if there's an existing project that does what you want.

> Even if you don't find exactly what you were looking for, you might find something so close that it makes more sense to join that project and add functionality to it than to start from scratch yourself.

Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/), Anthropic:

> A skill that restates what Claude would do by default adds context without adding value.

> After cataloging all of our internal skills at Anthropic, we noticed they cluster into nine categories. The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent.

Anthropic's [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills):

> Identify specific gaps in your agents’ capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

The struggle marks where to dig; what the dig unearths is a Thing: a method or concept with an established name and a checkable source. Checkable means anyone can fetch and diff it: a private file, a local transcript, a session log is not a source. Keep the established name for `grep`; where none exists, write the behavior in plain words.

## 2. Pointer: the promise the trigger matches

Anthropic's [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview):

> Claude loads this metadata at startup and includes it in the system prompt. The `description` is what Claude matches your request against when determining whether to trigger the Skill, so it must say both what the Skill does and when to use it. This lightweight approach means you can install many Skills without context penalty: until a Skill is triggered, only its name and description occupy context.

Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/), Anthropic:

> This listing is what Claude scans to decide “is there a skill for this request?” Which means the description field is not a summary, it’s a description of when to trigger this skill.

> It’s helpful to include triggers for the skill, like “babysit,” in its description.

Matt Pocock, [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md):

> A **context pointer** is a reference held in the agent's context that names some out-of-context material and encodes the condition for reaching it. A skill's description is one; a line in `AGENTS.md` naming a doc is the same object. The pointer's _wording_, not its target, decides when the agent reaches the material, and how reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

> A pointer does two jobs: state what the material is, and list the **branches** that should trigger reaching it (a branch is a distinct case the document handles, so different runs take different paths through it). Every word of an always-loaded pointer costs on every turn, so it earns even harder pruning than the body:
>
> - **Front-load the leading word**: the pointer is where it does its triggering work.
> - **One trigger per branch.** Synonyms that rename a single branch are one branch written twice; collapse them and keep only genuinely distinct branches.
> - **Cut identity the body already carries.**

The description names the moment the Skill answers. Every clause in it names a branch some Thing owns; an exclusion clause names a moment nothing here owns. Write the boundary positively or cut it.

Fogel's name rules (Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/getting-started.html)):

> Gives some idea what the project does, or at least is related in an obvious way, such that if one knows the name and knows what the project does, the name will come quickly to mind thereafter.

> Is not the same as some other project's name [...] You don't want to create identity confusion.

Claude Code docs, [Skills](https://code.claude.com/docs/en/skills), on who fires it:

> **`disable-model-invocation: true`**: Claude can't invoke the skill on its own. Use this for workflows with side effects or that you want to control timing, like `/commit`, `/deploy`, or `/send-slack-message`. You don't want Claude deciding to deploy because your code looks ready.

Under `disable-model-invocation`, the description's reader is the human or router deciding when to reach for it; the pointer rules are unchanged.

Compose the description after the basis stands: it reports what the basis can do. A clause promising a moment the work never reaches is cut from the pointer before any Thing is imported to cover it.

## 3. Basis: the Things span the promise, once each

Wikipedia, [Basis (linear algebra)](https://en.wikipedia.org/wiki/Basis_(linear_algebra)):

> a set B is a basis if its elements are linearly independent and every element of V is a linear combination of elements of B. In other words, a basis is a linearly independent spanning set.

> A generating set S is a basis of V if and only if it is minimal, that is, no proper subset of S is also a generating set of V.

> It is often convenient or even necessary to have an ordering on the basis vectors [...] one speaks of an **ordered basis**.

V is the territory the pointer's promise states; the when-branches are its entries, and a promised branch no Thing owns is a hole. The moments inside V are the dimensions; each Thing is one vector owning one moment; the same source under two headings is one vector duplicated, or two moments that are one. Vectors order by the moment the work meets them; excerpts inside a vector, same rule.

A moment is a decision point inside the act's own pipeline: not a precondition, a resource rule, or a general duty the reader owes everywhere. A vector's legitimacy comes from the work's own decomposition; name the moment it owns without citing the description. When the pointer names several branches, their moments order onto one spine; a branch whose moments cannot join the spine is a different Skill, not a tail to bolt on.

Aquinas's razor (SEP, [Simplicity](https://plato.stanford.edu/entries/simplicity/)):

> If a thing can be done adequately by means of one, it is superfluous to do it by means of several; for we observe that nature does not employ two instruments where one suffices

Removing a vector asks what it was doing first: [Chesterton's fence](https://en.wikiquote.org/wiki/G._K._Chesterton#The_Thing_%281929%29), G. K. Chesterton, The Thing (1929), ch. IV "The Drift From Domesticity":

> If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.

> Some person had some reason for thinking it would be a good thing for somebody. And until we know what the reason was, we really cannot judge whether the reason was reasonable.

## 4. Wording: tasks in the Things' own words

The body is compiled from verbatim excerpts of the Things, not paraphrase: a sentence or word drawn from no excerpt is cut. Seam words are permitted only where deleting them wrecks the excerpt's sense:

- **Block quote (`>`)** verbatim when the original wording carries the rule, marking omissions with `[...]`. Put the link in the lead-in; consecutive quotes from the same source inherit it.
- **Locator link** on the concept words (`[Bates's berrypicking](url)`) or a compact end-of-sentence parenthetical (`(Author, [Title](url), section/year)`) when only the mechanism matters; weave the citation into the sentence: author as plain text, link on the title, never a whole-citation link blob; use last names for academics, org names for standards, and full names for podcast guests (`Guest, [Lex Fridman Podcast #NNN](url)`).

Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/), Anthropic:

> Claude will generally try to stick to your instructions, and because skills are so reusable you’ll want to be careful of being too specific in your instructions. Give Claude the information it needs, but give it the flexibility to adapt to the situation.

> State the goal and the constraints, not every step.

The razor again, one level down: an instruction that decides nothing is an instrument too many. David Heinemeier Hansson relaying Claude Code's Boris, [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2-transcript/), 0:56:

> One of the things that Boris, working on Claude Code, shared in an interview recently about Opus 5 was that the system prompt that they ship for Opus 5, and presumably also Fable, shrunk by 80% because the agent not only needed far less human instruction, it was actually being damaged by overly prescriptive humans.

Matt Pocock, [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md):

> **Negation** is the failure mode beside this lever: steering by prohibition drags the forbidden behaviour into context and makes it _more_ available, not less. _Don't think of an elephant_, and the elephant is all there is; the negation is a weak modifier the strongly-activated concept overruns, so the ban half-reads as an instruction to do the thing. Prompt the **positive**: state the target behaviour ("write one-line comments") so the banned one is never spoken. A prohibition earns its place only as a hard guardrail you cannot phrase positively; even then, pair it with the positive target so attention lands on what to do.

> an instruction the model already obeys by default pays load to say nothing. The test (does it change behaviour versus the default?) is model-relative, not reader-relative: [...] When a sentence fails, delete the whole sentence rather than trim words from it.

> A **leading word** is a compact concept already living in the model's pretraining that the agent thinks with while running the document (_lesson_, _fog of war_, _tracer bullets_). Repeated as a token, never as a sentence, it accumulates a distributed definition and anchors a whole region of behaviour in the fewest tokens, by recruiting priors the model already holds. Coining your own works if you define it clearly, but a made-up word recruits no priors: you pay in definition tokens what a pretrained word gives free; reach for an existing word first.

> Assume every document is carrying restatements that leading words retire. Go find them.

The pointer's front-loaded word and the body's leading word are different levers that share a name.

Every line states a task: an observable action or a checkable failure, reversed onto its real target: the reader performs it, not the source's original audience; "find the implicit state machine" puts attention where the problem lives. Seams and the pointer phrase positively; a prohibition inside an excerpt stands on its source's authority, and an excerpt that changes nothing the reader does is cut, verbatim or not. A heading names the moment its Things own: established name where one exists. Describe the behavior itself in place of another skill's name, so the folder works copied alone.

## 5. Shape: each piece on its rung

Matt Pocock, [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md):

> A document is built from two content types: **steps** (the ordered actions the agent performs) and **reference** (definitions, rules, facts consulted on demand). The two mix freely [...] The core decision is where each piece sits on the **information hierarchy**, a ladder ranked by how immediately the agent needs the material: [...]

> **Context load** is the cost of always-loaded material on the agent's window [...] **Cognitive load** is the cost on the human: which documents exist and when to reach for each. The human is the index. Not a cost to minimise: it is the price of human agency; spend it where human judgement matters, remove it where it does not.

> Push too little down and the top bloats; push too much and you hide material the agent actually needs. That tension is the whole decision.

> Branching is the cleanest disclosure test: inline what every branch needs, and push behind a pointer what only some branches reach.

> **Sprawl** is the failure mode here: a document simply too long, even when every line is live and unique. Attention thins across the excess, and every extra line is one more to keep relevant.

> Keep each meaning in a **single source of truth**: one authoritative place, so changing the behaviour is a one-place edit. **Duplication** (the same meaning in more than one place) costs maintenance and tokens, and inflates a meaning's prominence on the ladder past its real rank.

That rule binds inside the folder. The same Thing quoted in a sibling Skill is overlap, not duplication: each folder carries its own basis so it works copied alone.

Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/), Anthropic:

> Tell Claude what files are in your skill, and it will read them at appropriate times. [...] The simplest form of progressive disclosure is to point to other markdown files for Claude to use.

Anthropic's [Equipping agents](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills):

> When the `SKILL.md` file becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage.

## 6. Test: run it, then falsify it

Anthropic, [Equipping agents](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills):

> Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts.

> As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong.

Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/), Anthropic:

> To understand how a skill is doing, we use a PreToolUse hook that lets us log skill usage within the company [...]. This means we can find skills that are popular or are undertriggering compared to our expectations.

Amanda Askell on prompt engineering, [Lex Fridman Podcast #452](https://lexfridman.com/dario-amodei-transcript/), chapters Talking to Claude and Prompt engineering:

> [...] I try and almost see myself from the position of the model and be like, what is the exact case that I would misunderstand or where I would just be like, I don’t know what to do in this case. And then I give that case to the model and I see how it responds. And if I think I got it wrong, I add more instructions or I even add that in as an example.

> [...] try to have empathy for the model. Read what you wrote as if you were a kind of person just encountering this for the first time, how does it look to you and what would’ve made you behave in the way that the model behaved?

> What could I have said that would make you not make that error? Write that out as an instruction, and I’m going to give it to model and I’m going to try it.

The case that catches a failure lands on the moment that failed as an example under it, or earns a new vector when no moment owns it. A challenge to a vector's legitimacy re-derives that slot from the work; post-hoc justification of an existing vector is the failure the challenge exists to catch. When information would fundamentally change the execution outcome (a Skill's survival, a mechanism's owner, a verdict mid-audit), stop and ask the user.

On any change to the basis: update `name` when the trigger shifted, every index the collection keeps (each index entry carrying the description's trigger wording), and every `grep` match; run the collection's validator when it ships one; then fetch each linked source and diff every block quote in `SKILL.md` against the original; where upstream has drifted, the quote follows the original.
