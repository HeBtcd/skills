---
name: primitives
disable-model-invocation: true
description: Find basic operations that combine to build the required capability.
---

# Primitives

Start from required behavior and caller uses. Find small operations that combine to build that capability; expansion into branches, loops, and assignments alone does not improve its foundation.

Show inputs, outputs, changes, and composition before implementation details. Preserve required effects and order; do not assume purity.

For each replacement, account for every required behavior and potentially lost use. Moving rules into a new function does not show that the remaining operations provide them. Keep conclusions conditional on unknown requirements.

Return the operations, how they build the capability, and why each is needed. A useful foundation need not be globally smallest; no further decomposition found does not prove none exists.
