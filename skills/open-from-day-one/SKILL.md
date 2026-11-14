---
name: open-from-day-one
disable-model-invocation: true
description: "Shape a project so a stranger on a clean machine can build, run, change, release, and take it over without asking you: README, one-step build, self-testing code, CONTRIBUTING, changelog, semver, license, bus factor. Use when starting a repo, open-sourcing one, or auditing what your departure would strand."
---

# Open From Day One

Set each piece below up once and the next person to touch the repo never needs to ask you anything.

## 1. Be open from day one

Do every step in a manner compatible with a future handover.

Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/setting-tone.html#be-open-from-day-one), "Be Open From Day One":

> Start your project out in the open from the very first day. The longer a project is run in a closed source manner, the harder it is to open source later.

> At each step in a project, programmers face a choice: to do that step in a manner compatible with a hypothetical future open-sourcing, or do it in a manner incompatible with open-sourcing. And every time they choose the latter, the project gets just a little bit harder to open source.

> "In the open" means the following things are publicly accessible, in standard formats, from the first day of the project: the code repository, bug tracker, design documents, user documentation, wiki (if any), and developer discussion forums. It also means the code and documentation are placed under an open source license, of course. And it means that your team's day-to-day work takes place in the publicly visible area.

## 2. README

Put what it is, how to install it, how to run it, and where to ask for help on the repo's front page.

Danny Guo, [Make a README](https://makeareadme.com/):

> A README is a text file that introduces and explains a project. It contains information that is commonly required to understand what the project is about.

> Definitely before you show a project to other people or make it public. You might want to get into the habit of making it the first file you create in a new project.

> Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a **Requirements** subsection.

> Use examples liberally, and show the expected output if you can.

> For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit.

> If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going.

## 3. One-step build

Reduce checkout-to-build to a single script, and prove it on a clean machine.

Joel Spolsky, [The Joel Test: 12 Steps to Better Code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/), step 2:

> Can you make a build in one step? By this I mean: how many steps does it take to make a shipping build from the latest source snapshot? On good teams, there's a single script you can run that does a full checkout from scratch, rebuilds every line of code, makes the EXEs, in all their various versions, languages, and #ifdef combinations, creates the installation package, and creates the final media — CDROM layout, download website, whatever.

> If the process takes any more than one step, it is prone to errors. And when you get closer to shipping, you want to have a very fast cycle of fixing the "last" bug, making the final EXEs, etc. If it takes 20 steps to compile the code, run the installation builder, etc., you're going to go crazy and you're going to make silly mistakes.

## 4. Self-testing code

Make one command run the whole suite, and treat untested code as broken.

Martin Fowler, [Self-Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html):

> You have self-testing code when you can run a series of automated tests against the code base and be confident that, should the tests pass, your code is free of any substantial defects.

> When done well this allows you to invoke a single command that executes the tests - and you are confident that these tests will illuminate any bugs hiding in your code.

> But the biggest benefit isn't about merely avoiding production bugs, it's about the confidence that you get to make changes to the system.

> Our attitude is to assume that any non-trivial code without tests is broken.

## 5. CONTRIBUTING

Publish the path a change takes: how to file an issue, how to open a pull request, what review expects.

GitHub Docs, [Setting guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors):

> To help your project contributors do good work, you can add a file with contribution guidelines to your project repository's root, `docs`, or `.github` folder. When someone opens a pull request or creates an issue, they will see a link to that file.

> For contributors, the guidelines help them verify that they're submitting well-formed pull requests and opening useful issues.

> For both owners and contributors, contribution guidelines save time and hassle caused by improperly created pull requests or issues that have to be rejected and re-submitted.

> In the new file, add contribution guidelines. These could include:
> - Steps for creating good issues or pull requests.
> - Links to external documentation, mailing lists, or a code of conduct.
> - Community and behavioral expectations.

## 6. Keep a Changelog

Record every notable change under `Unreleased`, and promote it to a dated version at each release.

Olivier Lacan, [Keep a Changelog](https://keepachangelog.com/en/1.1.0/):

> A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

> Keep an `Unreleased` section at the top to track upcoming changes. [...] At release time, you can move the `Unreleased` section changes into a new release version section.

> If you do nothing else, list deprecations, removals, and any breaking changes in your changelog.

## 7. Semantic Versioning

Let the version number tell adopters what kind of change they are taking on.

Tom Preston-Werner, [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html):

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 1. MAJOR version when you make incompatible API changes
> 2. MINOR version when you add functionality in a backward compatible manner
> 3. PATCH version when you make backward compatible bug fixes

> Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

> Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

## 8. License

Add the LICENSE file before the first outside contribution arrives.

GitHub, [Choose a License](https://choosealicense.com/no-permission/), "No License":

> When you make a creative work (which includes code), the work is under exclusive copyright by default. Unless you include a license that specifies otherwise, nobody else can copy, distribute, or modify your work without being at risk of take-downs, shake-downs, or litigation. Once the work has other contributors (each a copyright holder), "nobody" starts including you.

> If you find software that doesn't have a license, that generally means you have no permission from the creators of the software to use, modify, or share the software.

> An open source license allows reuse of your code while retaining copyright.

## 9. Bus factor

Move knowledge out of one head: docs for the processes, second maintainers for the keys.

Wikipedia, [Bus factor](https://en.wikipedia.org/wiki/Bus_factor):

> The "bus factor" is the minimum number of team members that have to suddenly disappear from a project before the project stalls due to lack of knowledgeable or competent personnel.

> A bus factor of one is a single point of failure whereas a bus factor greater than one means there is some redundancy for every part of the process.

> A good bus factor means many individuals know enough to carry on and the project could still succeed even in very adverse events.

> Several ways to improve the bus factor have been proposed:
> - Reduce complexity
> - Document all processes and keep that documentation up-to-date
> - Encourage cross-training
