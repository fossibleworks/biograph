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
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Workflow

## Work tracking (Interactor Build engine)
- Every code change starts from a tracked **Goal**. A GitHub issue becomes a Goal only after an explicit import.
- The engine creates EngineTasks under the Goal. Each task goes through investigation → execution → review.
- Create Goals from the Build web UI or with `ibuild engine goal-create "<title>"`, then admit them with `ibuild engine goal queue <goalId>`.
- **Before editing**, make sure a Goal exists, then work on branch **`goal/<goalId>`** in an isolated worktree. Never edit on the trunk.
- Each Goal ships through **one PR**, which must pass review and CI. Do not push directly to the trunk.
- `ibuild off` is allowed only for small changes in interactive sessions. Those changes still go through a hand-opened PR.

## Branches
- The trunk for this fork is **`biograph-fh`**. Goal branches are `goal/<slug>-<id>`.
- Upstream marley `version-16` changes come in through `git cherry-pick -x` batches, recorded in `wiki/upstream-sync-version-16.md`. Fork intent wins conflicts, and `patches.txt` is merged as a union.
- The upstream release model uses `develop`, `version-NN-hotfix` and `version-NN`. Mergify auto-closes PRs from non-maintainers that target `version-14/15/16`.

## Commits and PRs
- Use Conventional Commits, enforced by commitlint. Types are `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case. Scope is optional (`fix(tests): ...`, `docs(wiki): ...`). The sync-batch context goes in a parenthetical suffix, for example `(upstream sync B2)`.
- Follow the PR template: explain the problem and the details, add screenshots for UI changes, put business logic on the server, and add `closes #N`.
- `feat` PRs need a docs link (see docs checker). The `dont-merge` and `squash` labels control Mergify's merge method, and merging needs at least one approval.
- CODEOWNERS: @akurungadam, @Sajinsr.
- `.build/RULES.md` holds the project rules. It is mirrored into `.claude/rules`, `.github/instructions` and `AGENTS.md`. Edit only the source file.
