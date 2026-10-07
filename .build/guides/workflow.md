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
  - .mergify.yml
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking: the Interactor Build engine** (`CLAUDE.md`)
- Every code change needs a tracked **Goal**. A GitHub issue becomes a Goal only after it is explicitly imported. The engine generates **EngineTasks** under the Goal, and each one goes through investigation → execution → review.
- **Before editing any file:** a Goal must exist. Work on the branch `goal/<goalId>` in an isolated worktree, never on the main branch. Ship through the goal's single PR, which the engine opens and which must pass review and CI.
- From the CLI:
  - `ibuild engine goal-create "<title>"`
  - `ibuild engine goal queue <id>`
  - `ibuild engine work <task>`
  - `ibuild engine report --yes`
  - `ibuild engine goal accept <id>`
- Goals can also be created in the Build web UI.
- `ibuild off` turns the gate off for a small interactive change, but that change still goes through its own branch and a hand-opened PR.

**Branches**
- The fork's main or integration branch is **`biograph-fh`**, which is `origin/HEAD`.
- Goal branches are `goal/<slug>-<id>`.
- Upstream is `earthians/marley` `version-16`, tracked as the `upstream` remote. Sync it by `git cherry-pick -x` in numbered batches, recorded in `wiki/upstream-sync-version-16.md`. On conflict, the fork's intent wins.
- Inherited upstream conventions (`.mergify.yml`):
  - PRs into the stable branches `version-14/15/16` are auto-closed, except from maintainers or bots.
  - Changes go to the `-hotfix` or `develop` branches.
  - Merges are automatic after at least 1 approval and green CI. Use the `squash` label to squash, and `dont-merge` to block.

**Commits and PRs**
- Conventional Commits are enforced by commitlint on PRs. Types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`. Scopes are used, for example `docs(wiki):` and `fix(tests):`. Sync commits carry a suffix such as `(upstream sync B2)`.
- PR template asks for a description, screenshots, docs, `closes #XXXX`, and server-side validation.
- `feat` PRs need a docs link, or `no-docs` in the body.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- Project rules live in `.build/RULES.md`, which is currently an unfilled template. The rendered guide list is in `AGENTS.md`.
