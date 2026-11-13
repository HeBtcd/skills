---
name: let-it-crash
disable-model-invocation: true
description: "Failure-path contracts and ownership: who owns each check, where recovery lives when the worker crashes, whether a breach could pass unnoticed. Use when deciding who validates what, auditing error handling, or checking whether a failure could go unseen."
---

# Let It Crash

Failure-path contracts: every check has an owner, every error a handler, every breach an alarm. Six moments, in the order the work meets them.

## 1. Error kernel: which parts must be correct

Joe Armstrong, [Making reliable distributed systems in the presence of software errors](https://erlang.org/download/armstrong_thesis_2003.pdf), Appendix B:

> One of the basic elements of system design is identifying which part of the system has to be correct and which part of the system does not have to be correct.

> In conventional operating system design the kernel of the system is assumed to be, and must be, correct, whereas all user application programs do not necessarily have to be correct. If a user application program fails this will only concern the application where the failure occurred but should not affect the integrity of the system as a whole.

> The first part of the system design must be to identify that part of the system which must be correct; we call this the error kernel.

Find the part of the system that must be correct; that is the error kernel. Everything outside it earns the right to be wrong.

## 2. Contract: who owns each check

Bertrand Meyer, [ET: Design by Contract (tm), Assertions and Exceptions](https://www.eiffel.org/doc/eiffel/ET-_Design_by_Contract_%28tm%29%2C_Assertions_and_Exceptions):

> It is in fact part of the Eiffel method that a routine body should **never** test for the precondition, since it is the client's responsibility to ensure it. [...] one can get more reliable software by having fewer explicit checks in the software text.

> **Rule -- Assertion Violation:** A run-time assertion violation is the manifestation of a bug.
>
> * A precondition violation signals a bug in the client, which did not observe its part of the deal.
> * A postcondition (or invariant) violation signals a bug in the supplier -- the routine -- which did not do its job.

> contracts are not a mechanism to test for special conditions, for example erroneous user input. For that purpose, the usual control structures [...] are available [...] An assertion is instead a **correctness condition** governing the relationship between two software modules (not a software module and a human, or a software module and an external device).

Assign every check its party: the client owns the precondition, the supplier owns the postcondition, and the boundary owns validation of input from outside. A violation names whose bug it is.

## 3. Supervisor: where recovery lives

Armstrong, [Making reliable distributed systems in the presence of software errors](https://erlang.org/download/armstrong_thesis_2003.pdf), ch. 4:

> exceptions occur when the run-time system does not know what to do.
> errors occur when the programmer doesn't know what to do.

> The philosophy is let some other process fix the error, but what does this mean for their code? The answer is let it crash. By this I mean that in the event of an error, then the program should just crash.

> The error-handling code and the code which has the error execute within different threads of control. The code which solves the problem is not cluttered up with the code which handles the exception.

> [...] the idea of handling errors, not where they occurred, but at some other place in the system.

Erlang/OTP documentation, [Supervisor Behaviour](https://www.erlang.org/docs/26/design_principles/sup_princ.html):

> A supervisor is responsible for starting, stopping, and monitoring its child processes. The basic idea of a supervisor is that it is to keep its child processes alive by restarting them when necessary.

> If more than MaxR number of restarts occur in the last MaxT seconds, the supervisor terminates all the child processes and then itself. [...] When the supervisor terminates, then the next higher-level supervisor takes some action. It either restarts the terminated supervisor or terminates itself.

For every place a failure can occur, name the process above it that owns the recovery. A handler living in the failing thread is a check with no owner.

## 4. Crash-only: can this thing die safely

George Candea and Armando Fox, [Crash-Only Software](https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea_html/), HotOS-IX 2003:

> Crash-only programs crash safely and recover quickly. There is only one way to stop such software -- by crashing it -- and only one way to bring it up -- by initiating recovery.

> Since crashes are unavoidable, software must be at least as well prepared for a crash as it is for a clean shutdown.

> A crash-only system makes it affordable to transform every detected failure into component-level crashes; this leads to a simple fault model, and components only need to know how to recover from one type of failure.

> To make components crash-only, we require that all important non-volatile state be kept in dedicated state stores [...] To make a system of interconnected components crash-only, it must be designed so that components can tolerate the crashes and temporary unavailability of their peers.

Audit each component as though pulling the plug were its only shutdown: where does its state live, and what does the first request after restart see?

## 5. Circuit breaker: when the failure is on their side

Martin Fowler, [CircuitBreaker](https://martinfowler.com/bliki/CircuitBreaker.html), describing Michael Nygard's pattern from *Release It!*:

> One of the big differences between in-memory calls and remote calls is that remote calls can fail, or hang without a response until some timeout limit is reached. What's worse if you have many callers on a unresponsive supplier, then you can run out of critical resources leading to cascading failures across multiple systems.

> You wrap a protected function call in a circuit breaker object, which monitors for failures. Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error, without the protected call being made at all.

> Not all errors should trip the circuit, some should reflect normal failures and be dealt with as part of regular logic.

> Breakers on their own are valuable, but clients using them need to react to breaker failures. As with any remote invocation you need to consider what to do in case of failure.

At every call that crosses to a supplier you do not control, name the timeout, the trip condition, and what your side does while the circuit is open.

## 6. Fail fast: a breach must announce itself

Jim Shore, [Fail Fast](https://www.martinfowler.com/ieeeSoftware/failFast.pdf), IEEE Software, Sept/Oct 2004:

> Some people recommend making your software robust by working around problems automatically. This results in the software "failing slowly." The program continues working right after an error but fails in strange ways later on. A system that fails fast does exactly the opposite: when a problem occurs, it fails immediately and visibly.

> Assertions are the key to failing fast. An assertion is a tiny piece of code that checks a condition and then fails if the condition isn't met. So, when something starts to go wrong, an assertion detects the problem and makes it visible.

> Assertions shine in their ability to flush out problems in the seams of the system. Use them to show mistakes in how the rest of the system interacts with your method.

> Place your assertions so that the software fails earlier--close to the original problem--making the problem easy to find.

> If you use a global exception handler, avoid catch-all exception handlers in the rest of your application. They'll prevent exceptions from reaching your global handler. [...] Search your existing code for catch-all exception handlers and either remove or refactor them.

For each place a failure could be swallowed, place a check that fires at the seam; a breach announces itself where it happened, or it stays hidden until it can't be traced.
