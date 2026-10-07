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
  - .build/RULES.md
  - commitlint.config.js
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

This repo is driven by **Interactor Build's engine** (see `CLAUDE.md`):

1. **A Goal must exist before any code edit.** Create it in the Build web UI or with `ibuild engine goal-create "<title>"`, then admit it with `ibuild engine goal queue <goalId>`. GitHub issues become Goals only after an explicit import.
2. Work on the goal branch **`goal/<goalId>`** in an isolated worktree. Never commit to the default branch **`biograph-fh`** directly. Existing remote branches follow this, e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-…`.
3. Each Goal ships as **one PR**. EngineTasks under the Goal go through investigation → execution → review (`ibuild engine work` / `report --yes`, then `goal accept`).
4. Interactive sessions may use `ibuild off` for small changes. Those still go on their own branch with a hand-opened PR.

**Commits:** Conventional Commits, enforced by commitlint on PRs.
- During upstream syncs, suffix the subject with the batch, e.g. `(upstream sync B2)`.
- Cherry-pick with `git cherry-pick -x`.
- Resolve conflicts with *fork intent wins*.

**PRs:** follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`:
- Explain the problem.
- Tests pass.
- Server-side validations.
- Update docs.
- `closes #N`.

`feat` PRs need a docs link or `no-docs`. Mergify auto-merges after one approval (add the `squash` label to squash; `dont-merge` blocks) and closes PRs aimed at stable `version-*` branches from non-maintainers. CODEOWNERS: @akurungadam, @Sajinsr.

Project standing rules live in `.build/RULES.md` (currently unfilled) and are mirrored to `.claude/rules/build-rules.md` and `.github/instructions/`. Edit the source, not the mirrors.
