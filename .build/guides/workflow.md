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
  - .mergify.yml
  - commitlint.config.js
  - .github/labeler.yml
  - .github/helper/install.sh
---

**Work tracking (Interactor Build engine)**
- Every code change needs a tracked **Goal**: no Goal, no edits. Reading is always fine.
- Create Goals in the Build web UI or with `ibuild engine goal-create "<title>"` + `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
- The engine breaks each Goal into **EngineTasks**. Each task runs investigation → execution → review, driven by `ibuild engine work <task>` / `ibuild engine report --yes`.
- For small interactive changes, `ibuild off` may be used if the project allows it. The change still goes on its own branch with a hand-opened PR that runs CI.

**Branching**
- The default and integration branch is **`biograph-fh`**. Never commit or push directly to it.
- Work goes on **`goal/<goalId>`** branches (e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`) in an isolated worktree. Each goal gets one PR into `biograph-fh`.
- Upstream branches (`develop`, `version-14/15/16`, `version-*-hotfix`) belong to earthians. Mergify auto-closes PRs to stable `version-*` branches from non-maintainers.
- Upstream sync is done with `git cherry-pick -x` of `earthians/marley version-16` commits, in batches recorded in `wiki/upstream-sync-version-16.md`. When fork and upstream conflict, the fork's intent wins.

**Commits and PRs**
- Conventional commit titles, enforced by commitlint (`feat|fix|docs|test|chore|refactor|perf|style|ci|build|revert`), with optional scopes such as `fix(tests):` or `docs(wiki):`.
- Merges happen through Mergify after at least 1 approval. Add the `squash` label to squash-merge, or `dont-merge` to hold.
- Labels: `needs-tests` (added automatically), `skip-release-notes`, and `backport <branch>`.
