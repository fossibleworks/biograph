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
  - commitlint.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine):**
- Every code change needs a tracked **Goal**. A GitHub issue becomes a Goal only through an explicit import.
- Work happens on the branch `goal/<goalId>` in an isolated worktree. It ships through that goal's single PR, which must pass review and CI. Never commit directly to the default branch.
- EngineTasks under a Goal cycle through investigation → execution → review.
- CLI: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`.
- An interactive session may use `ibuild off` for a small change, but it must still go through its own branch and a hand-opened PR.

**Branches:**
- The fork's integration branch is **`biograph-fh`**, the default branch for PRs.
- Upstream earthians/marley `version-16` is synced into it in batches with `git cherry-pick -x`. Conflict policy: fork intent wins, and upstream fixes are layered on top. Every pick is recorded in `wiki/upstream-sync-version-16.md`.
- Inherited upstream conventions (Mergify) also apply:
  - `version-14/15/16` are stable branches that only bots or maintainers may target. Other PRs go to `develop` or `version-N-hotfix`.
  - Backports are made with `backport <branch>` labels.
  - Auto-merge after one approval. The `squash` label squash-merges; `dont-merge` blocks.

**Commits and PRs:**
- Conventional Commits (commitlint), for example `fix: …` or `docs(wiki): … (upstream sync B2)`.
- PR body: description, screenshots and `closes #N`. `feat` PRs need a docs link or `no-docs`.
