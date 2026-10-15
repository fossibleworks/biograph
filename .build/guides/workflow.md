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
  - AGENTS.md
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/workflows/docs_checker.yml
---

## Engine-tracked work (Interactor Build)
Every code change goes through a tracked **Goal**:
1. A Goal must exist before any file is edited. Create it in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` + `ibuild engine goal queue <goalId>`.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the default branch `biograph-fh` directly.**
3. The engine opens a single PR per Goal, which must pass review and CI before merging. EngineTasks under a Goal cycle through investigation → execution → review (`ibuild engine work`, `ibuild engine report --yes`, `ibuild engine goal accept`).

An interactive session may toggle the gate with `ibuild off` / `ibuild on` for small changes. The change still goes on its own branch through a hand-opened PR that runs CI.

## Commits and PRs
- **Conventional Commits** are enforced by commitlint on PRs. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test (lower-case, non-empty subject). Scopes are common, e.g. `feat(appointment): ...`, `fix(linters): ...`.
- The PR template asks you to name the target branch, follow the commit convention, run tests locally, keep business logic on the server, update docs, add `closes #XXXX`, and attach screenshots or GIFs for UI changes.
- `feat` PRs need a docs link or `no-docs` (docs checker).
- Mergify auto-merges after ≥1 approval (merge commit by default, squash with the `squash` label, blocked by `dont-merge`). Backports use the labels `backport develop` and `backport version-1x-hotfix`.
- Upstream-style PRs to stable `version-14/15/16` branches are auto-closed for non-maintainers.

## Project rules
`.build/RULES.md` holds the standing rules (currently a template). `AGENTS.md` renders the guide index from `.build/guides/`.
