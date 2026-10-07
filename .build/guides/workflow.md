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
  - .github/workflows/semantic-commits.yml
  - .github/CODEOWNERS
---

- **Interactor Build engine:** every code change needs a tracked **Goal** first. Create it in the web UI, with `ibuild engine goal-create`, or by importing a GitHub issue; an issue alone does not create a Goal. Work happens on branch `goal/<goalId>` in an isolated worktree and **never on the integration branch**. Each change ships through the goal's single PR, which must pass review and CI. EngineTasks under a Goal cycle through investigation, execution and review. An interactive session may use `ibuild off` for small changes, but the change still goes through a hand-opened PR.
- **Branches:** the fork's integration or default branch is `biograph-fh`. Upstream (`earthians/marley` and `biograph`) uses `develop`, with `version-14/15/16` stable branches and `version-N-hotfix` branches. Mergify auto-closes PRs aimed directly at stable branches by non-maintainers.
- **Merging:** Mergify merges once there is ≥1 approval and CI is green, unless the PR is labelled `dont-merge`. The `squash` label makes it squash-merge.
- **Commits:** Conventional Commits, enforced by commitlint in `semantic-commits.yml`. Use `git cherry-pick -x` for upstream sync, with fork intent winning conflicts.
- **Project rules** live in `.build/RULES.md`, which is currently a placeholder. Build mirrors it into `AGENTS.md` and `.github/instructions`.
- **CODEOWNERS** and the labeler (`needs-tests`) apply to PRs.
