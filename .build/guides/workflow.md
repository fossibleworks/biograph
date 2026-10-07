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
  - commitlint.config.js
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine, see `CLAUDE.md`):**
- Every code change needs a tracked **Goal** first. Create it in the Build web UI or with `ibuild engine goal-create "<title>"`, then admit it with `ibuild engine goal queue <goalId>`.
- Work happens on branch **`goal/<goalId>`** in an isolated worktree, **never on the default branch**.
- The engine splits a Goal into EngineTasks. Each task cycles through investigation, execution and review.
- Each goal ships through a **single PR** that must pass review and CI. Only an interactive session the project allows may bypass this with `ibuild off`, and even then it needs its own branch and a hand-opened PR.
- Standing rules live in `.build/RULES.md`. It is currently an unfilled template.

**Branches:**
- The fork's default/integration branch is **`biograph-fh`**. The upstream is `earthians/marley` `version-16`, added as the `upstream` remote.
- Inherited upstream config still refers to `develop`, `version-14/15/16` and `version-*-hotfix`. Mergify auto-closes PRs against stable `version-*` branches from non-maintainers.

**Commits:**
- Use Conventional Commits, checked by commitlint. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case, with a non-empty subject.
- Recent history adds a scope or context suffix, for example `fix: drop unused imports left by upstream aeca803f (upstream sync B2)` and `docs(wiki): ...`.

**Upstream sync:**
- Use `git cherry-pick -x` so every pick records its upstream sha.
- Conflict policy is **fork intent wins**: keep biograph-fh behaviour and add upstream's fix on top.
- DocType JSON gets a 3-way union. `patches.txt` gets a union. Keep the fork's `.releaserc`.
- Record every pick in `wiki/upstream-sync-version-16.md`.

**Review:**
- CODEOWNERS is `@akurungadam @Sajinsr`.
- Mergify auto-merges after 1 approval and CI success; the `squash` label squashes and `dont-merge` blocks.
- The PR template asks for: target branch, conventional title, passing tests, server-side business logic, docs, and `closes #XXXX`.
