---
name: open-from-day-one
disable-model-invocation: true
description: "Keep a repo or artifact ready to go public or change hands at any moment: a stranger on a clean machine can build, run, change, release, and take it over without asking you. Use when shaping a project, checking repo hygiene, or preparing work for outsiders or future maintainers."
---

# Open From Day One

Your process can stay private; the artifact must always be able to stand alone ([the twelve-factor app](https://12factor.net/config); [Fogel, Producing Open Source Software](https://producingoss.com/en/producingoss.html), Be Open From Day One):

> A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials.

> At each step in a project, programmers face a choice: to do that step in a manner compatible with a hypothetical future open-sourcing, or do it in a manner incompatible with open-sourcing.

## The test and the class

Walk every lifecycle verb (discover, clone, build, run, understand, change, release, take over) as a different person in your roles within the repo's declared support envelope (OS, toolchain, network). Whatever fails is a hidden dependency on you; a declared operator input (API key, paid seat) with a documented default is not.

Declare the class: **personal** (outlives the session and current machine), **handoff** (a stranger can build, run, change, release, take over), **public** (adds contribution path, security contact, release machinery), or **frozen** (use as-is). Every class bans irreversible dependencies from the first commit: secrets or personal data in history, personal-namespace publishing, murky contributor rights, missing license; keep reversible mess small.

## Hidden dependencies

- **Environment**: relative paths, declared prerequisites, dependencies declared and isolated with no assumed system tools ([12-factor II](https://www.12factor.net/dependencies)), backing services in config ([12-factor IV](https://12factor.net/backing-services)).
- **Source completeness**: preferred form for modification ([GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) Corresponding Source): generators, schemas, build scripts, never only generated or minified output.
- **Context**: entry-point contract (purpose, prerequisites, build/test commands, license, scope, public vs internal boundary) verified by running it literally; decisions and *why* in commits and records.
- **Residue**: strip one-off debris, redundant docs, dead branches, and caches, but version operational regeneration scripts ([Fogel, version everything](https://www.producingoss.com/en/technical-infrastructure.html)).
- **Legal surface**: full license file naming copyright holder ([Fogel, license quickstart](https://www.producingoss.com/en/license-quickstart.html)), compatible dependency licenses, per-asset coverage, clear trademark.
- **Verification**: in-repo tests and fixtures passing against an external oracle (spec, golden data, reference impl), not circular self-assertions.
- **Named good states**: versioned releases with human-readable notes ([OpenSSF criteria](https://www.bestpractices.dev/en/criteria)).
- **Control plane**: registries, domains, CI, and org seats under project accounts; transferable merge/release rights; transfer bundle beyond `git push` (issues, releases, discussions); no lockfile dependencies on personal namespaces. Survivability is whether someone else can take over, which is what the "bus factor" measures, not standing headcount ([Avelino et al., ESEM 2019](https://arxiv.org/abs/1906.08058)).
- **Data custody**: datasets, weights, or corpora in project-controlled or content-addressed storage with stated license.

Audit each dependency for decay (what rots and how it renews: vendoring/update tooling vs lockfiles). Community operation is a separate layer ([Fogel, Be Open From Day One, Not Day N](https://blog.opentechstrategies.com/2018/09/be-open-from-day-one/)):

> you open source your code, not your developers' time.

## Verify

Run the declared class's verbs from a fresh clone on a clean environment inside the envelope; fix any step that still has to ask you.
