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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

- Work is tracked through **Interactor Build**. Every code change needs a tracked **Goal** first, created in the web UI or with `ibuild engine goal-create`. A GitHub issue becomes a Goal only after an explicit import. EngineTasks under a Goal cycle through investigation → execution → review.
- Work on the branch **`goal/<goalId>`** in an isolated worktree. Never commit to the default branch **`biograph-fh`** directly. Every change ships through the goal's single PR, which must pass review and CI.
- `ibuild off` lets an interactive session skip the gate for a small change. That change still goes on its own branch through a hand-opened PR.
- Commits follow Conventional Commits (enforced by commitlint in CI). Scopes and suffixes such as `(upstream sync B2)` are used for traceability.
- **Upstream sync:** changes from earthians/marley `version-16` are applied with `git cherry-pick -x` under a "fork intent wins" conflict policy and logged in `wiki/upstream-sync-version-16.md`.
- PR template: pick the target branch, follow commit conventions, put business logic server-side, update docs, and add `closes #XXXX`.
- Mergify rules inherited from upstream: auto-merge after 1 approval plus CI (use the `squash` label to squash, `dont-merge` to hold), PRs to stable `version-*` branches are auto-closed, and labels trigger backports to `version-1x-hotfix`.
- CODEOWNERS: @akurungadam @Sajinsr.
- Project rules live in `.build/RULES.md`.
