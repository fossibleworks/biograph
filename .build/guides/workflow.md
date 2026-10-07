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
  - .github/helper/install.sh
  - commitlint.config.js
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine, per `CLAUDE.md`)**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import.
- Work happens on the branch `goal/<goalId>` in an isolated worktree. Never commit directly to the main branch.
- Each Goal ships through a single PR that must pass review and CI.
- Commands: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`. Alternatively use the Build web UI.
- For small changes an interactive session may run `ibuild off`. The change still goes on its own branch through a hand-opened PR.

**Branches**
- This fork's integration branch is `biograph-fh`. CI's `install.sh` maps any branch other than `develop` / `version-*` (such as `biograph-fh` and `goal/*`) to Frappe/ERPNext `version-16`.
- Upstream branching (Mergify):
  - Stable branches `version-14/15/16` do not accept PRs; they are auto-closed unless the author is a maintainer or bot.
  - Fixes go to `develop` or `version-N-hotfix`.
  - Backports use the labels `backport develop` and `backport version-N-hotfix`.
  - PRs auto-merge after at least 1 approval. Add the `squash` label for a squash merge, or `dont-merge` to block merging.
- **Upstream sync**: changes from earthians/marley are brought in with `git cherry-pick -x`. The policy is "fork intent wins", and each pick is logged in `wiki/upstream-sync-version-16.md`.

**Commits and PRs**
- Conventional commits (commitlint, `semantic-commits` workflow).
- Fill in the PR template: problem details, screenshots, and `closes #XXXX`.
- `feat` PRs need a docs link or the text `no-docs` in the body.
- CODEOWNERS: @akurungadam and @Sajinsr.

`.build/RULES.md` is the project-rules source. It is currently an unfilled template.
