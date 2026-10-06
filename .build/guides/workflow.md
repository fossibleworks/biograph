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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
  - .build/RULES.md
---

**Work tracking (Interactor Build engine, per `CLAUDE.md`):**
- Every code change needs a tracked **Goal** first. Create one in the Build web UI, with `ibuild engine goal-create "<title>"`, or by importing a GitHub issue.
- Each Goal owns a single branch, **`goal/<goalId>`**, worked in an isolated worktree, and a **single PR** opened by the engine. The engine breaks Goals into EngineTasks, and each task goes through investigation → execution → review.
- Never commit or push directly to the default branch **`biograph-fh`**. For small changes in an interactive session, `ibuild off` is allowed, but the change still goes through its own branch and a PR.
- Project rules: `.build/RULES.md`, mirrored to `.claude/rules/` and `.github/instructions/`. Guides go in `.build/guides/`, indexed in `AGENTS.md`.

**Commits:** Conventional Commits, enforced by commitlint on PRs. Allowed types are `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, all lowercase, and the subject is required. Scopes are common (`fix(tests): ...`, `docs(wiki): ...`). Upstream-sync work adds a suffix such as `(upstream sync B2)`.

**Upstream sync:** pull upstream earthians/marley `version-16` commits with `git cherry-pick -x`. On conflict, the fork's intent wins (union DocType `fields`/`field_order`, union `patches.txt`, keep the fork's `.releaserc`). Log each commit's outcome in `wiki/upstream-sync-version-16.md`.

**Review:** CODEOWNERS are `@akurungadam` and `@Sajinsr`. Mergify (an upstream config) auto-closes PRs against the `version-1x` stable branches unless the author is a maintainer or bot. It auto-merges after one approval and green CI unless the PR is labelled `dont-merge` or `squash`.
