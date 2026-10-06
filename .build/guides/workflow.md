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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

Work is tracked through **Interactor Build** (`CLAUDE.md`).

**Before any file edit:**
1. A tracked **Goal** must exist. Create it in the web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. Never commit to `biograph-fh` (the default branch) directly.
3. Ship everything through the Goal's single PR. It must pass review and CI before merge.

Each EngineTask goes through investigation → execution → review. Report with `ibuild engine report --yes`; after merge, deliver with `ibuild engine goal accept <goalId>`.

An interactive session may use `ibuild off` for a small change. That change still goes on its own branch through a hand-opened PR that runs CI.

**Other conventions:**
- Commits follow Conventional Commits. Upstream picks use `git cherry-pick -x`, and fork-specific fixes note "(upstream sync Bn)".
- PRs follow the PR template: explain the change, include screenshots, keep logic server-side, add `closes #N`.
- Code owners: @akurungadam, @Sajinsr.
- Standing project rules live in `.build/RULES.md`, which is currently a placeholder.
