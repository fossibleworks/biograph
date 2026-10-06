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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - commitlint.config.js
---

**Build engine gate (this fork):**
1. Every code change needs a tracked **Goal** in Interactor Build. A GitHub issue maps to a Goal only after an explicit import. Create the Goal in the web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`.
2. Work on the branch **`goal/<goalId>`** in an isolated worktree. **Never commit directly to the default branch `biograph-fh`** (or `main`).
3. Every change ships through the Goal's **single PR**, which must pass review and CI. Under each Goal, EngineTasks go through investigation → execution → review (`ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <goalId>`).
4. An interactive session may use `ibuild off` for a small change, but it still needs its own branch and a hand-opened PR.

**Branches (inherited from upstream earthians):** `develop` is the integration branch. `version-14/15/16` are stable branches, `version-XX-hotfix` are hotfix branches. Mergify auto-closes outside PRs against stable branches. Backports use the labels `backport develop` and `backport version-XX-hotfix`. Mergify auto-merges after one approval (merge commit, or squash with the `squash` label; `dont-merge` blocks it).

**Commits and PRs:** Conventional Commits, checked by commitlint on every PR. Fork upstream-sync work uses `git cherry-pick -x` and suffixes like `(upstream sync B2)`, and is logged in `wiki/upstream-sync-version-16.md`. The PR template asks you to pick the right base branch, have tests passing, keep validations server-side, update docs, and write `closes #XXXX`. CODEOWNERS: `@akurungadam @Sajinsr`.
