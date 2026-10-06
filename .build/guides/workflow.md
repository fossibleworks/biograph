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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - .releaserc
---

- **Interactor Build engine gate:**
  - Every code change needs a tracked **Goal**. Create it in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create`.
  - Work happens on branch `goal/<goalId>` in an isolated worktree, never directly on the default branch.
  - Changes ship through the Goal's single PR, after review and CI gates.
  - EngineTasks under a Goal cycle through investigation → execution → review.
  - Interactive sessions may use `ibuild off` for small changes, which still go through a hand-opened PR.
- **Default/integration branch:** `biograph-fh`. Upstream release branches are `version-14/15/16` (used by semantic-release); `develop` is the upstream dev branch.
- **Commits:** Conventional Commits with lower-case types (`build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`). The `semantic-commits` workflow checks this with commitlint. Scopes in use include `docs(wiki)` and `fix(tests)`.
- **PRs:**
  - Follow the PR template: target branch, conventional title, tests pass, business logic server-side, docs updated, `closes #XXXX`, screenshots.
  - `feat` PRs need a wiki docs link or `no-docs`.
  - CODEOWNERS (`@akurungadam @Sajinsr`) review everything.
- **Upstream syncs from earthians/marley:**
  - Cherry-pick with `git cherry-pick -x`.
  - The fork's intent wins on conflict.
  - Doctype JSON is merged as a union.
  - Every pick is recorded in `wiki/upstream-sync-version-16.md` with its outcome (picked-clean / with-conflict-resolution / already-present / skipped / deferred).
