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

## Interactor Build engine (this fork)

- Every code change needs a tracked **Goal**, created in the Build web UI or with `ibuild engine goal-create`. GitHub issues become Goals only after an explicit import. EngineTasks under a Goal go through investigation, then execution, then review.
- Work on branch **`goal/<goalId>`** in an isolated worktree, **never on the default branch `biograph-fh`**. Changes ship via the goal's single PR, which must pass review and CI. Do not push directly. `ibuild off` allows a small hand-opened PR when the project permits it.
- Standing rules live in `.build/RULES.md`, which is imported by CLAUDE.md and mirrored to `.claude/rules/` and `.github/instructions/`. Edit the source file, not the mirrors.

## Conventions inherited from upstream

- Commits and PR titles follow Conventional Commits, enforced by commitlint in CI.
- Mergify **auto-closes PRs to stable branches** (`version-14/15/16`) unless they come from maintainers or bots. Target `develop` or a hotfix branch instead (on this fork, `biograph-fh` via a goal branch). Mergify merges after 1 approval and CI. Add the label `squash` to squash-merge, `dont-merge` to block, and `backport <branch>` to backport.
- CODEOWNERS: `@akurungadam @Sajinsr` own everything.
- PR body: explain the problem, add screenshots, include `closes #XXXX`, and add a docs link for `feat` PRs.

## Upstream syncing

Cherry-pick from `upstream` (earthians/marley `version-16`) with `-x` and record every outcome in `wiki/upstream-sync-version-16.md` (picked-clean / picked-with-conflict-resolution / already-present / skipped). Fork intent wins conflicts.
