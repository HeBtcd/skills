---
name: review-the-pr
disable-model-invocation: true
description: "Code review for agent-written pull requests: machines verify what they can, context checks cover what the diff cannot carry, and a person signs the risk. Use when asked to review, approve, or sign off on a PR produced faster than anyone can read, or when the reviewer is also an agent."
---

# Review the PR

Layer automated checks, fresh-context review, repo rules, human sign-off, and fast rollback ([Anthropic, How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/), Oct 2026):

> We think "did a human read the code?" is an imprecise proxy for "what could go wrong with this change, and which check—automated or human—is the right one to catch it?"

## Machine checks and fresh-context passes

Require actual command output (tests, build, visual diff), then review the diff in a fresh context separate from the author session. Reject specification gaming: deleting, skipping, or weakening tests, assertions, lints, or type/permission checks to reach green; edit a test only when its old assertion was provably wrong.

Verify candidate findings before surfacing them, resolve each (fixed, false positive, intentional, won't-fix) to tune reviewer rules, flag each bug class once, re-review only new commits, and cap automated review-fix loops at a few rounds; if it still churns, rethink the approach. Encode repo-specific conventions and recurring review comments into in-repo rules or CI checks.

## Human sign-off and rollout

Scale approval to diff risk: trusted authors get the fast lane; sensitive paths and untrusted changes need a second human reviewer. On agent PRs:

> An agent's approval never counts as a person's, either.

> An approval covers one specific commit.

The prompting human counts as one reviewer; sign-off attests to intent, assumptions, and design via a completed staff-work summary (outcome, verified vs assumed, trade-offs, recommendation). Merge through a re-testing queue, gate new behavior behind feature flags with one-step rollback, own production breakages, and turn escaped bugs into new checks.
