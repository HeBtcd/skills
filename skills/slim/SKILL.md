---
name: slim
disable-model-invocation: true
description: "Reduce a bloated artifact or a failing repro to its essential minimum. Use when code, a feature set, or a document is over-built and the question is what can go, or when a bug reproduction needs shrinking to the smallest case that still fails."
---

# Slim

Both branches run one spine: fix the check, find what can go, clear it against the check, stop at the minimum. Seven moments, in the order the work meets them.

## 1. The oracle: what must still hold

For a failing repro, the check is that it still fails, standing alone. The [SSCCE](https://sscce.org/), Short, Self Contained, Correct (Compilable), Example:

> * Short (Small) - Minimise bandwidth for the example, do not bore the audience.
> * Self Contained - Ensure everything is included, ready to go.
> * Correct - Copy, paste, (compile,) see is the aim.
> * Example - Displays the problem we are trying to solve.

> Make sure the posted code, displays the problem!

For an over-built system, what must hold is whatever anyone actually depends on, not what the contract promised. Hyrum Wright, [Hyrum's Law](https://www.hyrumslaw.com/):

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

> Given enough use, there is no such thing as a private implementation.

Write down the check every cut must pass: the repro still displays the problem, and the behaviors anyone depends on still work.

## 2. Dead code: what nothing reaches

Wikipedia, [Dead code](https://en.wikipedia.org/wiki/Dead_code):

> Some use the term to refer to code (i.e. instructions in memory) which can never be executed at run-time. In some areas of computer programming, dead code is a section in the source code of a program which is executed but whose result is never used in any other computation.

> In large programming projects, it is sometimes difficult to recognize and eliminate dead code, particularly when entire modules become dead. Test scaffolding can make it appear that the code is still live [...]

> While the result of a dead computation may never be used, it may raise exceptions or affect some global state, thus removal of such code may change the output of the program and introduce unintended bugs.

Sweep for what cannot be reached or cannot matter: uncalled functions, unread results, branches that cannot fire, modules nothing imports.

## 3. Yagni: what nothing needs

Fowler, [Yagni](https://martinfowler.com/bliki/Yagni.html):

> Yagni originally is an acronym that stands for “You Aren't Gonna Need It”. [...] It's a statement that some capability we presume our software needs in the future should not be built now because “you aren't gonna need it”.

> The code for the presumptive feature adds some complexity to the software, this complexity makes it harder to modify and debug that software, thus increasing the cost of other features.

> [...] any abstraction that makes it harder to understand the code for current requirements is presumed guilty.

> One approach I use when mentoring developers in this situation is to ask them to imagine the refactoring they would have to do later to introduce the capability when it's needed.

For every feature, flag, or abstraction whose only user is a presumed future, imagine the change that would add it when the need arrives; the ones that would be cheap to add back can go.

## 4. Omit needless words: what adds no meaning

For the document, comment, or message branch of bloat, Strunk, [The Elements of Style](https://www.gutenberg.org/files/37134/37134-h/37134-h.htm) (1918), rule 13:

> Vigorous writing is concise. A sentence should contain no unnecessary words, a paragraph no unnecessary sentences, for the same reason that a drawing should have no unnecessary lines and a machine no unnecessary parts. This requires not that the writer make all his sentences short, or that he avoid all detail and treat his subjects only in outline, but that he make every word tell.

Cut every word, sentence, and section that adds no meaning; keep the detail that tells.

## 5. Chesterton's fence: the reason it is there

Before any candidate is cleared, Chesterton, [The Thing](https://en.wikiquote.org/wiki/G._K._Chesterton) (1929), ch. IV "The Drift From Domesticity":

> If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.

> Some person had some reason for thinking it would be a good thing for somebody. And until we know what the reason was, we really cannot judge whether the reason was reasonable.

> If he knows how it arose, and what purposes it was supposed to serve, he may really be able to say that they were bad purposes, or that they have since become bad purposes, or that they are purposes which are no longer served.

For every part you cannot explain, find the reason it was added: the commit, the ticket, the call site, the constraint. A reason found and found stale is the license to cut.

## 6. Delta debugging: cut against the check

Zeller, [The Debugging Book](https://www.debuggingbook.org/html/DeltaDebugger.html), "Reducing Failure-Inducing Inputs":

> A reducer takes a failure-inducing input and reduces it to the minimum that still reproduces the failure.

Kernighan and Pike, The Practice of Programming (1999), as quoted there:

> For every circumstance of the problem, check whether it is relevant for the problem to occur. If it is not, remove it from the problem report or the test case in question.

> Proceed by binary search. Throw away half the input and see if the output is still wrong; if not, go back to the previous state and discard the other half of the input.

> Delta Debugging implements the "binary search" strategy, as listed above, but with a twist: If neither half fails (also as above), it keeps on cutting away smaller and smaller chunks from the input, until it eliminates individual characters. Thus, after cutting away the first half, we cut away the first quarter, the second quarter, and so on.

> Its result is 1-minimal, meaning that every character contained is required to produce the error; removing any [...] no longer causes the test to fail.

> To ensure we do not remove code that actually would be necessary for normal behavior, let us add another check [...] If this one fails (say, after the code has been tampered with too much), it raises an exception – but a different one from the original failure

Take the cut in rounds against the check: remove a chunk and rerun it; hold the cut if the verdict stands, restore and try a finer chunk if it breaks, down to single elements.

## 7. Nothing left to take away

Saint-Exupéry, [Wind, Sand and Stars](https://en.wikiquote.org/wiki/Antoine_de_Saint-Exup%C3%A9ry) (1939), ch. III "The Tool", trans. Lewis Galantière:

> In anything at all, perfection is finally attained not when there is no longer anything to add, but when there is no longer anything to take away, when a body has been stripped down to its nakedness.

Stop when the next cut breaks the check: every remaining piece either makes the failure fire or serves someone who would notice.
