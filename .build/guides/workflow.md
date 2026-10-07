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
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

**Work tracking (Interactor Build engine):**
- Every code change needs a tracked **Goal**. Create it in the Build web UI or with `ibuild engine goal-create "<title>"` / `ibuild engine goal queue <goalId>`. GitHub issues become Goals only when explicitly imported.
- Work on branch **`goal/<goalId>`** in an isolated worktree, **never on `main`/`biograph-fh`**. Changes ship through the goal's single PR, which the engine opens and which must pass review and CI. Each Goal's EngineTasks go through investigation → execution → review.
- Reading code is always allowed. The gate applies once you write files.

**Branches:** the fork's default branch is `biograph-fh`. Goal branches are `goal/<slug>-<id>`. Upstream sync from `earthians/marley version-16` uses `git cherry-pick -x` under a fork-intent-wins conflict policy, with every outcome recorded in `wiki/upstream-sync-version-16.md`.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, in lower case and with a subject. Add a scope suffix where helpful, e.g. `fix: ... (upstream sync B2)` or `docs(wiki): ...`.

**PRs:** follow the PR template: explain the problem and the change, keep logic server-side, update docs, add `closes #N`. Mergify merges a PR after one approval (label `squash` to squash, `dont-merge` to block). Backport with the `backport develop` label. CODEOWNERS: @akurungadam @Sajinsr.
