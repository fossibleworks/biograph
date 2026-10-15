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
  - commitlint.config.js
  - .github/CODEOWNERS
---

**This fork (fossibleworks/biograph → fossibleHIS)** is driven by **Interactor Build**:
- Every code change needs a tracked **Goal** first. Create one in the Build web UI, through an imported GitHub issue, or with `ibuild engine goal-create "<title>"`.
- Work on the branch **`goal/<goalId>`** in an isolated worktree. Never commit to the default branch `biograph-fh` directly.
- Each Goal ships as one PR opened by the engine. The PR must pass review and CI before merge. EngineTasks under a Goal cycle through investigation → execution → review.
- For a small change, an interactive session may run `ibuild off`. The change still goes on its own branch through a hand-opened PR.
- Project rules live in `.build/RULES.md`, which is mirrored to the `.claude`, `.cursor`, `.github/instructions` and `AGENTS.md` copies.

**Upstream conventions (still present in config):**
- Conventional Commit titles are enforced by commitlint.
- The PR template asks contributors to choose the right base branch, explain the change, attach screenshots, put all business logic server-side, update docs and include `closes #NNN`.
- Upstream branches are `develop` plus the stable `version-14/15/16` branches and their `-hotfix` branches. Mergify auto-closes PRs against stable branches. It auto-merges after one approval, or squashes if the PR has the `squash` label. Labels like `backport version-15-hotfix` trigger backports.
- CODEOWNERS sets the default reviewers to @akurungadam and @Sajinsr.
