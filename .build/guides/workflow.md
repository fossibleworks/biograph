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
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Engine gate (from CLAUDE.md)**
- Every code change needs a tracked **Goal** in Interactor Build. Create one in the web UI or with `ibuild engine goal-create "<title>"` and `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
- Do the work on branch **`goal/<goalId>`** in an isolated worktree, and never on the default branch.
- Each Goal ships through **one PR** that the engine opens. EngineTasks under a Goal cycle through investigation → execution → review.
- For small changes, `ibuild off` is allowed: use a hand-opened PR from its own branch, which still runs CI.

**Branches**
- The fork's default/integration branch is **`biograph-fh`**. Upstream is `earthians/marley` `version-16`, and the fork syncs it with `git cherry-pick -x` under a "fork intent wins" conflict policy. Record the outcome of each sync in `wiki/upstream-sync-version-16.md`.
- Inherited upstream conventions:
  - `develop` is for features.
  - `version-1X-hotfix` is for fixes.
  - Stable `version-14/15/16` branches don't accept PRs; Mergify auto-closes PRs from non-maintainers.
  - Backports use `backport <branch>` labels.

**PRs**
- Commit and PR titles follow Conventional Commits (commitlint).
- Put `closes #XXXX` in the PR body.
- `feat` PRs link docs or say `no-docs`.
- Merges need at least 1 approval plus green CI. Mergify does a merge commit by default, or a squash with the `squash` label; `dont-merge` blocks.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- Standing project rules go in `.build/RULES.md`, which is currently an unfilled template.
