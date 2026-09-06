---
name: runtime-probes
disable-model-invocation: true
description: Specify debugger probes, capture conditions, and recovery; assess collected results.
---

# Runtime Probes

Specify the smallest distinguishing probe. Record available debugger/target state, separating existing probes, proposed additions, and unknowns.

Define each probe's target, capture condition/values, sampling window, and removal condition. Prefer passive observation; stopping probes require immediate hit handling, bounded pause, and supported resume.

For success and interruption, recover original state: remove additions, restore existing probes, clear introduced pauses, resume, and verify final state.

Return probe/recovery specifications, separating available observations from expectations. Report unverified cleanup/restoration when assessing collected records.
