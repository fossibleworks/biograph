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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/CODEOWNERS
---

## Interactor Build engine (from CLAUDE.md)

- Every code change needs a tracked **Goal**. Create one in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`.
- Work on branch **`goal/<goalId>`** in an isolated worktree. Never work on the default branch **`biograph-fh`**. Existing branches follow this pattern, e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`.
- Every change ships through the Goal's single PR, which must pass review and CI. Nobody pushes directly to `biograph-fh`.
- EngineTasks under a Goal cycle through investigation, execution and review (`ibuild engine work`, `ibuild engine report --yes`).
- Standing rules live in `.build/RULES.md`. It is mirrored into `.claude/rules/` and `.github/instructions/`; edit only the source.

## Commits

- Conventional Commits, enforced by commitlint.
- Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lower-case.
- Scopes are used, e.g. `fix(tests): ...`, `docs(wiki): ...`.
- Upstream sync commits use `git cherry-pick -x` and add a suffix such as `(upstream sync B2)`.

## PRs

- Follow the template: target branch, conventional title, tests passing, server-side validation, docs updated, `closes #XXXX`, screenshots.
- Upstream (earthians) rules come from `.mergify.yml`. Stable `version-*` branches are bot-only. Merging needs at least one approval; the `squash` label squash-merges and `dont-merge` blocks. Backports are requested with `backport <branch>` labels.
- CODEOWNERS: @akurungadam @Sajinsr.
