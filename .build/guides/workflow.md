---
title: Work-tracking and branching workflow
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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/helper/install.sh
---

**Interactor Build engine (CLAUDE.md, required):**
1. A tracked **Goal** must exist before any file is edited. Create one in the Build web UI or with `ibuild engine goal-create "<title>"` and `ibuild engine goal queue <goalId>`. GitHub issues become Goals only through an explicit import.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. Never work on the default branch.
3. Changes ship through the Goal's single PR. The engine opens it, and it must pass review and CI before merge. No direct pushes.
4. Each EngineTask goes through investigation → execution → review. Report phases with `ibuild engine work` / `ibuild engine report --yes`.
   An interactive session may run `ibuild off` for a small change. That change still goes on its own branch with a hand-opened PR.

**Branches:**
- **`biograph-fh`** is this fork's main and integration branch, and the target of goal PRs.
- The upstream-style branches `develop`, `version-14|15|16` (stable) and `version-*-hotfix` are referenced by the inherited workflows. Mergify auto-closes PRs against stable `version-*` branches from non-maintainers. Use hotfix or develop instead. Backports are driven by `backport <branch>` labels.
- **Upstream sync:** cherry-pick from `earthians/marley` `version-16` with `git cherry-pick -x`. The conflict policy is "fork intent wins" (union doctype `fields` and `field_order`, union `patches.txt`, keep the fork's `.releaserc` and version). Log every commit's outcome in `wiki/upstream-sync-version-16.md`.

**Commits and PRs:**
- Conventional Commits are required (commitlint): `fix: ...`, `feat: ...`, `docs(wiki): ...`, with optional scope.
- Follow the PR template. State the target branch, explain the problem, include screenshots or GIFs, use `closes #XXXX`, and keep logic server-side.
- Merging needs at least 1 approving review (Mergify). The `squash` label switches to a squash merge, and `dont-merge` blocks merging. CODEOWNERS: `@akurungadam @Sajinsr`.
