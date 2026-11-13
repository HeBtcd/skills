---
name: open-from-day-one
disable-model-invocation: true
description: "Takeover-readiness for a repo or artifact: keep it able to go public or change hands at any moment, so a stranger on a clean machine can build, run, change, release, and take it over without asking you. Use when shaping a project, checking repo hygiene, or preparing work for outsiders or future maintainers."
---

# Open from Day One

A repo stays ready to go public or change hands when a stranger on a clean machine can build, run, change, release, and take it over without asking you. Eight moments, in the order the work meets them.

## 1. Day one: could it go public right now?

Karl Fogel, [Producing Open Source Software](https://producingoss.com/en/setting-tone.html), "Be Open From Day One":

> Start your project out in the open from the very first day. The longer a project is run in a closed source manner, the harder it is to open source later.

> At each step in a project, programmers face a choice: to do that step in a manner compatible with a hypothetical future open-sourcing, or do it in a manner incompatible with open-sourcing. And every time they choose the latter, the project gets just a little bit harder to open source.

> "In the open" means the following things are publicly accessible, in standard formats, from the first day of the project: the code repository, bug tracker, design documents, user documentation, wiki (if any), and developer discussion forums. It also means the code and documentation are placed under an open source license, of course. And it means that your team's day-to-day work takes place in the publicly visible area.

> You open source your code, not your time.

Adam Wiggins's litmus test, [The Twelve-Factor App](https://12factor.net/config):

> A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials.

GitHub's [Open Source Guides](https://opensource.guide/starting-a-project/) pre-launch checklist applies the same test to history:

> There are no sensitive materials in the revision history, issues, or pull requests (for example, passwords or other non-public information)

## 2. Front door: does a stranger know what this is, and how to start?

Tom Preston-Werner, [Readme Driven Development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html):

> Write your Readme first.

> First. As in, before you write any code or tests or behaviors or stories or ANYTHING.

> The Readme should be the single most important document in your codebase; writing it first is the proper thing to do.

Fogel's name rules, [Producing Open Source Software](https://producingoss.com/en/getting-started.html):

> Gives some idea what the project does, or at least is related in an obvious way, such that if one knows the name and knows what the project does, the name will come quickly to mind thereafter.

> Is not the same as some other project's name [...] You don't want to create identity confusion.

Fogel's mission statement:

> [...] the next thing people will look for is a quick description or mission statement, so they can decide (within 30 seconds) whether or not they're interested in learning more. This should be prominently placed on the front page, preferably right under the project's name. [...] The description should be concrete, limiting, and above all, short.

GitHub's [Open Source Guides](https://opensource.guide/starting-a-project/), the README's four questions:

> * What does this project do?
> * Why is this project useful?
> * How do I get started?
> * Where can I get more help, if I need it?

Fogel, on the earliest documentation a newcomer needs:

> Describe clearly and thoroughly how to set up the software, and tell the user how to run some sort of diagnostic test or simple command to confirm that they've set things up correctly. Startup documentation is in some ways more important than actual usage documentation. [...] When people abandon, they abandon early; therefore, it's the earliest stages, like installation, that need the most support.

The threshold all of this lowers is Fogel's *hacktivation energy*:

> [...] the amount of energy a newcomer must put in before she starts getting something back. The lower a project's hacktivation energy, the better.

## 3. Permission: may they use and change it?

GitHub's [Choose a License](https://choosealicense.com/no-permission/), on what "no license" means:

> When you make a creative work (which includes code), the work is under exclusive copyright by default. Unless you include a license that specifies otherwise, nobody else can copy, distribute, or modify your work without being at risk of take-downs, shake-downs, or litigation. Once the work has other contributors (each a copyright holder), “nobody” starts including you.

> If you find software that doesn't have a license, that generally means you have no permission from the creators of the software to use, modify, or share the software.

Fogel:

> *The front page must make it unambiguously clear that the project is open source.* [...] State up front, in or near the mission statement, that the project is "free software" or "open source software", and give the exact license.

## 4. Clean machine: does it build where you aren't?

[The Twelve-Factor App](https://12factor.net/dependencies), dependencies:

> **A twelve-factor app never relies on implicit existence of system-wide packages.** It declares all dependencies, completely and exactly, via a *dependency declaration* manifest.

> One benefit of explicit dependency declaration is that it simplifies setup for developers new to the app. The new developer can check out the app's codebase onto their development machine, requiring only the language runtime and dependency manager installed as prerequisites. They will be able to set up everything needed to run the app's code with a deterministic *build command*.

Martin Fowler's rule of thumb, [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html):

> anyone should be able to bring in a clean machine, check the sources out of the repository, issue a single command, and have a running system on their own environment.

## 5. Proof: does every change prove it still works?

Fowler:

> We thus need to ensure that every commit is verified in a reference environment. The usual way to do this is with a **Continuous Integration Service (CI Service)** that monitors the mainline. [...] Every time the mainline receives a commit, the CI service checks out the head of the mainline into an integration environment and performs a full build. Only once this integration build is green can the developer consider the integration to be complete.

> A programmer's job isn't done merely when the new feature is working, but also when they have automated tests to prove it.

Kent Beck's rule, via Fowler:

> nobody has a higher priority task than fixing the build

Fowler:

> Imperfect tests, run frequently, are much better than perfect tests that are never written at all.

## 6. Change: how does a stranger's fix get in?

GitHub's [Open Source Guides](https://opensource.guide/starting-a-project/):

> A CONTRIBUTING file tells your audience how to participate in your project. For example, you might include information on:
> * How to file a bug report [...]
> * How to suggest a new feature
> * How to set up your environment and run tests

> In the earliest stages of your project, your CONTRIBUTING file can be simple. You should always explain how to report bugs or file issues, and any technical requirements (like tests) to make a contribution.

> Over time, you might add other frequently asked questions to your CONTRIBUTING file. Writing down this information means fewer people will ask you the same questions over and over again. [...] Link to your CONTRIBUTING file from your README, so more people see it.

Fogel, on what else the guidelines carry:

> Developer guidelines are not so much technical as social: they explain how the developers interact with each other and with the users, and ultimately how things get done. [...] some indication of *how* development is usually done and how decisions are made [...]

## 7. Release: what does a version say, and what changed?

Fogel:

> When you release a downloadable package, give it a unique version number, so that people can compare any two releases and know which supersedes the other.

[Semantic Versioning](https://semver.org/):

> Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 1. MAJOR version when you make incompatible API changes
> 2. MINOR version when you add functionality in a backward compatible manner
> 3. PATCH version when you make backward compatible bug fixes

> Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

Olivier Lacan, [Keep a Changelog](https://keepachangelog.com/en/1.1.0/):

> A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

> Changelogs are *for humans*, not machines.

> Keep an `Unreleased` section at the top to track upcoming changes. [...] At release time, you can move the `Unreleased` section changes into a new release version section.

## 8. Takeover: does the project survive losing you?

Wikipedia, [Bus factor](https://en.wikipedia.org/wiki/Bus_factor):

> [...] a measurement of the risk resulting from information and capabilities not being shared among team members, derived from the phrase "in case they get hit by a bus".

> The "bus factor" is the minimum number of team members that have to suddenly disappear from a project before the project stalls due to lack of knowledgeable or competent personnel.

> Several ways to improve the bus factor have been proposed: Reduce complexity, Document all processes and keep that documentation up-to-date, Encourage cross-training.

GitHub's [Open Source Guides](https://opensource.guide/starting-a-project/) pre-launch checklist:

> At least two people have administrative access to the project

The audit for all eight is one walk: clone the repo onto a machine you do not control, follow only what is written down, and note where the stranger stalls; every stall lands on the moment that failed.
