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
  - .github/instructions/build-rules.instructions.md
  - .mergify.yml
  - .github/helper/install.sh
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - commitlint.config.js
---

**Work tracking: the Interactor Build engine** (from `CLAUDE.md`)
- Every code change belongs to a tracked **Goal**. A GitHub issue maps to a Goal after it is explicitly imported. The engine generates **EngineTasks** under the Goal, and each one cycles through investigation, execution and review.
- **Gate:** reading code is always fine, but before writing any file there must be a Goal. Work happens on branch **`goal/<goalId>`** in an isolated worktree, **never on the main branch**. Changes ship through the goal's single PR, which the engine opens. That PR must pass review and CI before it merges.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. The web UI is at build.interactor.com.
- An interactive session may run `ibuild off` for a small change (if the project allows it). The change must still go on its own branch with a hand-opened PR that runs CI.
- Standing rules come from `.build/RULES.md`, which is mirrored in `.claude/rules/build-rules.md` and `.github/instructions/build-rules.instructions.md`. Guides are listed in `AGENTS.md`, inside a managed block that must not be edited by hand.

**Branches**
- The fork's integration branch is **`biograph-fh`**. Goal branches are `goal/*`.
- Upstream convention (inherited from earthians): `develop`, the stable branches `version-14/15/16`, and the `version-XX-hotfix` branches. Mergify **auto-closes PRs against stable branches** from non-maintainers and supports `backport <branch>` labels.
- **Upstream sync:** cherry-pick from `earthians/marley` `version-16` with `git cherry-pick -x`, work in numbered batches (B1, B2, ...), and resolve conflicts in favour of the fork's intent. Record each batch in `wiki/upstream-sync-version-16.md`.

**Commits and PRs**
- Conventional Commits (commitlint), with optional scopes and a trailing context in parentheses, for example `fix: ... (upstream sync B2)`.
- Follow the PR template: explain the change, add screenshots, and put `closes #NNN` in the body. `feat` PRs need a docs link or `no-docs`.
- Mergify merges after at least one approval and green CI. It uses a merge commit by default, or a squash when the PR has the `squash` label. The `dont-merge` label blocks merging.
