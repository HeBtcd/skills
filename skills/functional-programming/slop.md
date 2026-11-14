# FP slop: the register of convictions

Verdicts from a falsification pass over the FP canon: independent panels nominated and defended each idiom, then a prosecution attacked every acquittal and a final defense attacked every conviction.

The standard: an idiom is guilty when working as designed already hurts, when the mechanism is the harm. Where only a variant hurts, convict the variant and acquit the parent. Where a design hurts only inside a contract it dissolves, record the verdict as context-bound. Overuse of an honest tool is the programmer's crime, not the idiom's.

## Universal convictions

### Composition machinery

| Idiom | Working as designed costs | On record |
| --- | --- | --- |
| Transformer stacks of three or more concrete layers as application architecture | the nesting order is a semantics the signature never states, plus quadratic lift plumbing; the community retreated twice, mtl to effect systems to explicit handles | [Extensible Effects](https://okmij.org/ftp/Haskell/extensible/exteff.pdf); Snoyman, [The ReaderT Design Pattern](https://www.fpcomplete.com/blog/readert-design-pattern/) |
| Free monad and tagless-final as the default effect discipline | an AST plus an interpreter to rediscover the function call; freer measured about thirty times slower than mtl | [freer monads](https://reasonablypolymorphic.com/blog/freer-monads/); De Goes, [The Death of Tagless Final](https://degoes.net/articles/tagless-horror) |
| Eager effect types as the pure primitive (Scala `Future`) | eagerness plus memoization is in the definition; binding the value changes its meaning | cats-effect documentation contrasts it with `IO` |
| Capability constraint soup (`Has*` environment signatures) | parametricity theatre over an environment that is constant | |
| Cake pattern self-type wiring | an is-a dependency with initialization-order landmines; mass teardowns on record | the "cake pattern is a lie" postmortems |
| Purity by interpreter | an operation ADT plus its interpreter with identical behavior: the same code written twice so it may be called pure | |

### Implicit machinery

| Idiom | Working as designed costs | On record |
| --- | --- | --- |
| Implicit conversions | the compiler rewrites a value's type at a call site nothing marks | confined behind a language flag: [Scala 3 changed features](https://docs.scala-lang.org/scala3/reference/changed-features/implicit-conversions.html) |
| Implicit resolution as control flow or API surface | a call's behavior is decided by what was in scope at the import site; the designer's own keynote enumerated the errors | "Some Mistakes We Made When Designing Implicits", Typelevel Summit 2019; [Contextual Abstractions](https://docs.scala-lang.org/scala3/book/ca-contextual-abstractions-intro.html) |
| Orphan instances | coherence's global uniqueness breaks quietly: a `Set` built under one `Ord` reads wrong under another | ezyang, [Type classes: confluence, coherence, global uniqueness](https://blog.ezyang.com/2014/07/type-classes-confluence-coherence-global-uniqueness/) |
| Whitebox-macro auto-derivation | instance structure recomputed per call site; coproduct derivation measured quadratic | Scala compiler-team analyses of macro-heavy derivation; shapeless's author joined dotty to make it redundant |
| Type-level programming exposed as API (singletons, HList, sized vectors) | users pay the proof tax and still hit the runtime check underneath; singletons measured up to 48 percent of a benchmark | Dependently Typed Haskell in Industry (experience report) |
| HKT simulation encodings (`Kind` URIs, defunctionalization, witness types) | the language lacks the abstraction, so the encoding reproduces it badly: inference collapses, errors unreadable | Effect-TS issue 1005 dropped the URI registry; fp-ts rewritten |
| Profunctor or van Laarhoven optics as the exposed API | a missing field reports `Could not deduce (Bicontravariant p)` | [well-typed/optics](https://github.com/well-typed/optics) exists to escape those errors |

### Evaluation defaults

| Idiom | Working as designed costs | On record |
| --- | --- | --- |
| Laziness by default | thunk accumulation is the default space behavior, and even experienced programmers cannot predict it | every strict descendant refused it: [PureScript, Differences from Haskell](https://github.com/purescript/documentation/blob/master/language/Differences-from-Haskell.md); Lean 4, Idris, F#, OCaml, Elm |
| Lazy I/O | handle lifetime bound to demand and GC order; a closed handle yields empty output silently | the conduit, pipes and streamly ecosystems exist to replace it |
| `foldl`, the lazy left fold | correct usage, correct types, correct result, and a stack of thunks | its own committee calls it an anti-pattern: [CLC 167](https://github.com/haskell/core-libraries-committee/issues/167) |
| Partial functions on the default surface (`head`, `!!`, `fromJust`) | blessed imports that crash on legal input | `x-partial` warnings in [Data.List](https://hackage.haskell.org/package/base/docs/Data-List.html) |
| `Foldable` instances on degenerate containers | `length (1,2)` returns 1 and `maximum (99,0)` returns 0: type-correct nonsense | the Foldable Wats thread on the libraries list |
| MonadPlus and Alternative law ambiguity | the specification publishes two mutually exclusive law sets and agrees on neither | the MonadPlus reform proposals |

### Style and ritual

| Idiom | Working as designed costs | On record |
| --- | --- | --- |
| Tacit golf beyond a single composition | the arguments vanish and the diff becomes decryption | "pointless" is the community's own name: [Tacit programming](https://en.wikipedia.org/wiki/Tacit_programming) |
| Auto-curry plus placeholder combinator libraries | every call site pays the reorder tax, and `flip` exists to confess the parameter order was wrong | Elm 0.19 removed `curry`, `flip` and custom operators: [upgrade instructions](https://github.com/elm/compiler/blob/master/docs/upgrade-instructions/0.19.0.md) |
| Arrows as application plumbing | several classes and a dozen methods to compose what Applicative already composes | Netwire's author abandoned arrows and Reflex was born; Mokhov, Selective Applicative Functors (ICFP 2019) |
| Recursion-scheme zoos as the default AST representation | two declarations per tree so a `cata` can fold it; zygohistomorphic prepromorphism is a real exported name | [github/semantic retrospective](https://github.com/github/semantic/issues/662) |
| Comonads as application architecture | `extend` and `duplicate` gymnastics to say "a structure with a focus" | |
| Church encoding as storage representation, CPS as API | values become functions: no case analysis, no sharing, no inspector view | the callback-hell to async-await migration, ecosystem scale |
| Refinement towers of per-field smart constructors | the check still runs at runtime while the compile-time tax is paid | |
| Zero-information law ceremony | properties written for combines that obviously hold: ceremony nonzero, information zero | |
| Category-theory naming tax in domain APIs | every reader must carry the CT dictionary where a domain word exists | |
| `unsafe*` and purity theatre (`unsafePerformIO`, `@uncheckedVariance`) | lying to the type system is the use | |
| No-loop dogma on platforms without tail calls | a lawful mutual recursion overflows on legal input sizes; the trampoline workaround charges an allocation per step | |
| Option transplanted wholesale into nullable languages | a second null appears (`Some(null)`, uninitialized Option fields) while the first stays open | |
| Prelude-transplant libraries (LanguageExt, fp-ts into imperative hosts) | the design goal is paradigm replacement; every contributor learns two vocabularies | |
| OCaml functors and `include` as default composition | the heaviest syntactic tool made the default; packed modules copied wholesale until module aliases were invented | Jane Street's packed-modules postmortem |

## Context-bound convictions

A design acquitted in general can still be guilty inside a contract it dissolves. Any architecture that bets on checkable roots (a pure step folded over a log, a typed boundary, a declared effect surface) inherits seven failure mechanisms. Inside the roots, convict the form that does the dissolving:

- **Dissolving the anchor**: a root the recognizer cannot identify: curried entry points, bodies assembled from combinators, monkeypatched or injected behavior.
- **Hiding behind the tool's construction**: code living where the checker's model ends: generated code and macro expansions, implicit conversions the checker strips away, template or type-level dispatch erased at runtime, delegate invocation that reachability never follows, library types it cannot see into.
- **Smuggling a channel the contract does not carry**: environment or allocator parameters that carry behavior, lazy and thunk fields, ref-cells laundering mutation, hidden memoization, runtime type dispatch, event streams, exceptions as ordinary branching.
- **Running a second fold beside the lawful one**: nested replay, reduce chains doing the step's work, recursion schemes on the contract's data, unbounded recursion where the contract iterates.
- **Pushing cost outside the accounting window**: per-element rebuild cascades, large-value copies inside hot loops, per-step deep clones, trampolines.
- **Claiming self-awarded immunity**: generated-code markers, `@ts-ignore`, `as any`, `const_cast`, `mutable`, `unchecked` escapes.
- **Forging the contract's equality**: hand-rolled equality or serialization beside the canonical one, erased untagged unions, wrapper layers that change the wire shape, unordered containers where order is data, tuples across the boundary, stringly-typed discriminants, boolean parameters hiding what should be a case, silent truncation and default-swallowing, unchecked accessors on the contract's paths.

## Acquitted after falsification

Tagged unions on closed domains; Option and Result as plain data; currying; opt-in laziness; a single env parameter of plain configuration; folds as named loops; bounded recursion; coherent typeclasses; type machinery kept inside a library's internals; tactic interaction during development; recursion schemes inside their library; comonads over zippers and cellular automata; do-notation; monoid and semigroup the abstractions; persistent data structures where history is data (an append-only log is one); native HKT; laws written beside non-obvious properties; memoization; single-layer newtypes; erased type aliases; whole-value replacement (`with`, `Next = State`); single terminal aggregations over small bounded collections.

## Case law: executed by their own maintainers

`foldl` ([CLC 167](https://github.com/haskell/core-libraries-committee/issues/167), approved); `head`/`tail`/`init`/`last` marked partial (base-4.19 onward); `Monad.fail` split out ([MonadFail Proposal](https://wiki.haskell.org/MonadFail_Proposal)); datatype contexts and `n+k` patterns removed (Haskell 2010); the implicit mechanism split into given/using/Conversion, implicit conversions flagged (Scala 3); the Scala 3 dropped list (`CanBuildFrom`, view bounds, `any2stringadd`, `DelayedInit`); Elm's own FRP ([A Farewell to FRP](https://elm-lang.org/news/farewell-to-frp)), custom operators, `curry`/`flip`, open FFI (Elm 0.19); Ltac1 replaced ([Rocq Ltac2](https://docs.rocq-prover.org/V8.19.1/refman/proof-engine/ltac2.html)); green-thread runtime removed before Rust 1.0 ([RFC 230](https://rust-lang.github.io/rfcs/0230-remove-runtime.html)); Monad of no return in progress; `ApplicativeDo` decoupling do-notation from Monad.
