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

# Workflow

## Work tracking (Interactor Build engine)
This repo is connected to Interactor Build (`CLAUDE.md`):
1. **No Goal, no edits.** Every change needs a tracked **Goal**, created in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`.
2. Work on the branch **`goal/<goalId>`** in an isolated worktree, **never on the default branch**.
3. Changes ship through the **Goal's single PR**, which the engine opens and which must pass review and CI. Each EngineTask under a Goal cycles through investigation → execution → review.
4. An interactive session may run `ibuild off` for a small change. That change still goes on its own branch with a hand-opened PR that runs CI.

Standing rules are in `.build/RULES.md` (currently a placeholder template).

## Branching (upstream conventions)
- `develop` is the integration branch. `version-14|15|16-hotfix` are hotfix branches. `version-14|15|16` are stable branches. Mergify **auto-closes PRs to stable branches** from non-maintainers.
- Backports are done by adding a label (`backport develop`, `backport version-15-hotfix`, …), which Mergify handles.
- Mergify merges after ≥1 approval and passing CI. The `squash` label squashes, and `dont-merge` blocks merging.
- In this fork, the checked-out default branch is `biograph-fh`.

## Commits and PRs
- Use conventional commit titles (commitlint on every PR): `feat: …`, `fix: …`, etc.
- `feat` PRs need a wiki docs link or `no-docs` in the body.
- Fill in the PR template: details of the change, screenshots, `closes #NNN`.
- Default code owners are `@akurungadam @Sajinsr`.
