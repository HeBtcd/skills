---
name: just-throw
disable-model-invocation: true
description: Replace redundant error prose with typed failures and diagnostics in guards, exceptions, validation, or logs.
---

# Just Throw

Remove error prose duplicated by typed failures/runtime diagnostics while preserving consumer needs established by contracts and usage. Missing local callers do not prove public output unused; leave uncertain removals unresolved.

For programmer errors/invariant violations, use the most specific native error and parameter information; preserve source location, stack, and cause. Signal once unless a distinct observer needs a separate log.

Represent expected domain rejection as data; retain required natural-language text at its UI, CLI, localization, or protocol boundary.

Return proposed removals for reviews or changed failure signals for transformations, preserving diagnostics and external contracts.
