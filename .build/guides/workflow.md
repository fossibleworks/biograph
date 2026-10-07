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
  - .mergify.yml
  - commitlint.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

**Work tracking: Interactor Build engine** (`CLAUDE.md`)
- Every code change needs a tracked **Goal** first, created in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"`. A Goal owns one branch and one PR. The engine generates **EngineTasks** under it, and each task cycles through investigation → execution → review.
- Work only on **`goal/<goalId>`** branches, in an isolated worktree. Never commit or push directly to the default branch **`biograph-fh`**.
- All changes ship through the goal's PR, which must pass review and CI gates. A small change may skip the Goal with `ibuild off` if the project allows it, but it still goes through a hand-opened PR on its own branch.
- Standing rules live in `.build/RULES.md` (currently a placeholder) and are mirrored in `.claude/rules/build-rules.md` and `.github/instructions/build-rules.instructions.md`.

**Branching model** (inherited from upstream)
- Upstream development happens on `develop`. Stable branches are `version-14/15/16` with matching `version-N-hotfix` branches. Mergify **auto-closes PRs against stable branches** unless they come from maintainers or bots. Mergify auto-merges PRs that have at least one approval, passing CI, and no `dont-merge`/`squash` label.
- Fork: `biograph-fh` is the integration branch. Upstream (`earthians/marley` `version-16`) is synced with `git cherry-pick -x` in batches. Conflict policy: **fork intent wins**. Every pick is recorded in `wiki/upstream-sync-version-16.md`.

**Commits and PRs**
- Conventional Commits, checked by commitlint on every PR, e.g. `fix: …`, `feat: …`, `docs(wiki): …`, `chore(release): …`.
- PR template: choose the target branch, follow the commit convention, make sure tests pass, keep logic server-side, update docs, and add `closes #XXXX`. Include screenshots for UI changes.
- CODEOWNERS: `@akurungadam @Sajinsr` own everything.
- Bug and feature issues use the YAML issue forms in `.github/ISSUE_TEMPLATE/`.
