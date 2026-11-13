---
name: slim
disable-model-invocation: true
description: "Slim an artifact from the design down: cut the parts that never earned or never ran, undo a wrong decomposition, or grow a smaller replacement at the edges of the old. Use when something is bloated or over-built and the question is what can go, or when a failing repro needs shrinking to its minimum. Parts and structure, not prose."
---

# Slim

Slimming is removal at design grain: the unit of work is a named part, not a sentence. Eight moves, in the order the work meets them.

## 1. Floor: which complexity can go

Frederick P. Brooks, [No Silver Bullet](https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html) (1987):

> Following Aristotle, I divide them into essence, the difficulties inherent in the nature of software, and accidents, those difficulties that today attend its production but are not inherent.

> The complexity of software is an essential property, not an accidental one. Hence, descriptions of a software entity that abstract away its complexity often abstract away its essence.

Find the accidents; the essence is the floor.

## 2. Reason: what the part was for

G. K. Chesterton, [The Thing](https://catholiclibrary.org/library/view?docId=/Contemporary-EN/XCT.165.html&chunk.id=00000011) (1929), "The Drift from Domesticity":

> If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.

> If he knows how it arose, and what purposes it was supposed to serve, he may really be able to say that they were bad purposes, or that they have since become bad purposes, or that they are purposes which are no longer served.

Explain the part before the cut; "purposes which are no longer served" is the removal test.

## 3. Pin: the artifact is its own specification

Michael Feathers, [Characterization Testing](https://michaelfeathers.silvrback.com/characterization-testing):

> When a system goes into production, in a way, it becomes its own specification. We need to know when we are changing existing behavior regardless of whether we think it's right or not.

> The purpose of characterization testing is to document your system's actual behavior, not check for the behavior you wish your system had.

> When we write characterization tests we build up our knowledge of what the code actually does. This is particularly useful when we want to refactor or rewrite. We can run our tests and find out immediately whether we've changed behavior.

Pin before the first cut.

## 4. Shares: the parts that can go

Three tests for a removable part: never needed, never run, never earning. Fowler and Beck, [Bad Smells in Code](https://www.informit.com/articles/article.aspx?p=2952392), Refactoring (2nd ed.):

> You get it when people say, "Oh, I think we'll need the ability to do this kind of thing someday" and thus add all sorts of hooks and special cases to handle things that aren't required. [...] If all this machinery were being used, it would be worth it. But if it isn't, it isn't. The machinery just gets in the way, so get rid of it.

> Speculative generality can be spotted when the only users of a function or class are test cases. If you find such an animal, delete the test case and apply Remove Dead Code (237).

> We like using program elements to add structure [...] But sometimes the structure isn't needed. It may be a function that's named the same as its body code reads, or a class that is essentially one simple function. [...] Either way, such program elements need to die with dignity.

## 5. Undo: the fastest way forward is back

Sandi Metz, [The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction):

> duplication is far cheaper than the wrong abstraction

> If you find yourself passing parameters and adding conditional paths through shared code, the abstraction is incorrect.

> When dealing with the wrong abstraction, the fastest way forward is back. Do the following:
>
> 1. Re-introduce duplication by inlining the abstracted code back into every caller.
> 2. Within each caller, use the parameters being passed to determine the subset of the inlined code that this specific caller executes.
> 3. Delete the bits that aren't needed for this particular caller.

> This removes both the abstraction and the conditionals, and reduces each caller to only the code it needs. [...] Once an abstraction is proved wrong the best strategy is to re-introduce duplication and let it show you what's right.

## 6. Recut: one hidden decision per part

D. L. Parnas, [On the Criteria To Be Used in Decomposing Systems into Modules](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html) (1972):

> The effectiveness of a "modularization" is dependent upon the criteria used in dividing the system into modules.

> We propose instead that one begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others.

> Every module in the second decomposition is characterized by its knowledge of a design decision which it hides from all others. Its interface or definition was chosen to reveal as little as possible about its inner workings.

## 7. Strangle: grow the small at the edges of the old

When no cut saves it, replace. Martin Fowler, [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html):

> Replacements seem easy to specify, but often it's hard to figure out the details of existing behavior. What's worse, much of that behavior is stuff that isn't really wanted, so building it is a waste.

> The alternative that my colleagues and I prefer, is to do a gradual process of modernization. Like the fig, it begins with small additions, often new features, that are built on top of, yet separate to the legacy code base. As we do this we move bits of behavior from the legacy system into the new code base.

> Once we have seams to isolate a few components, we can start replacing them.

## 8. Minimum: a failing repro at its smallest

When the artifact itself is a failing repro. Zeller et al., [Reducing Failure-Inducing Inputs](https://www.debuggingbook.org/html/DeltaDebugger.html), The Debugging Book:

> A standard problem in debugging is this: Your program fails after processing some large input. Only a part of this input, however, is responsible for the failure. Reducing the input to a failure-inducing minimum not only eases debugging – it also helps in understanding why and when the program fails.

> A reducer takes a failure-inducing input and reduces it to the minimum that still reproduces the failure.

Kernighan and Pike's manual version, quoted in the chapter:

> For every circumstance of the problem, check whether it is relevant for the problem to occur. If it is not, remove it from the problem report or the test case in question.
