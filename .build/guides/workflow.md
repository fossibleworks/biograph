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
  - commitlint.config.js
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine), per `CLAUDE.md`:**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import.
- Do the work on branch `goal/<goalId>` in an isolated worktree. Never commit directly to the default branch.
- Every change ships through the Goal's single PR, which must pass review and CI.
- The `ibuild engine` CLI drives the lifecycle: `goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`.
- `ibuild off` allows a small, untracked hand-opened PR when the project permits it.
- Standing rules live in `.build/RULES.md`. It is currently an unfilled template.

**Branches:**
- The fork's integration/default branch is **`biograph-fh`**.
- Upstream (`earthians/marley`) uses `develop`, hotfix branches `version-NN-hotfix`, and stable `version-14/15/16`.
- Mergify auto-closes PRs against stable `version-*` branches from non-maintainers. Target a hotfix branch or develop instead.

**Upstream sync:**
- Cherry-pick with `git cherry-pick -x` from `upstream/version-16`.
- Record each commit's outcome in `wiki/upstream-sync-version-16.md`.
- Conflict policy: fork intent wins. Doctype JSON gets a 3-way union of `fields`/`field_order`, and `patches.txt` gets a union.
- Commits carry a `(upstream sync Bn)` suffix.

**Commits and PRs:**
- Conventional Commits, enforced by commitlint.
- PR template: pick the target branch, run the tests locally, keep business logic server-side, update docs, and reference `closes #N`.
- Merging needs at least one approving review. Mergify merges, or squashes when the PR has the `squash` label; `dont-merge` blocks.
- CODEOWNERS: @akurungadam @Sajinsr.
