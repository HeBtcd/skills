---
name: clean-history
description: Prepare or organize a task’s Git changes into coherent commits.
---

# Clean History

Determine task changes and commit boundaries from the request, working tree, and history. Preserve outside history; follow-up work adds commits. Whole-repository squashing requires explicit scope. Resolve uncertain boundaries before rewriting.

Make complete, reviewable commits describing resulting behavior and purpose. Combine intermediate fixes; separate independent, coherent changes. Preserve intended content and attribution; leave unrelated work untouched.

Check the final diff and sequence for intended changes and preserved history. Retain a recoverable reference before authorized rewrites. Push only when authorized; replace published commits with a lease against the inspected remote head, reassessing if it changes.
