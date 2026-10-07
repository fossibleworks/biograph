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
  - AGENTS.md
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - commitlint.config.js
---

# Workflow

## Work tracking (Interactor Build engine)
- Every code change ships through a tracked **Goal** in Interactor Build. A GitHub issue becomes a Goal only after an explicit import.
- The engine generates **EngineTasks** under the Goal. Each task cycles through investigation → execution → review.
- **Gate before editing:**
  1. A Goal exists.
  2. Work happens on branch `goal/<goalId>` in an isolated worktree, never on the default branch.
  3. All changes ship through the Goal's single PR, which must pass review and CI.
- CLI: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`.
- `ibuild off` / `ibuild on` toggles the gate for small hand-PR changes. Those changes still go on their own branch with a PR that runs CI.
- Standing rules are in `.build/RULES.md`, which CLAUDE.md imports.

## Branches
- Fork integration branch: **`biograph-fh`**, the default/PR base for this repo.
- Upstream model (earthians):
  - `develop` is for features.
  - `version-1x-hotfix` is for fixes.
  - `version-14/15/16` are stable branches. Mergify auto-closes PRs from non-maintainers that target them.
  - Backports use labels (`backport develop`, `backport version-1x-hotfix`).
- Upstream syncs cherry-pick with `git cherry-pick -x` and record each commit's outcome in a `wiki/` ledger. Conflict policy: fork intent wins.

## Commits & PRs
- Conventional Commits, checked by commitlint in CI. Upstream-sync commits add a suffix such as `(upstream sync B2)`.
- PR template: pick the correct base, keep tests passing, keep validations server-side, update docs, and add `closes #XXXX`.
- Merging: Mergify merges after ≥1 approval and CI. The `squash` label squashes, and `dont-merge` blocks.
- CODEOWNERS: `@akurungadam @Sajinsr`.
