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
  - .github/CODEOWNERS
  - commitlint.config.js
---

**Work tracking (Interactor Build engine), per CLAUDE.md**
- Every code change needs a tracked **Goal** first. Create one in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` + `ibuild engine goal queue <goalId>`. The engine generates **EngineTasks** under the Goal, and each task goes through investigation → execution → review.
- Work happens on branch **`goal/<goalId>`** in an isolated worktree, **never on the default branch**. All changes ship through the goal's single PR, which must pass review and CI.
- For small changes, an interactive session may run `ibuild off` if the project allows it. The change still goes on its own branch with a hand-opened PR.
- Standing rules live in `.build/RULES.md` (still a placeholder). It is mirrored to `AGENTS.md`, `.claude/rules/`, `.cursor/rules/` and `.github/instructions/`.

**Branches**
- The fork's default/integration branch is **`biograph-fh`**. Upstream (`earthians/marley`) uses `develop` plus stable `version-14/15/16`, with `version-*-hotfix` branches.
- Mergify auto-closes PRs against stable `version-*` branches unless they come from maintainers or bots, and auto-merges once there is ≥1 approval and CI passes. The `squash` label switches the merge to squash, and `dont-merge` blocks it.
- CODEOWNERS: `@akurungadam @Sajinsr` own everything.

**Commits**
- Conventional Commits, enforced by commitlint on PRs. Types are `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, lower-case, with an optional scope, for example `feat(appointment): ...` or `docs(wiki): ... (upstream sync B2)`.
- Upstream cherry-picks use `git cherry-pick -x` and the conflict policy "fork intent wins". Doctype JSON is a 3-way union of `fields`/`field_order`, and `patches.txt` is a union. Each pick is logged in `wiki/upstream-sync-version-16.md`.
- PR titles starting with `feat` need a docs link or `no-docs` in the body.
