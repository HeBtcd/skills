---
name: let-it-crash
disable-model-invocation: true
description: "Design or review failure-path contracts and ownership. Use when deciding who owns a check, auditing error handling, or checking whether a breach could pass unnoticed."
---

# Let It Crash

Draw the caller/callee boundary by contract ([Meyer, Applying "Design by Contract"](https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf), IEEE Computer, October 1992):

> The precondition expresses requirements that any call must satisfy if it is to be correct; the postcondition expresses properties that are ensured in return by the execution of the call.

> In the absence of assertions, defensive programming may be the only reasonable approach. But with techniques for defining precisely each party's responsibility, as provided by assertions, such redundancy (so harmful to the consistency and simplicity of the structure) is not needed.

Precondition breach is a caller bug; postcondition breach is a callee bug; only outcomes left open by the contract are runtime failure paths. Give each invariant, state, and cache invalidation a single owner, separating rules the code already enforces from ones you propose.

Parse untrusted input once at the boundary into types that make illegal states unrepresentable ([Minsky, Effective ML Revisited](https://blog.janestreet.com/effective-ml-revisited/)) and delete redundant interior checks ([King, Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)):

> Get your data into the most precise representation you need as quickly as you can. Ideally, this should happen at the boundary of your system, before any of the data is acted upon.

> Shotgun parsing is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing code — throwing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the "bad" cases.

Do not guard against hypothetical threats you cannot trigger concretely; expanding scope for speculative defenses is the user's call ([Fowler, Yagni](https://martinfowler.com/bliki/Yagni.html)):

> The code for the presumptive feature adds some complexity to the software, this complexity makes it harder to modify and debug that software, thus increasing the cost of other features.

> Yagni only applies to capabilities built into the software to support a presumptive feature, it does not apply to effort to make the software easier to modify.

Pick the exception-safety level each failure path requires: basic, strong, or no-throw ([Abrahams, Exception-Safety in Generic Components](https://docs.cppalliance.org/user-guide/exception-safety.html)); fail visibly instead of swallowing errors into corrupt state ([Shore, Fail Fast](https://martinfowler.com/ieeeSoftware/failFast.pdf); [PEP 20](https://peps.python.org/pep-0020/)):

> A system that fails fast does exactly the opposite: when a problem occurs, it fails immediately and visibly.

> If you use a global exception handler, avoid catch-all exception handlers in the rest of your application. They'll prevent exceptions from reaching your global handler.

> Errors should never pass silently.
> Unless explicitly silenced.

Silencing or defaulting belongs to the caller's contract; catch only to recover, clean up, or translate into domain terms, and pair every crash with an external supervisor that restores a safe state ([Armstrong, Making reliable distributed systems in the presence of software errors](https://erlang.org/download/armstrong_thesis_2003.pdf), PhD thesis, 2003, ch. 13):

> The Erlang philosophy for building fault-tolerant software can be summed up in two easy-to-remember phrases: "Let some other process fix the error" [...] "Let it crash"

Assert internal invariants where relied on, and pair enforcement with detection: name the metric, check, or log that surfaces bypassed or pre-existing breaches and who watches it.
