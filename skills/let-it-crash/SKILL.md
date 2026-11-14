---
name: let-it-crash
disable-model-invocation: true
description: "Audit failure paths under the let-it-crash doctrine: who detects a failure, who recovers it, who must be correct, and when restarts give up. Use when deciding who validates what on failure paths, auditing error handling, or checking whether a failure could pass unnoticed."
---

# Let It Crash

Four moments on a failure path, in the order the work meets them.

## Fail-fast

Jim Gray, [Why Do Computers Stop and What Can Be Done About It?](https://pages.cs.wisc.edu/~remzi/Classes/739/Fall2015/Papers/gray-why-do-computers-stop-85.pdf) (Tandem TR 85.7, 1985):

> The process approach to fault isolation advocates that the process software module be fail-fast, it should either function correctly or it should detect the fault, signal failure and stop operating.

> Processes are made fail-fast by defensive programming. They check all their inputs, intermediate results, outputs and data structures as a matter of course. If any error is detected, they signal a failure and stop. In the terminology of [Cristian], fail-fast software has small fault detection latency.

> * Make each module fail-fast -- either it does the right thing or stops.
> * Detect module faults promptly by having the module signal failure or by requiring it to periodically send an I AM ALIVE message or reset a watchdog timer.

For each component on the path, confirm it either does its job or stops, and name who receives the signal.

## Let it crash

Joe Armstrong, [Making reliable distributed systems in the presence of software errors](https://erlang.org/download/armstrong_thesis_2003.pdf) (PhD thesis, 2003), chapters 3 to 4 and Appendix B:

> Let some other process do the error recovery.
>
> If you can't do what you want to do, die.
>
> Let it crash.
>
> Do not program defensively.

> One process, the worker process, does the job. [...] If an error occurs in the worker, the supervisor takes actions to correct the error.

> It often turns out that the error correcting code is generic, that is, generally applicable to many applications, whereas the worker code is more often application specific.

> The answer is let it crash. By this I mean that in the event of an error, then the program should just crash. But what is an error? For programming purpose we can say that:
>
> exceptions occur when the run-time system does not know what to do.
>
> errors occur when the programmer doesn't know what to do.

> error handling only occurs if a local attempt to fix the error fails. In the event of an exception a local process may be able to detect and correct the fault which caused the exception, in which case as far as any other process in the system is concerned, no error has occurred.

> Don't clutter code for the "normal case" with code designed to handle exceptions. As far as possible you should only program the normal case. If the code for the normal case fails, your process should report the error and crash as soon as possible. Don't try to fix up the error and continue. The error should be handled in a different process.

> One of the basic elements of system design is identifying which part of the system has to be correct and which part of the system does not have to be correct. [...] The first part of the system design must be to identify that part of the system which must be correct; we call this the error kernel.

> Most of the code in the system should be written with the assumption that the input data to the function in question is correct. Only a small part of the code should actually perform any checking of the data. This is usually done when data "enters" the system for the first time [...] The caller is responsible for supplying correct input.

> The error logs which are generated when a software or hardware error is detected will be used at a later stage to diagnose and correct the error. A permanent record should be kept of any information that will be helpful in this process.

For every error on the path, name its owner: who checks the input at the boundary, which part must be correct, who crashes, and who corrects.

## Supervision

Erlang/OTP documentation, [Supervisor Behaviour](https://www.erlang.org/doc/system/sup_princ.html), on what the corrector does; the restart scope is one of `one_for_one`, `one_for_all`, `rest_for_one`:

> A supervisor is responsible for starting, stopping, and monitoring its child processes. The basic idea of a supervisor is that it is to keep its child processes alive by restarting them when necessary.

> If a child process terminates, only that process is restarted. [...] If a child process terminates, all remaining child processes are terminated. Subsequently, all child processes, including the terminated one, are restarted. [...] If a child process terminates, the child processes after the terminated process in start order are terminated. Subsequently, the terminated child process and the remaining child processes are restarted.

> * A `permanent` child process is always restarted.
> * A `temporary` child process is never restarted [...]
> * A `transient` child process is restarted only if it terminates abnormally, that is, with an exit reason other than `normal`, `shutdown`, or `{shutdown,Term}`.

> If more than `MaxR` number of restarts occur in the last `MaxT` seconds, the supervisor terminates all the child processes and then itself. [...] When the supervisor terminates, then the next higher-level supervisor takes some action. It either restarts the terminated supervisor or terminates itself.

> The intention of the restart mechanism is to prevent a situation where a process repeatedly dies for the same reason, only to be restarted again.

> Keep in mind that the total number of restarts (before the top level supervisor gives up and terminates the application) will be the product of the intensity values of all the supervisors above the failing child process.

> If you set intensity to 10 and set the period as low as 1, the supervisor will allow child processes to keep restarting up to 10 times per second, forever, filling your logs with crash reports until someone intervenes manually.

For each supervisor, read the restart scope, which children come back, the intensity and period that make it give up, and which level is told when it does.

## The regular failure case

Fred Hébert, [The Zen of Erlang](https://ferd.ca/the-zen-of-erlang.html) (2016), the audit itself:

> If I know how to handle an error, fine, I can do that for that specific error. Otherwise, just let it crash!

> Well for repeatable bugs on core features, restarting is useless. [...] For transient bugs though, restarting is extremely effective, and they tend to be the majority of bugs you'll meet live. [...] Rolling back to a known stable state and trying again is unlikely to hit the same weird context that causes them.

> With all of this done, our Erlang system now has all of the following properties defined:
> * what is critical or not to the survival of the system
> * what is allowed to fail or not, and at which frequency it can do so before it is no longer sustainable
> * [...]
> * how software should fail, meaning it defines the legal states of partial failures you find yourself in, and how to roll back to a known stable state when this happens
> * [...]
> * how components interdepend on each other

> In a nutshell, the Zen of Erlang and 'let it crash' is really all about figuring out how components interact with each other, figuring out what is critical and what is not, what state can be saved, kept, recomputed, or lost. In all cases, you have to come up with a worst-case scenario and how to survive it. By using fail-fast mechanisms with isolation, links & monitors, and supervisors to give boundaries to all of these worst-case scenarios' scale and propagation, you make it a really well-understood regular failure case.

> That sounds simple, but it's surprisingly good; if you feel that your well-understood regular failure case is viable, then all your error handling can fall-through to that case. You no longer need to worry or write defensive code. You write what the code should do and let the program's structure dictate the rest. Let it crash.

Walk each handler and keep the ones that know what to do; let the rest fall through, then check that what remains is a survivable, well-understood regular failure case.
