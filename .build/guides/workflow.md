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
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/CODEOWNERS
---

# Workflow

## Interactor Build engine (this fork)
- Every code change needs a tracked **Goal**. Create it with `ibuild engine goal-create "<title>"` or the Build web UI. A GitHub issue becomes a Goal only after an explicit import.
- **EngineTasks** under the Goal go through investigation → execution → review.
- Work on branch **`goal/<goalId>`** in an isolated worktree. Never commit to the default branch **`biograph-fh`** or to `main`.
- Each Goal ships as **one PR** opened by the engine, and it must pass review and CI before merging. `ibuild off` allows a small change without a Goal, but it still goes on its own branch through a hand-opened PR.
- Standing rules: `.build/RULES.md`, also mirrored in `.claude/rules/` and `.github/instructions/`.

## Commits and PRs
- **Conventional Commits**, enforced by commitlint on PRs. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case, and the subject is required. Scopes are used, e.g. `docs(wiki): ...`, `fix(tests): ...`, and a context suffix such as `(upstream sync B2)`.
- PR template: explain the problem, add screenshots, put `closes #N`, keep business logic server-side, and update docs. `feat` PRs need a docs link or `no-docs`.

## Upstream sync
- Pick commits from `earthians/marley` with `git cherry-pick -x`. Under the **fork intent wins** policy, keep biograph behaviour and layer the upstream fix on top.
- Union doctype JSON `fields`/`field_order` and `patches.txt`. Keep the fork's version.
- Record each pick's outcome in `wiki/upstream-sync-version-16.md`: picked-clean, picked-with-conflict-resolution, already-present, or skipped.

## Inherited upstream rules
`.mergify.yml` comes from upstream. It auto-closes PRs to stable `version-*` branches (use `*-hotfix` or `develop`), auto-merges after 1 approval, and supports `backport <branch>` labels. CODEOWNERS: @akurungadam @Sajinsr.
