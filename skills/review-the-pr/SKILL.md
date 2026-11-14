---
name: review-the-pr
disable-model-invocation: true
description: "Review or sign off on a pull request produced faster than anyone can read it. Use when asked to approve a diff too big to read line by line, or to sweep a codebase for every instance of a defect class."
---

# Review the PR

Spend finite attention where it decides the verdict; make the artifact carry the evidence the unread remainder cannot give.

## 1. The Standard of Code Review

Google's engineering practices, [The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html):

> [...] it is the duty of the reviewer to make sure that each CL is of such a quality that the overall code health of their codebase is not decreasing as time goes on.

> [...] a reviewer has ownership and responsibility over the code they are reviewing.

> **In general, reviewers should favor approving a CL once it is in a state where it definitely improves the overall code health of the system being worked on, even if the CL isn’t perfect.**

> [...] there is no such thing as “perfect” code—there is only better code.

State your verdict as a claim about the code health of the system, and name what degrades when you cannot approve.

## 2. Navigating a CL in Review

Google's engineering practices, [Navigating a CL in Review](https://google.github.io/eng-practices/review/reviewer/navigate.html):

> Look at the CL description and what the CL does in general. Does this change even make sense?

> Find the file or files that are the “main” part of this CL. [...] Look at these major parts first. This helps give context to all of the smaller parts of the CL, and generally accelerates doing the code review.

> If the CL is too large for you to figure out which parts are the major parts, ask the developer what you should look at first, or ask them to split up the CL into multiple CLs.

> If you see some major design problems with this part of the CL, you should send those comments immediately, even if you don’t have time to review the rest of the CL right now.

> [...] it’s also helpful to read the tests first before you read the main code, because then you have an idea of what the change is supposed to be doing.

Read the description and the tests before the implementation, and ask the author to name the main part when it is not obvious.

## 3. What to Look For in a Code Review

Google's engineering practices, [What to Look For in a Code Review](https://google.github.io/eng-practices/review/reviewer/looking-for.html):

> The most important thing to cover in a review is the overall design of the CL.

> Does this CL do what the developer intended? Is what the developer intended good for the users of this code?

> “Too complex” usually means “can’t be understood quickly by code readers.”

> Ask for unit, integration, or end-to-end tests as appropriate for the change. [...] Make sure that the tests in the CL are correct, sensible, and useful. Tests do not test themselves, and we rarely write tests for our tests—a human must ensure that tests are valid.

> In the general case, look at every line of code that you have been assigned to review. Some things like data files, generated code, or large data structures you can scan over sometimes, but don’t scan over a human-written class, function, or block of code and assume that what’s inside of it is okay.

> [...] some code deserves more careful scrutiny than other code—that’s a judgment call that you have to make—but you should at least be sure that you understand what all the code is doing.

> If it’s too hard for you to read the code and this is slowing down the review, then you should let the developer know that and wait for them to clarify it before you try to review it.

> Don’t accept CLs that degrade the code health of the system.

Read every line you approve, and ask for clarification where the code is too hard to read.

## 4. Inspection rate

SmartBear, [Best Practices for Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/), on its study of a Cisco Systems team:

> [...] developers should review no more than 200 to 400 lines of code (LOC) at a time. The brain can only effectively process so much information at a time; beyond 400 LOC, the ability to find defects diminishes.

> [...] a review of 200-400 LOC over 60 to 90 minutes should yield 70-90% defect discovery.

> [...] research shows a significant drop in defect density at rates faster than 500 LOC per hour.

> [...] performance starts dropping off after about 60 minutes.

> Omissions in particular are the hardest defects to find because it's difficult to review something that isn't there. Checklists are the most effective way to eliminate frequently made errors and to combat the challenges of omission finding.

> Authors should annotate code before the review occurs because annotations guide the reviewer through the changes, showing which files to look at first and defending the reason behind each code modification.

> [...] "spot checking" 20% to 33% of the code resulted in lower defect density with minimal time expenditure.

Choose which files get your sharpest hour, work a checklist there, ask the author to annotate the rest, and note which parts you reviewed.

## 5. Debugging is twice as hard

Kernighan and Plauger, [The Elements of Programming Style](https://en.wikiquote.org/wiki/Brian_Kernighan), 2nd edition, chapter 2:

> Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

For the parts you did not read, require runnable evidence of behavior: tests that pin the change, a demo, or a reproduction.

## 6. Variant analysis

GitHub, [About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/):

> CodeQL is a language and toolchain for code analysis. It is designed to allow security researchers to scale their knowledge of a single vulnerability to identify variants of that vulnerability across a wide range of codebases.

> Variant analysis is the process of using a known security vulnerability as a seed to find similar problems in your code. It’s a technique that security engineers use to identify potential vulnerabilities, and ensure these threats are properly fixed across multiple codebases.

> [...] develop or iterate over the query to automatically find logical variants of the same bug that could be missed using traditional manual techniques.

> [...] run that query across a large number of codebases, and identify all of the places where that vulnerability exists.

> Following interpretation, results are output for code review and triaging.

Write the defect's shape as a query, run it over the whole codebase, and triage every hit by hand.

## 7. Large-scale changes

Wright, [Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch22.html), chapter 22, "Large-Scale Changes":

> [...] an LSC is any set of changes that are logically related but cannot practically be submitted as a single atomic unit.

> LSCs at Google are almost always generated using automated tooling.

> In our experience, organic migrations are unlikely to fully succeed, in part because engineers tend to use existing code as examples when writing new code.

> Every change should be tested [...], but the larger the change, the more difficult it is to actually test it appropriately.

> [...] run as many tests as you can to be sure the change is safe.

> [...] local owners don't often treat LSCs with the same rigor as regular changes—they trust the engineers generating LSCs too much.

> Instead of reviewing each change individually, global reviewers use a separate set of pattern-based tooling to review each of the changes and automatically approve ones that meet their expectations. Thus, they need to manually examine only a small subset that are anomalous because of merge conflicts or tooling malfunctions, which allows the process to scale very well.

Cut the fix into the largest shards you can test and review, and clear every instance before the old pattern seeds new code.

## 8. Static analysis

Sadowski, [Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch20.html), chapter 20, "Static Analysis":

> Static analysis refers to programs analyzing source code to find potential issues such as bugs, antipatterns, and other issues that can be diagnosed without executing the program.

> Static analysis is [...] an integral tool in the API deprecation process, where it can prevent backsliding during migration of the codebase to a new API.

> Anything that can be fixed automatically should be fixed automatically.

> [...] analyses are contributed by developers who discover a bug and would like to prevent the same kind of bug from reappearing anywhere else in the codebase.

> [...] static analysis can save reviewer time by highlighting common issues automatically; static analysis tools help the code review process (and the reviewers) scale. Code review is a sweet spot for analysis results.

Leave the sweep's check standing in the review pipeline, so the pattern is flagged on every future change.
