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
  - .github/instructions/build-rules.instructions.md
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Interactor Build engine (this fork, from CLAUDE.md):**
- Every code change belongs to a tracked **Goal**. A GitHub issue maps to a Goal only after it is explicitly imported. The engine generates **EngineTasks** under the Goal, and each task goes through investigation → execution → review.
- **The gate:** with no Goal, no edits. Create a Goal (web UI at build.interactor.com, or `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`). Then work on branch **`goal/<goalId>`** in an isolated worktree. Never commit directly to the default branch **`biograph-fh`**.
- The engine opens a single PR per Goal, and that PR must pass review and CI. Use `ibuild engine work <task>` / `ibuild engine report --yes` to work and report phases, and `ibuild engine goal accept <goalId>` to deliver.
- An interactive session may run `ibuild off` for a small change. That change still goes on its own branch through a hand-opened PR that runs CI.
- Standing AI rules come from `.build/RULES.md`, which is mirrored into `.claude/rules/build-rules.md`, `.github/instructions/build-rules.instructions.md` and `AGENTS.md`. Edit the source file, not the mirrors.

**Commits and PRs:**
- Conventional Commits, checked by commitlint on every PR.
- Upstream cherry-picks use `git cherry-pick -x` and are recorded in `wiki/upstream-sync-version-16.md`. The conflict policy there is "fork intent wins" (union of DocType `fields` / `field_order` and of `patches.txt`; keep the fork's `.releaserc`).
- PR template: pick the target branch, follow commit conventions, run tests locally, keep validations server-side, update docs, and add `closes #XXXX`.

**Inherited upstream rules (Mergify, CODEOWNERS):**
- PRs to stable `version-14/15/16` branches are auto-closed unless the author is on the allow-list. Target a hotfix or develop branch instead.
- Auto-merge needs ≥1 approval and no `dont-merge` label. The `squash` label selects squash merge.
- The default code owners are @akurungadam and @Sajinsr.
