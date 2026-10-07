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
  - .mergify.yml
  - .github/workflows/semantic-commits.yml
  - commitlint.config.js
  - .github/CODEOWNERS
---

**Work tracking: Interactor Build engine (required)**
- Every code change belongs to a tracked **Goal**. A GitHub issue maps to a Goal, but only after an explicit import. EngineTasks under a Goal cycle through investigation, then execution, then review.
- **Gate before editing:** a Goal must exist. Work happens on branch **`goal/<goalId>`** in an isolated worktree, **never on the main branch**. All changes ship through the Goal's single PR, which the engine opens and which must pass review and CI.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. The web UI at build.interactor.com always works.
- Small interactive changes may use `ibuild off`. They still go through their own branch and a hand-opened PR with CI.

**Branches**
- The fork's integration branch is **`biograph-fh`**, which is the PR base. Upstream earthians uses `develop`, `version-1x-hotfix` and the stable `version-14/15/16`. Mergify auto-closes PRs against stable `version-*` branches from non-maintainers.
- **Upstream sync:** use `git cherry-pick -x` from `earthians/marley version-16`. Conflict policy: **fork intent wins**. Record each pick in `wiki/upstream-sync-version-16.md` (picked-clean, picked-with-conflict-resolution, already-present or skipped).

**Commits and PRs**
- Conventional commits, enforced by commitlint in CI (`feat|fix|chore|docs|refactor|perf|test|style|ci|build|revert`, lower case). Scopes are used, for example `docs(wiki): ...`.
- `feat` PRs need a wiki docs link, or `no-docs` in the body.
- CODEOWNERS: `@akurungadam @Sajinsr` own everything.
- Run `pre-commit` locally before pushing.
