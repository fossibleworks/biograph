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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

# Workflow

## Work tracking (Interactor Build engine)
- Every change needs a tracked **Goal** (issue → Goal). Create it in the Build web UI or with `ibuild engine goal-create`.
- Work on branch `goal/<goalId>` in an isolated worktree. Never commit to the default branch (`biograph-fh` here).
- Each Goal ships through **one PR**, opened by the engine, which must pass review and CI. Engine tasks cycle through investigation → execution → review.
- For small interactive changes, `ibuild off` is allowed. The change must still go through its own branch and a hand-opened PR.

## Commits and PRs
- **Conventional commits** are enforced by commitlint on PRs. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Use a lower-case type and a non-empty subject.
- PR template: choose the target branch, give a conventional title, and confirm tests pass. Business logic goes server-side; update docs; add `closes #N`; include screenshots for UI changes.
- Upstream branch model: `develop` plus `version-1x-hotfix`. PRs to stable `version-14/15/16` are auto-closed by Mergify. Backports use `backport <branch>` labels.
- Mergify auto-merges after 1 approval and green CI. Add the `squash` label to squash, or `dont-merge` to block.
- CODEOWNERS: @akurungadam @Sajinsr.
