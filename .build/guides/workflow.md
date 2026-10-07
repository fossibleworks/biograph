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
  - .github/CODEOWNERS
  - commitlint.config.js
---

**Work tracking (Interactor Build engine):**
- Every code change needs a tracked **Goal** (create one in the Build web UI or with `ibuild engine goal-create`). A GitHub issue becomes a Goal only after an explicit import. The engine creates **EngineTasks** under the Goal, and each task cycles through investigation → execution → review.
- Work happens on the **`goal/<goalId>`** branch in an isolated worktree, **never on the default branch**. All changes ship through the goal's single PR, which the engine opens and which must pass review and CI. An interactive session may run `ibuild off` for a small change, but that change still goes through its own branch and a hand-opened PR.

**Branches:**
- Fork integration branch: **`biograph-fh`** (the default/PR base).
- Inherited upstream model: `develop` for development, hotfix branches `version-N-hotfix`, and stable `version-14/15/16`. Mergify **auto-closes PRs against stable branches** opened by anyone other than the listed maintainers.
- Upstream sync from `earthians/marley` `version-16` uses `git cherry-pick -x` in batches. Fork behaviour wins conflicts. Every commit's outcome (picked-clean / picked-with-conflict-resolution / already-present / skipped) is recorded in `wiki/upstream-sync-version-16.md`.

**PRs and commits:**
- Conventional Commit titles (commitlint). Fill out the PR template (details, screenshots, `closes #N`). Mergify merges once there is ≥1 approval: a merge commit by default, or a squash with the `squash` label. `dont-merge` blocks merging, and `backport develop` triggers a backport.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- Project rules live in `.build/RULES.md` (currently placeholders) and `AGENTS.md` (Build-managed guides block).
