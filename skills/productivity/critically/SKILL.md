---
name: critically
disable-model-invocation: true
description: Use a subagent to challenge claims or solutions when requested.
---

# Critically

Use one independent critic on a bounded claim or solution: fresh context with source requirements, constraints, artifact revision, and claim; original evidence before the main agent's explanations. Keep it read-only with no further agents; report unavailable if independence cannot hold.

Seek objections valid under the original meaning and constraints. Return the claim, refuting evidence or missing support, and what would settle it. Preference is not a defect; no objection is not proof.

The main agent supplies evidence, correction, or a gap. The same critic checks the reply and current artifacts against the original objection, including its own possible error. Stop when evidence resolves the dispute or exchange adds none. Return supported conclusions and unresolved dependencies; agreement cannot replace evidence.
