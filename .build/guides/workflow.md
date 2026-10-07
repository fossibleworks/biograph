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
  - .github/CODEOWNERS
  - .build/RULES.md
---

**Engine gate (Interactor Build, from CLAUDE.md):**
- Every code change needs a tracked **Goal**. Create one with `ibuild engine goal-create "<title>"` (then `ibuild engine goal queue <goalId>`), in the Build web UI, or by importing a GitHub issue.
- Work on branch `goal/<goalId>` in an isolated worktree. Never commit to the default branch.
- Changes ship through the goal's single PR, which passes review and CI. EngineTasks under a Goal cycle investigation → execution → review.
- Reading is always allowed.
- `ibuild off` lets an interactive session skip the Goal for small changes. It still needs its own branch and a hand-opened PR.

**Branches:**
- The fork's integration branch is `biograph-fh` (default).
- Goal branches look like `goal/<slug>-<id>`.
- Upstream release branches are `version-14/15/16`. Mergify auto-closes PRs to them from non-maintainers, so target hotfix or develop branches instead.

**Commits:** Conventional Commits, enforced by commitlint (`build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, lower-case type, non-empty subject). Optional scopes are used (`fix(linters):`, `feat(appointment):`, `docs(wiki):`).

**Upstream sync:** Cherry-pick from earthians/marley with `git cherry-pick -x`. Conflict policy: **fork intent wins**. Use a 3-way union for doctype JSON `fields`/`field_order` and a union for `patches.txt`. Log each pick's outcome in `wiki/upstream-sync-version-16.md`.

**Review and merge:**
- CODEOWNERS: @akurungadam, @Sajinsr.
- Mergify merges after at least one approval and CI success. Add the `squash` label to squash, or `dont-merge` to block.
- The PR template asks for passing tests, server-side validation, docs, and `closes #XXXX`.
