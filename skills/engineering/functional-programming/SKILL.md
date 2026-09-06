---
name: functional-programming
disable-model-invocation: true
description: Design with value semantics, composable functions, explicit effects, and types encoding legal states and operations.
---

# Functional Programming

Encode legal domain states with algebraic data types.
Use value semantics; preserve observable identity.
Use typestate when legal operations vary by state.
Enforce value invariants with target-language facilities, such as refinement types or validated constructors.
Keep pure logic referentially transparent and computational effects explicit.
Express varying behavior with higher-order functions.
Use polymorphism only across distinctions the implementation does not inspect.
Require totality on the legal domain.
Preserve observable evaluation strategy.

Use Haskell notation to clarify types and combinations before expressing them in the target language, when helpful.
