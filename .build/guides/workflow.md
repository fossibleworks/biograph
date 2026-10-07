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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
---

- **Interactor Build engine.** Every code change needs a tracked **Goal**, created via the build.interactor.com UI or `ibuild engine goal-create`. Work happens on branch `goal/<goalId>` in an isolated worktree, never on the main branch `biograph-fh`, and ships through the Goal's single PR, which must pass review and CI. GitHub issues map to Goals only after an explicit import. EngineTasks under a Goal cycle through investigation → execution → review. `ibuild off` is allowed only for small interactive changes, which still go through a hand-opened PR.
- **Commits** use Conventional Commits, enforced by commitlint and `semantic-commits.yml`. Batch work carries a scope suffix, e.g. `fix: ... (upstream sync B2)`.
- **Upstream sync** cherry-picks from `earthians/marley version-16` with `git cherry-pick -x`. Conflicts are resolved so the fork's intent wins, with a 3-way union of doctype JSON `fields` and a union of `patches.txt`. Each pick is logged in the wiki ledger.
- **Review and merge.** Owners are @akurungadam and @Sajinsr (CODEOWNERS). Mergify auto-merges after one approval and green CI; the `squash` label means squash-merge and `dont-merge` blocks merging. Mergify also closes PRs against the stable `version-*` branches; use hotfix or develop branches instead.
