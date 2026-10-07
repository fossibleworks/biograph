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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
---

This repo is driven by **Interactor Build** (see `CLAUDE.md`).

- **Gate:** no file edits without a tracked **Goal**. Create one in the Build web UI, from an imported GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`. EngineTasks under a Goal go through investigation, then execution, then review.
- **Branching:** work on `goal/<goalId>` in an isolated worktree, never on the default branch **`biograph-fh`**. Each Goal ships as one PR into `biograph-fh`. Don't push directly. For an interactive small change, `ibuild off` is allowed, but it still needs its own branch and a hand-opened PR.
- **Commits:** Conventional Commits, enforced by commitlint (`build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`, lowercase type, non-empty subject). Recent history adds a context suffix, for example `fix: drop unused imports left by upstream aeca803f (upstream sync B2)` or `docs(wiki): ...`.
- **Upstream sync:** take earthians/marley fixes with `git cherry-pick -x` and record every commit in `wiki/upstream-sync-version-16.md` with the outcome vocabulary picked-clean / picked-with-conflict-resolution / already-present / skipped. Fork behaviour wins.
- **Inherited upstream process** (Mergify): PRs to the stable `version-14/15/16` branches are auto-closed unless a maintainer opens them. Target `develop` or a `version-N-hotfix` branch. Merging needs at least 1 approval. The `squash` label squash-merges and `dont-merge` blocks. The `backport develop` label backports. CODEOWNERS: @akurungadam @Sajinsr.
- **Rules:** `.build/RULES.md` (also in `.claude/rules/` and `.cursor/rules/`) is currently an unfilled template.
