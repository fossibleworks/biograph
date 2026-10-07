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
  - commitlint.config.js
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/helper/install.sh
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Workflow

## Work tracking: Interactor Build engine
`CLAUDE.md` defines the contract.
- Every change belongs to a tracked **Goal**, created in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`.
- A Goal owns **one branch `goal/<goalId>`** and **one PR**. Work happens in an isolated worktree, never on the main branch.
- EngineTasks beneath a Goal cycle through investigation → execution → review. Report with `ibuild engine report --yes` and deliver with `ibuild engine goal accept <goalId>`.
- A GitHub issue becomes a Goal only after an explicit import.
- The gate can be turned off for a small interactive change with `ibuild off`. The change still lands on its own branch through a PR that runs CI.
- Standing rules live in `.build/RULES.md`. It is mirrored to `.claude/rules/build-rules.md` and `.github/instructions/build-rules.instructions.md` and is still a template. `AGENTS.md` lists the guides.

## Branches
- **Fork default/integration branch: `biograph-fh`.** Goal branches PR into it.
- Upstream (earthians/marley) uses `develop`, `version-14/15/16` (stable) and `version-N-hotfix` branches.
  - Mergify auto-closes PRs to stable `version-*` branches from non-maintainers.
  - Backports go through labels such as `backport develop` and `backport version-16-hotfix`.
- CI's `install.sh` maps fork branches (`biograph-fh`, `goal/*`) to Frappe/ERPNext `version-16`.

## Commits and PRs
- **Conventional Commits**, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lower-case.
- Scopes are common, e.g. `fix(tests): ...`, `docs(wiki): ...`.
- Upstream sync commits add a suffix such as `(upstream sync B2)` and use `git cherry-pick -x`.
- PR template: explain the problem and details, add screenshots, keep logic server-side, update docs, and use `closes #N`.
- Merges: Mergify merges once there is at least 1 approval (squash with label `squash`, block with `dont-merge`).
- CODEOWNERS: @akurungadam @Sajinsr.
