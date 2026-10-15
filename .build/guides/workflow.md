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
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

## Work tracking (Interactor Build engine)

- Every code change belongs to a tracked **Goal** in Interactor Build. A GitHub issue maps to a Goal only after an explicit import.
- The engine generates **EngineTasks** under the Goal. Each task goes through investigation → execution → review.
- **The gate:** before writing any file, a Goal must exist. Work then happens on branch **`goal/<goalId>`** in an isolated worktree, never on the default branch, and ships through the goal's single PR. Direct pushes to the default branch are not allowed.
- CLI commands:
  - `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <id>`
  - `ibuild engine work <task>`, then `ibuild engine report --yes`
  - `ibuild engine goal accept <id>`
- For small changes, an interactive session may run `ibuild off`. The change still goes on its own branch through a hand-opened PR with CI.
- Standing rules are in `.build/RULES.md`, which is mirrored to `.claude/rules`, `.cursor/rules` and `.github/instructions`.

## Branches

- **This fork's default/integration branch is `biograph-fh`.** Goal branches are `goal/<slug>-<id>`.
- Upstream conventions are inherited in `.mergify.yml` and the workflows: `develop`, `version-14/15/16` stable, and `version-N-hotfix`.
  - Mergify auto-closes PRs against stable branches and supports `backport <branch>` labels.
  - Upstream auto-merges after one approval. The `squash` label selects squash merge, and `dont-merge` blocks merging.

## Commits & PRs

- **Conventional Commits** are enforced by commitlint. Allowed types are `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, lowercase, with a non-empty subject.
- Follow the PR template:
  - Explain the problem being solved, and add screenshots/GIFs for UI changes.
  - Make sure tests pass and keep business logic server-side.
  - Update docs, and use `closes #N` to link issues.
- `feat:` PRs need a docs link or `no-docs` in the body.
- CODEOWNERS (upstream) is `@akurungadam @Sajinsr`.
