---
name: show-your-math
disable-model-invocation: true
description: "Derive quantities and defaults from constraints, separating derivation from calibration and preference. Use when a number or default needs defending, or the user asks to see the working (show your work)."
---

# Show Your Math

Follow the [NIST Guide for the Use of the International System of Units](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-7-rules-and-style-conventions-expressing-values), Chapter 7, §§7.11 and 7.14.

Derive quantities and defaults from problem constraints using dimensional analysis, boundary conditions, and latency/memory/error budgets instead of inventing magic numbers. Separate what is forced by math (derivation), measured from the system (calibration), and chosen by policy (preference). Collapse algebraically equivalent formulas to the simplest one, and when precomputing constants or tables, fold only fixed terms and state what invalidates them. When a constraint the derivation needs is missing or conflicting, name the gap and sync with the user instead of guessing.

Show the derivation and its holding conditions, hand policy trade-offs back to the owner, and close with [Polya, How to Solve It](https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it):

> Can you check the result? Can you check the argument?
