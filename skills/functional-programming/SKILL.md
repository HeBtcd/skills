---
name: functional-programming
disable-model-invocation: true
description: "Functional design: model the domain in types, keep state essential, parse at the boundary, push side effects to the edges, refactor by substitution, write laws as properties, and convict idioms that hurt by design. Use when modeling a domain, untangling state and branching, deciding where side effects live, refactoring toward correctness, or judging whether an FP idiom earns its ceremony."
---

# Functional Programming

Seven moments, in the order the work meets them.

## 1. Model: which states can exist?

Scott Wlaschin, [Designing with types: Making illegal states unrepresentable](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) (the phrase is Yaron Minsky's):

> If we think about the business rule carefully, we realize that there are three possibilities: [...] Once it is put like this, the solution becomes obvious – use a union type with a case for each possibility.

> All three cases are explicitly represented, and the fourth possible case (with no email or postal address at all) is not allowed.

> First, the business logic *is* complicated. There is no easy way to avoid it. If your code is not this complicated, you are not handling all the cases properly.

> [...] if the logic is represented by a type, any changes to the business rules will immediately create breaking changes, which is a generally a good thing.

List the states the domain permits; give each a case in the type, and leave no case for the illegal ones.

## 2. Untangle: which state is essential?

Ben Moseley and Peter Marks, [Out of the Tar Pit](https://curtclifton.net/papers/MoseleyMarks06a.pdf) (2006):

> We believe that the major contributor to this complexity in many systems is the handling of state and the burden that this adds when trying to analyse and reason about the system.

> If the procedure in question (which is itself stateless) makes use of any other procedure which is stateful — even indirectly — then all bets are off, our procedure becomes contaminated and we can only understand it in the context of state.

> Our recommendations for dealing with complexity (as exemplified by both state and control) can be summed up as:
>
> • Avoid
> • Separate
>
> Specifically the overriding aim must be to avoid state and control where they are not absolutely and truly essential. [...] — whatever the language being used — there are large benefits to be had from avoiding hidden, implicit, mutable state.

Derived data is accidental state:

> Data of this kind can always be re-derived (from the input data — i.e. from the essential state) whenever required. As a result we do not need to store it in the ideal world (we just re-derive it when it is required) and it is clearly accidental state.

Find every piece of mutable state the system keeps; keep what the user supplies (essential), re-derive what the system computes (accidental).

## 3. Parse: which checks live at the boundary?

Alexis King, [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/):

> [...] a parser is just a function that consumes less-structured input and produces more-structured output.

> [...] they allow discharging checks on input up-front, right on the boundary between a program and the outside world, and once those checks have been performed, they never need to be checked again!

Momot, Bratus, Hallberg and Patterson name the failure mode in [The Seven Turrets of Babel: A Taxonomy of LangSec Errors and How to Expunge Them](http://langsec.org/papers/langsec-cwes-secdev2016.pdf) (2016):

> Shotgun parsing is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing code—throwing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the "bad" cases.

King again:

> The problem is that validation-based approaches make it extremely difficult or impossible to determine if everything was actually validated up front or if some of those so-called "impossible" cases might actually happen.

> Parsing avoids this problem by stratifying the program into two phases—parsing and execution—where failure due to invalid input can only happen in the first phase.

> **Push the burden of proof upward as far as possible, but no further.** Get your data into the most precise representation you need as quickly as you can. Ideally, this should happen at the boundary of your system, before *any* of the data is acted upon.

> [...] write functions on the data representation you *wish* you had, not the data representation you are given.

Find the shotgun parsing; replace checks that return nothing with parses that return refined data.

## 4. Isolate: where do effects live?

Gary Bernhardt's "Functional Core, Imperative Shell": [Boundaries](https://www.destroyallsoftware.com/talks/boundaries) (SCNA 2012), [transcript](https://gist.github.com/cabe56/4f3f4385fc857374cc1ef97b363b7d60):

> [...] an imperative shell which surrounds the functional core [...] the functional core is the bulk of the application it has all the intelligence and the imperative shell is sort of a glue layer between the functional pieces of the system and the nasty external world of disks and networks and other things that fail and are slow

> the expired users class makes all the decisions and the sweeper class has all the dependencies [...] the functional core is heavy on paths heavy on decisions light on dependencies which is exactly what unit testing is good at [...] and exactly the same thing is true for the shell lots of dependencies few paths is exactly what an integration test is good at it

Mark Seemann, [Functional architecture is Ports and Adapters](https://blog.ploeh.dk/2016/03/18/functional-architecture-is-ports-and-adapters/):

> In Haskell programming, you should strive towards maximising the amount of pure functions you write, pushing the impure code to the edges of the system. A good Haskell program has a big core of pure functions, and a shell of `IO` code.

> It basically means that Haskell's type system *enforces* the Ports and Adapters architecture. The *ports* are all your `IO` code. The application's core is all your pure functions.

Push every effect to the edges; let the core decide and the shell do.

## 5. Substitute: what makes refactoring safe?

Paul Chiusano and Rúnar Bjarnason, [Functional Programming in Scala](https://livebook.manning.com/book/functional-programming-in-scala/chapter-1), ch. 1:

> [...] we construct our programs using only pure functions—in other words, functions that have no side effects. [...] A function has a side effect if it does something other than simply return a result.

Christopher Strachey, [Fundamental Concepts in Programming Languages](https://www.cs.cmu.edu/~crary/819-f09/Strachey67.pdf) (1967 lectures):

> One of the most useful properties of expressions is that called by Quine [4] referential transparency. In essence this means that if we wish to find the value of an expression which contains a sub-expression, the only thing we need to know about the sub-expression is its value.

> The introduction of the assignment command alters all this [...] we can no longer even be sure that the Boolean expression x = x has the value True. Referential transparency has been destroyed, and without it we have lost most of our familiar mathematical tools—for how much of mathematics can survive the loss of identity?

> Any departure of R-value referential transparency in a R-value context should either be eliminated by decomposing the expression into several commands and simpler expressions, or, if this turns out to be difficult, the subject of a comment.

Refactor by substitution: wherever a call cannot be replaced by its value, find the hidden input and pass it explicitly.

## 6. Specify: which laws hold?

Koen Claessen and John Hughes, [QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf) (ICFP 2000):

> Functional programs are well suited to automatic testing. It is generally accepted that pure functions are much easier to test than side-effecting ones, because one need not be concerned with a state before and after execution.

> We have designed a simple domain-specific language of testable specifications which the tester uses to define expected properties of the functions under test. QuickCheck then checks that the properties hold in a large number of cases.

> Properties are normally written in the same module as the functions they test, where they serve also as checkable documentation of the behaviour of the code.

> [...] they make it easy to repeat tests after each modification to a program. [...] If the law fails, then quickCheck reports the counterexample.

Write each law the function must satisfy as a property beside it; generated cases hunt the counterexample.

## 7. Convict: which idioms hurt by design?

The six moments above are also the suspects: each tool has a variant that keeps the ceremony and drops the cargo, and the communities that built them keep handing down verdicts.

Bodigrim, [CLC proposal 167: Add foldl' to Prelude](https://github.com/haskell/core-libraries-committee/issues/167) (approved, shipped in base-4.20):

> Currently `Prelude` exports `foldl` (which is an anti-pattern most of the time, especially for lists), but does not export `foldl'`. This is silly and harmful, especially for newcomers, who easily fall into the trap and get space leaks even in the simplest programs.

Tobias Nipkow, [Programming and Proving in Isabelle/HOL](https://isabelle.in.tum.de/website-Isabelle2024/dist/library/Doc/Prog_Prove/Isar.html), on the tactic scripts Isar was written to replace:

> Apply-scripts are unreadable and hard to maintain. The language of choice for larger proofs is Isar.

Scala 3 book, [Contextual Abstractions](https://docs.scala-lang.org/scala3/book/ca-contextual-abstractions-intro.html), on the redesign of implicits:

> The design of Scala 3 focuses on **intent** rather than **mechanism**. [...] It makes implicits easier to learn and harder to abuse.

Judge an idiom by what its working design costs, not by its worst use: convict the smallest variant that carries the harm, acquit the parent, and name the scope. The register of convictions lives in [slop.md](slop.md).
