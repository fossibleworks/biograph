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
  - AGENTS.md
---

**Work tracking: Interactor Build engine** (from `CLAUDE.md`)
- Every code change belongs to a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. The engine generates **EngineTasks** beneath the Goal, and each task cycles through investigation → execution → review.
- **Gate before editing any file:** (1) a Goal exists, (2) work happens on branch `goal/<goalId>` in an isolated worktree, never on the default branch, (3) changes ship through the Goal's single PR, which must pass review and CI. Create Goals in the Build web UI or with `ibuild engine goal-create`. Use `ibuild engine work` / `report --yes` / `goal accept`.
- An interactive session may run `ibuild off` for a small change. The change still goes on its own branch with a hand-opened PR.
- Standing rules live in `.build/RULES.md` (currently a template). Local `.goals/` and `.tasks/` are untracked engine state.

**Branches**
- The fork's default/integration branch is **`biograph-fh`**. Goal branches are `goal/<slug>`.
- Upstream sync: cherry-pick from `earthians/marley version-16` with `git cherry-pick -x` in numbered batches (B1, B2, ...). Conflict policy is "fork intent wins". For doctype JSON, union `fields` / `field_order`. Union `patches.txt`. Keep the fork's `.releaserc` and version. Record every pick in `wiki/upstream-sync-version-16.md`, and tag commits with a suffix such as `(upstream sync B2)`.
- The inherited upstream rules (`.mergify.yml`) auto-close PRs to `version-1x` stable branches from non-maintainers. They auto-merge after at least one approval, and squash when the `squash` label is set. The `dont-merge` label blocks merging.

**Commits:** Conventional Commits (commitlint-enforced types), e.g. `fix: ...`, `docs(wiki): ...`, `test: ...`, `chore: bump version to 16.0.8`.
