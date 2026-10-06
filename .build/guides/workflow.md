---
title: Workflow
category: workflow
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - CLAUDE.md
  - .build/RULES.md
  - commitlint.config.js
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/workflows/semantic-commits.yml
---

**Work tracking (Interactor Build engine).** Every code change belongs to a tracked **Goal**. A Goal maps 1:1 to a GitHub issue and owns one branch and one PR. Work happens on branch `goal/<goalId>` in an isolated worktree, **never on `main`/`biograph-fh` directly**, and ships through the Goal's PR after review and CI gates. Create Goals in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. Engine tasks cycle through investigation → execution → review. Reading code needs no Goal; writing does. `ibuild off` is an exception for small changes, but those still go through a hand-opened PR with CI.

**Branches.** The fork's integration branch is `biograph-fh`. Upstream (earthians) uses `develop` plus `version-14/15/16` stable branches with `version-N-hotfix` branches. Mergify **auto-closes PRs to stable `version-*` branches** from anyone outside the maintainer list.

**Commits.** Conventional Commits are enforced by commitlint. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`; the type must be lower-case and the subject non-empty. Scopes are used like `docs(wiki): …`, and upstream-sync commits are suffixed `(upstream sync B2)`.

**Upstream sync.** Cherry-pick with `git cherry-pick -x` from `earthians/marley` `version-16`. The rule is that **fork intent wins**: keep all biograph-fh behaviour and add the upstream fix on top. Doctype JSON gets a 3-way union of `fields`/`field_order`, `patches.txt` gets a union, and the fork's `.releaserc` version is kept. Record every commit's outcome in `wiki/upstream-sync-version-16.md`.

**Review and merge.** CODEOWNERS (`@akurungadam @Sajinsr`) review. Mergify auto-merges (or squashes with the `squash` label) after ≥1 approval and green CI, unless the PR is labelled `dont-merge`. `feat` PRs need a docs link or `no-docs`.
