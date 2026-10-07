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
  - .github/workflows/semantic-commits.yml
  - .github/CODEOWNERS
---

Work is tracked through **Interactor Build's engine** (see `CLAUDE.md`).

- **The gate:** before writing any file, a tracked **Goal** must exist. Create it in the Build web UI, with `ibuild engine goal-create '<title>'` + `ibuild engine goal queue <goalId>`, or by importing a GitHub issue. EngineTasks under the Goal go through investigation → execution → review.
- **Branching:** work on `goal/<goalId>` in an isolated worktree. Never commit directly to the default branch **`biograph-fh`** (or `main`).
- **Delivery:** each Goal ships as one PR, which must pass the review and CI gates. `ibuild engine goal accept <goalId>` delivers it after merge. For small changes, a session can run `ibuild off` and land them on their own branch through a hand-opened PR that runs CI.
- **Commits:** use Conventional Commits, checked by commitlint in `semantic-commits.yml`.
- **Upstream sync:** pull earthians/marley changes in with `git cherry-pick -x`. The fork's behaviour wins conflicts, and each pick is logged in `wiki/upstream-sync-version-16.md`.
- **Merging rules (Mergify):** a PR merges automatically once CI passes and it has 1 approval. The `squash` label makes it squash-merge and the `dont-merge` label blocks merging. PRs to stable `version-1x` branches from non-maintainers are closed automatically, so use develop or hotfix branches.
- PRs are labelled automatically (`labeler.yml`), and code owners are listed in `.github/CODEOWNERS`.
