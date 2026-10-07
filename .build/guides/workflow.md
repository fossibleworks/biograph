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
  - .github/labeler.yml
---

**Work tracking (Interactor Build engine)**, from `CLAUDE.md`:
- Every code change belongs to a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. The engine breaks the Goal into **EngineTasks**, and each task goes through investigation → execution → review.
- **Gate:** before editing any file, a Goal must exist. Work happens on the branch `goal/<goalId>` in an isolated worktree and **never on the main branch**. Changes ship through the Goal's single PR, which must pass review and CI. Direct pushes to the main branch are not allowed.
- Drive the flow from the Build web UI or with `ibuild engine goal-create`, `goal queue`, `work`, `report --yes` and `goal accept`. For a small change, `ibuild off` skips the Goal, but the change still goes through its own branch and a hand-opened PR.

**Branches:** the fork's integration branch is **`biograph-fh`**. Upstream (earthians) uses `develop`, `version-NN-hotfix` and the stable `version-14/15/16`. Mergify there auto-closes PRs against stable branches, merges after one approval and CI, and backports through `backport <branch>` labels.

**Commits:** Conventional Commits, enforced by commitlint (types build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test). Use scopes when they help, for example `fix(linters):`, `feat(appointment):`, `docs(wiki):`. Upstream-sync commits use `git cherry-pick -x` and the `(upstream sync B<n>)` suffix, and their outcomes are logged in the wiki ledger.

**PR expectations:** pre-commit and Semgrep must pass. `feat` PRs need a docs link or `no-docs`. Python changes without tests get the `needs-tests` label. The patch coverage target is 85%.
