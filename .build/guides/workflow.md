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
  - AGENTS.md
  - .build/RULES.md
  - commitlint.config.js
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine):** every code change needs a tracked **Goal**.
- Create it in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`.
- Work happens on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the integration branch directly.**
- Each goal ships as **one PR**, which the engine opens and which must pass review and CI.
- EngineTasks under a Goal go through investigation, then execution, then review.
- For a small change, `ibuild off` lets an interactive session skip the Goal. The change still goes on its own branch through a hand-opened PR.

**Branches**
- The fork's integration/default branch is **`biograph-fh`** (`origin/HEAD`). Goal branches look like `goal/<slug>-<id>`.
- Upstream (`earthians/biograph` / `marley`) uses `develop`, `version-NN-hotfix` and `version-NN`. Mergify there auto-closes PRs to stable `version-*` branches from non-maintainers.

**Commits**
- Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test.
- Types are lower-case and the subject is required. Scopes are used, e.g. `docs(wiki): ...` and `fix: ... (upstream sync B2)`.
- Upstream picks use `git cherry-pick -x` and are logged in the wiki ledger. When fork and upstream conflict, fork intent wins.

**PRs**
- Follow the PR template: explain the problem, add screenshots for UI changes, and add `closes #XXXX`.
- Business logic belongs on the server.
- CODEOWNERS are `@akurungadam @Sajinsr`.
- Mergify auto-merges after one approval and green CI. The `squash` label switches it to squash; `dont-merge` blocks merging.
