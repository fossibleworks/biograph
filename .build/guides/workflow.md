---
title: Work tracking & branching workflow
category: workflow
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - CLAUDE.md
  - .build/RULES.md
  - AGENTS.md
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/CODEOWNERS
  - commitlint.config.js
---

## Interactor Build engine (this fork)
- **No code edits without a tracked Goal.** Create one in the Build web UI or with `ibuild engine goal-create "<title>"` and `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
- Each Goal owns one branch, **`goal/<goalId>`** (e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`), worked in an isolated worktree, and **one PR** opened by the engine.
- EngineTasks under a Goal cycle through investigation → execution → review. Report each phase with `ibuild engine work <task>` and `ibuild engine report --yes`. After merge, accept the goal with `ibuild engine goal accept <goalId>`.
- **Never commit or push directly to the mainline `biograph-fh`.** For a small change, an interactive session may run `ibuild off`. The change still goes on its own branch through a hand-opened PR that runs CI.
- Standing AI rules live in `.build/RULES.md`, which is mirrored to `.claude/rules` and `.github/instructions`.

## Commits & PRs
- Conventional Commits, checked by commitlint on every PR.
- Follow the PR template: choose the target branch, follow the naming convention, make sure tests pass, keep business logic on the server, update docs, and add `closes #N`. Include screenshots for UI changes.
- Inherited upstream automation: Mergify auto-closes PRs to stable `version-1x` from non-maintainers, auto-merges after 1 approval (or squashes with the `squash` label), and handles backports through `backport <branch>` labels. CODEOWNERS: @akurungadam @Sajinsr.

## Upstream sync
Pull upstream Marley changes in batches with `git cherry-pick -x`. When there is a conflict, fork intent wins: take the 3-way union of doctype JSON fields and the union of `patches.txt`. Record every commit in `wiki/upstream-sync-version-16.md`.
