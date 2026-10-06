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
  - .github/CODEOWNERS
  - commitlint.config.js
---

## Work tracking: Interactor Build engine
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import.
- Goals are created in the Build web UI or with `ibuild engine goal-create "<title>"`.
- The engine breaks a Goal into EngineTasks. Each task goes through investigation → execution → review.

## Branching
- Work on `goal/<goalId>` in an isolated worktree. Never commit directly to the integration branch.
- This fork's main branch is **`biograph-fh`**.
- Every change ships through the goal's single PR, which must pass review and CI.
- For a small change, an interactive session may run `ibuild off`. The change still goes on its own branch through a hand-opened PR that runs CI.

## Upstream relationship
- Upstream `earthians/marley` (remote `upstream`) uses `develop`, plus `version-14/15/16` stable branches and `version-*-hotfix` branches.
- Mergify auto-closes PRs against stable branches from non-maintainers. It auto-merges after one approval (`label!=dont-merge`) and squashes when the `squash` label is set.
- Sync from upstream with `git cherry-pick -x` under the "fork intent wins" policy, and log every batch in the wiki ledger.

## Commits and PRs
- Use conventional commits (commitlint), with a scope where useful.
- `feat` PRs need a docs link or `no-docs`.
- CODEOWNERS are `@akurungadam` and `@Sajinsr`.
- Use the issue templates for bugs and feature requests.
