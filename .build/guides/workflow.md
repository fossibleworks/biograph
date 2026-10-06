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
  - .github/helper/documentation.py
---

# Workflow

## Engine gate (Interactor Build)
Every code change ships through a tracked **Goal**:
1. A Goal must exist before any file is written. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after it is explicitly imported.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. Never commit to the default branch.
3. All changes ship through the goal's single PR, which the engine opens. It must pass review and CI before it merges.
4. EngineTasks under a Goal cycle through investigation → execution → review. Report with `ibuild engine report --yes`.

Interactive sessions may use `ibuild off` for small changes if the project allows it. The change still goes through its own branch and a hand-opened PR.

## Branches
- Fork default/integration branch: **`biograph-fh`**.
- Upstream (earthians) model: `develop` for features. `version-14/15/16` are stable branches that **auto-close PRs** from non-maintainers (Mergify). `version-N-hotfix` is the hotfix branch. The label `backport develop` triggers a backport.
- Upstream sync: cherry-pick with `git cherry-pick -x` (preserving the upstream sha), apply the "fork intent wins" conflict policy, and record each pick in `wiki/upstream-sync-version-16.md`.

## Commits and PRs
- Conventional commit titles, enforced by commitlint. Release notes drop `chore|ci|test|docs|style` entries.
- `feat` PRs need a docs link or `no-docs` in the body.
- Mergify merges after at least 1 approving review and green CI. Add the `squash` label to squash-merge and `dont-merge` to block merging.
- Code owners: `@akurungadam @Sajinsr`.

## Rules
The source of project rules is `.build/RULES.md`, which is currently an unfilled template. `AGENTS.md`, `.claude/rules/`, `.cursor/rules/` and `.github/instructions/` are generated mirrors.
