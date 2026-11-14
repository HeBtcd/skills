---
name: when-in-rome
disable-model-invocation: true
description: "Match an established codebase's own conventions when adding code to it. Use when about to write or change code in a project that already has its way of doing things: read the code around the change, let local precedent outrank general style rules, trace odd conventions to their reasons, run the project's own tools, and package each logical change on its own."
---

# When in Rome

A change to an established codebase is a visit: the place's ways answer before your preferences do. Seven moments, in the order the work meets them.

## 1. When in Rome

Ambrose's advice to a newcomer, reported by Augustine, [Letter 54](https://www.newadvent.org/fathers/1102054.htm) (A.D. 400), chapter 2:

> [...] there is no better rule for the wise and serious Christian in this matter, than to conform to the practice which he finds prevailing in the Church to which it may be his lot to come. For such a custom, if it is clearly not contrary to the faith nor to sound morality, is to be held as a thing indifferent, and ought to be observed for the sake of fellowship with those among whom we live.

> When I visit Rome, I fast on Saturday; when I am here, I do not fast. On the same principle, do you observe the custom prevailing in whatever Church you come to, if you desire neither to give offense by your conduct, nor to find cause of offense in another's.

The failure mode, Augustine's diagnosis in the same chapter:

> [...] raise questions, it may be, from some crotchet of their own, or from attachment to the custom followed in one's own country, or from preference for that which one has seen abroad, supposing that wisdom is increased in proportion to the distance to which men travel from home, and agitate these questions with such keenness, that they think all is wrong except what they do themselves.

Let the custom prevailing in this codebase govern your change; the ways you saw abroad stay abroad.

## 2. The golden rule

LLVM, [Coding Standards](https://llvm.org/docs/CodingStandards.html), Introduction:

> While this document may provide guidance for some mechanical formatting issues, whitespace, or other “microscopic details”, these are not fixed standards. Always follow the golden rule:
>
> **If you are extending, enhancing, or bug fixing already implemented code, use the style that is already being used so that the source is uniform and easy to follow.**

> There are some conventions that are not uniformly followed in the code base [...] This is because they are relatively new, and a lot of code was written before they were put in place.

Before writing a line, read the code your change will sit among; imitate its names, its factoring, its error handling, its libraries.

## 3. A foolish consistency

Python's [PEP 8](https://peps.python.org/pep-0008/), Style Guide for Python Code:

> One of Guido’s key insights is that code is read much more often than it is written.

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

> Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.

> However, know when to be inconsistent – sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don’t hesitate to ask!

> In particular: do not break backwards compatibility just to comply with this PEP!

> Some other good reasons to ignore a particular guideline: [...] To be consistent with surrounding code that also breaks it (maybe for historic reasons) – although this is also an opportunity to clean up someone else’s mess (in true XP style).

Where a general rule and this place's practice disagree, follow the place: its own guide over general guides, its surrounding code over both, its compatibility promises over all.

## 4. Chesterton's fence

G. K. Chesterton, [The Thing](https://en.wikiquote.org/wiki/G._K._Chesterton#The_Thing_(1929)) (1929), ch. IV "The Drift From Domesticity":

> If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.

> Some person had some reason for thinking it would be a good thing for somebody. And until we know what the reason was, we really cannot judge whether the reason was reasonable.

> It is extremely probable that we have overlooked some whole aspect of the question, if something set up by human beings like ourselves seems to be entirely meaningless and mysterious.

Before changing or removing a convention you cannot explain, find the reason it exists: git blame, history, comments, docs, the people who wrote it.

## 5. Rule of three

"Three strikes and you refactor," attributed to Don Roberts and popularised by Martin Fowler's Refactoring (Wikipedia, [Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))):

> [...] two instances of similar code do not require refactoring, but when similar code is used three times, it should be extracted into a new procedure.

> Attempting premature refactoring risks selecting a wrong abstraction, which can result in worse code as new requirements emerge and will eventually need to be refactored again.

Imitate the duplication the codebase already carries; let the codebase's own third instance, not your preference, mark when extraction is earned.

## 6. Gofmt's style

Rob Pike, [Go Proverbs](https://go-proverbs.github.io/):

> Gofmt's style is no one's favorite, yet gofmt is everyone's favorite.

Run the project's own formatter, linters, and checks; where a tool owns the question, its answer is the house style.

## 7. Separate your changes

Linux kernel documentation, [Submitting patches](https://www.kernel.org/doc/html/latest/process/submitting-patches.html):

> Separate each **logical change** into a separate patch.

> The point to remember is that each patch should make an easily understood change that can be verified by reviewers. Each patch should be justifiable on its own merits.

> [...] when moving code from one file to another [...] you should not modify the moved code at all in the same patch which moves it. This clearly delineates the act of moving the code and your changes.

> Describe your changes in imperative mood, e.g. “make xyzzy do frotz” instead of “[This patch] makes xyzzy do frotz” or “[I] changed xyzzy to do frotz”, as if you are giving orders to the codebase to change its behaviour.

Give each logical change its own commit, each justifiable on its own merits; let moves and cleanups travel separately, and match the message to the voice of the project's log.
