---
name: review-the-pr
disable-model-invocation: true
description: "Review a pull request produced faster than anyone can read: machines verify what they can, context checks cover what the diff cannot carry, and a person signs the risk. Use when asked to review, approve, or sign off on a PR, or to sweep a codebase for every instance of a defect class."
---

# Review the PR

Code review for agent-written pull requests: machines verify what they can, context checks cover what the diff cannot carry, and a person signs the risk. Six moments, in the order the work meets them.

## 1. Gate: does this change even make sense, and can it be read?

Google's [Navigating a CL in Review](https://google.github.io/eng-practices/review/reviewer/navigate.html), step one:

> Look at the CL description and what the CL does in general. Does this change even make sense? If this change shouldn’t have happened in the first place, please respond immediately with an explanation of why the change should not be happening.

Step two, when the change outruns the reader:

> If the CL is too large for you to figure out which parts are the major parts, ask the developer what you should look at first, or ask them to split up the CL into multiple CLs.

## 2. Machines: what did the checks already prove?

Read the machine verdicts before the code; a checkable claim no machine checked is a missing check. Sadowski, [*Software Engineering at Google*](https://abseil.io/resources/swe-book/html/ch20.html), ch. 20 "Static Analysis":

> Anything that can be fixed automatically should be fixed automatically.

> static analysis can save reviewer time by highlighting common issues automatically; static analysis tools help the code review process (and the reviewers) scale. Code review is a sweet spot for analysis results.

> pointing out formatting errors is not a good use of a human reviewer’s time.

The Linux kernel docs, [Submitting patches](https://docs.kernel.org/process/submitting-patches.html), on ordering:

> automated CI processes that attempt to run a series of tests in order to establish the quality of your submission before the maintainer starts the review.

## 3. Look: does the code carry the intent?

The navigation guide sets the reading order:

> Sometimes it’s also helpful to read the tests first before you read the main code, because then you have an idea of what the change is supposed to be doing.

Google's [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) sets the checks:

> The most important thing to cover in a review is the overall design of the CL. Do the interactions of various pieces of code in the CL make sense? Does this change belong in your codebase, or in a library? Does it integrate well with the rest of your system? Is now a good time to add this functionality?

> Does this CL do what the developer intended? Is what the developer intended good for the users of this code?

> Tests do not test themselves, and we rarely write tests for our tests—a human must ensure that tests are valid.

> Will the tests actually fail when the code is broken?

> In the general case, look at *every* line of code that you have been assigned to review. [...] you should at least be sure that you *understand* what all the code is doing.

Then the context the diff cannot carry:

> Usually the code review tool will only show you a few lines of code around the parts that are being changed. Sometimes you have to look at the whole file to be sure that the change actually makes sense. [...] It’s also useful to think about the CL in the context of the system as a whole. Is this CL improving the code health of the system or is it making the whole system more complex, less tested, etc.? **Don’t accept CLs that degrade the code health of the system.**

And the limits of your own read: get a qualified reviewer, and say what your review covered:

> If you understand the code but you don’t feel qualified to do some part of the review, make sure there is a reviewer on the CL who is qualified, particularly for complex issues such as privacy, security, concurrency, accessibility, internationalization, etc.

> In these cases, note in a comment which parts you reviewed. [...] If you instead wish to grant LGTM after confirming that other reviewers have reviewed other parts of the CL, note this explicitly in a comment to set expectations.

## 4. Sweep: where else does this defect live?

One instance in the diff means the class may be everywhere. GitHub's CodeQL docs name the move [variant analysis](https://codeql.github.com/docs/codeql-overview/about-codeql/):

> Variant analysis is the process of using a known security vulnerability as a seed to find similar problems in your code. It’s a technique that security engineers use to identify potential vulnerabilities, and ensure these threats are properly fixed across multiple codebases.

The instance found in review is the seed:

> develop or iterate over the query to automatically find logical variants of the same bug that could be missed using traditional manual techniques.

## 5. Standard: approve when it leaves the codebase healthier

Google's [The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html):

> In general, reviewers should favor approving a CL once it is in a state where it definitely improves the overall code health of the system being worked on, even if the CL isn’t perfect.

> there is no such thing as “perfect” code—there is only *better* code.

> Nothing in this document justifies checking in CLs that definitely *worsen* the overall code health of the system. The only time you would do that would be in an emergency.

> it is the duty of the reviewer to make sure that each CL is of such a quality that the overall code health of their codebase is not decreasing as time goes on.

> a reviewer has ownership and responsibility over the code they are reviewing.

## 6. Signature: a person signs the risk

The Linux kernel docs, [Submitting patches](https://docs.kernel.org/process/submitting-patches.html), on whose name a review carries:

> Any interested reviewer (who has done the work and is a person with known identity) can offer a Reviewed-by tag for a patch.

What the tag attests, the Reviewer's Statement of oversight:

> By offering my Reviewed-by: tag, I state that:
>
> (a) I have carried out a technical review of this patch to evaluate its appropriateness and readiness for inclusion into the mainline kernel.
>
> (b) Any problems, concerns, or questions relating to the patch have been communicated back to the submitter. I am satisfied with the submitter's response to my comments.
>
> (c) While there may be things that could be improved with this submission, I believe that it is, at this time, (1) a worthwhile modification to the kernel, and (2) free of known issues which would argue against its inclusion.
>
> (d) While I have reviewed the patch and believe it to be sound, I do not (unless explicitly stated elsewhere) make any warranties or guarantees that it will achieve its stated purpose or function properly in any given situation.

Hand the person a record they can sign to (a) through (d): what the machines proved, which parts you reviewed, every problem raised, and how each was answered.
