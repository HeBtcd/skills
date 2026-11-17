---
name: walk-states
description: "Walk a change's user stories and produce states, not an action log: known state in, event, observable state out, verdict per story. Use before claiming a feature or fix works, when a review needs evidence, or when a verify skill exists but no proof was produced."
---

# Walk States

A change is a set of claims about what a user can now do. Each claim earns a walk: a known state, an action, an observed state, a verdict. Five moments, in the order the walk meets them.

## The story is the unit

Enumerate the change as stories, not as files touched. Mike Cohn, [User Stories Applied](https://en.wikipedia.org/wiki/User_story): the acceptance criterion is what makes a story testable:

> Acceptance criteria are the conditions that a software product must satisfy to be accepted by a user, customer, or other stakeholder.

One story per thing the change claims a user can now do. "It compiles" is not a story; "a new user can finish signup" is. If a story has no observable condition, it is not a story yet, so sharpen it until it does.

## State in, event, state out

Walk each story as a triad: the known state before, the action, the observed state after. Cucumber's Gherkin reference, [Given-When-Then](https://cucumber.io/docs/gherkin/reference/):

> **Given** steps are used to describe the initial context of the system — the scene of the scenario.

> **Then** steps are used to describe an expected outcome, or result. [...] The outcome should be on an **observable** output. That is, something that comes *out* of the system (report, user interface, message) and not a behavior deeply buried inside the system (like reading a record from a database).

The action is only a means of reaching the resulting state; it is not the evidence. What matters is what is true after: the rendered page, the response body, the file's contents.

## The state is the proof

Prefer states the machine produces: a screenshot, a DOM snapshot, a diff of the file, the actual response. An action log ("I clicked", "I ran the test") is a claim made by the walker; the observed state is the evidence a reviewer can judge directly. The moment that goes wrong is usually the one missing from the action log; the state cannot omit it.

## Keep the event stream, show the state

Fowler on keeping the event log as the record, [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html):

> The fundamental idea of Event Sourcing is that of ensuring every change to the state of an application is captured in an event object, and that these event objects are themselves stored in the sequence they were applied for the same lifetime as the application state itself.

The raw trail stays underneath (screenshots per step, console output, the command log), but the deliverable is the projected state. A reviewer reads verdicts backed by states and descends into the trail only when a state looks wrong.

## Disclose the walk

Close out with the table, not a summary paragraph:

```markdown
### States

| story | in | event | out | verdict |
| --- | --- | --- | --- | --- |
| user filters inbox | seeded inbox, filter empty | apply filter "unread" | inbox shows only unread rows | pass |
```

Every story gets a row; every row carries the states that convict it. A story that could not be walked is a row with an empty state and a failed verdict, never a footnote.
