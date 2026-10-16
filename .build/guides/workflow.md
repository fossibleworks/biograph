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
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/workflows/semantic-commits.yml
---

- **Interactor Build engine:** every code change needs a tracked **Goal** first. GitHub issues map to Goals only after an explicit import, and the engine generates EngineTasks under each Goal (investigation → execution → review).
  - Work on the goal branch `goal/<goalId>` in an isolated worktree. Never commit to the default branch.
  - All changes ship through the Goal's single PR, which must pass review and CI.
  - CLI: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`.
  - Interactive sessions can run `ibuild off` for a small change, but the change still goes on its own branch with a hand-opened PR.
- **Branches:** the fork's integration branch is `biograph-fh`. Upstream earthians/marley uses `develop` plus stable `version-14/15/16` branches. Mergify auto-closes outside PRs aimed at stable branches; target develop or a hotfix branch instead.
- **Upstream sync:** cherry-pick with `git cherry-pick -x`. Fork intent wins on conflicts. Doctype JSON is merged as a 3-way union of fields and field_order. Each pick is logged in `wiki/upstream-sync-version-16.md`.
- **Commits and PR titles:** Conventional Commits, checked by the semantic-commits workflow.
- **PR body:** follow the PR template. Explain the change, put business logic server-side, update docs, and include `closes #XXXX`. `feat` PRs need a docs link or `no-docs`.
- **Review and merge:** CODEOWNERS are `@akurungadam` and `@Sajinsr`. Mergify merges automatically once there is at least one approval and CI is green. The `squash` label squashes; the `dont-merge` label blocks.
- **Project rules:** in `.build/RULES.md`, still a placeholder template.
