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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - .mergify.yml
---

**Work tracking (Interactor Build engine)**, per `CLAUDE.md`:
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal, but only after an explicit import. The engine generates **EngineTasks** under the Goal, and each task goes through investigation → execution → review.
- Before writing any file: make sure a Goal exists (create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <id>`). Work on branch **`goal/<goalId>`** in an isolated worktree, **never on the main branch**.
- All changes ship through the Goal's single PR, which must pass review and CI. No direct pushes. For small changes an interactive session may run `ibuild off`, but the change still goes on its own branch with a hand-opened PR.
- Project rules live in `.build/RULES.md`, which feeds the generated rule files.

**Branches:** `biograph-fh` is the fork's main integration branch. Release lines are `version-14`, `version-15` and `version-16`, with `version-1x-hotfix` branches; upstream development happens on `develop`. Upstream syncs from `earthians/marley version-16` use `git cherry-pick -x` and are logged in batches (B1, B2, …) in the wiki ledger.

**Commits and PRs:**
- Conventional Commit titles, enforced by commitlint.
- The PR template asks you to pick the target branch, confirm tests pass, keep logic server-side, update docs, and link issues with `closes #NNN`.
- `@akurungadam` and `@Sajinsr` are CODEOWNERS for everything.
- Mergify config is present (`.mergify.yml`).
