---
title: Work-tracking & branching workflow
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
  - .mergify.yml
  - .github/CODEOWNERS
  - commitlint.config.js
---

**This fork (fossibleworks/biograph) is driven by Interactor Build's engine.**

- Each change belongs to a tracked **Goal** (a GitHub issue maps to a Goal, and only an explicit import turns an issue into one). The engine creates **EngineTasks** under the Goal. Each task cycles through investigation → execution → review.
- **The gate:** before writing any file, (1) a Goal must exist, (2) work happens on branch `goal/<goalId>` in an isolated worktree and **never on the default branch `biograph-fh`**, (3) changes ship only through the Goal's single PR, which must pass review and CI. No direct pushes.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. The web UI at build.interactor.com always works. For a small change, an interactive session may run `ibuild off`, but the change still goes on its own branch through a hand-opened PR.
- Standing rules come from `.build/RULES.md` (currently a template). `.build/guides/` is rendered into `AGENTS.md`. Local engine state lives in `.goals/` and `.tasks/` (untracked).

**Upstream syncs** from earthians/marley use `git cherry-pick -x`, in batches (B1, B2, …). Each sync is logged in `wiki/upstream-sync-version-16.md` under the policy "fork intent wins": union doctype JSON fields, union `patches.txt`, keep the fork's `.releaserc`.

**Inherited upstream conventions** that still apply: Conventional Commit titles (commitlint), the PR template checklist (target branch, tests pass, server-side validation, docs, `closes #N`), and labels (`squash`, `dont-merge`, `backport <branch>`, `needs-tests`). `.mergify.yml` and CODEOWNERS (@akurungadam, @Sajinsr) reflect upstream's `develop`/`version-N-hotfix` model. Upstream auto-closes PRs against stable `version-*` branches.
