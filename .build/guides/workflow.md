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
  - .mergify.yml
  - .github/CODEOWNERS
  - commitlint.config.js
---

- **Work tracking:** this repo is connected to **Interactor Build**. Each change is a tracked **Goal**, created in the Build web UI, from an imported GitHub issue, or with `ibuild engine goal-create`. Under each Goal, **EngineTasks** cycle through investigation → execution → review.
- **Gate:** do not edit files without a Goal. Work on branch `goal/<goalId>` in an isolated worktree, **never on the main branch `biograph-fh`**. Changes ship through the goal's single PR, which must pass review and CI. Small interactive changes may use `ibuild off`, but they still go through their own branch and a hand-opened PR.
- **Branches:** the fork's integration branch is `biograph-fh`, and goal branches look like `goal/<slug>-<id>`. Upstream (earthians) uses `develop`, `version-1x-hotfix` and stable `version-1x`. Mergify auto-closes PRs against stable branches unless they come from maintainers, and handles backports through `backport <branch>` labels.
- **Upstream sync:** cherry-pick from `earthians/marley` `version-16` with `git cherry-pick -x`. Fork intent wins in conflicts. Record each commit in `wiki/upstream-sync-version-16.md`.
- **Commits:** Conventional Commits, checked by commitlint on every PR, with scopes like `fix(tests):` or `docs(wiki):`.
- **PRs:** follow `.github/PULL_REQUEST_TEMPLATE.md`. Explain the problem, add screenshots for UI changes, put `closes #N`, and keep business logic server-side. Mergify merges after ≥1 approval (squash if labelled `squash`; `dont-merge` blocks it). Default code owners are @akurungadam and @Sajinsr.
- Standing rules for AI sessions belong in `.build/RULES.md`, which is currently an unfilled template.
