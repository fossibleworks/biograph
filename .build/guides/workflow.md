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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine, from CLAUDE.md)**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. EngineTasks under a Goal cycle through investigation, execution and review.
- Before editing any file: make sure a Goal exists (`ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, or the web UI). Then work on branch **`goal/<goalId>`** in an isolated worktree, **never on the default branch**.
- All changes ship through the Goal's single PR, which the engine opens and which passes review and CI. No direct pushes to the default branch. An interactive session may use `ibuild off` for a small change, but that change still goes on its own branch through a hand-opened PR.
- Project rules live in `.build/RULES.md`, which is mirrored to AGENTS.md, `.claude/rules`, `.cursor/rules` and `.github/instructions`.

**Branches**
- In this fork the default/integration branch is **`biograph-fh`**. Goal branches are `goal/<slug>-<hash>`. `upstream/version-16` (earthians/marley) is the sync source.
- Upstream conventions (Mergify) still apply: no PRs to stable `version-14/15/16`. Use `develop` or the `version-N-hotfix` branches. PRs auto-merge after 1 approval and green CI; the `squash` label gives a squash merge and `dont-merge` blocks merging.

**Commits and PRs**
- Conventional Commit titles (commitlint). Scopes are common (`feat(appointment): …`, `fix(linters): …`). Upstream cherry-picks use `git cherry-pick -x`, and fork follow-ups add a suffix such as `(upstream sync B2)`.
- PR body: problem and details, screenshots, `closes #N`, and a docs link or `no-docs` for `feat` PRs.
- Upstream-sync conflict policy: fork intent wins. Doctype JSON gets a 3-way union of fields. `patches.txt` gets a union.
