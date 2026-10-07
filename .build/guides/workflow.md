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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/workflows/labeller.yml
---

- **The Interactor Build engine tracks all work.** A **Goal** (from the Build web UI, `ibuild engine goal-create`, or an imported GitHub issue) owns one branch, `goal/<goalId>`, and one PR. EngineTasks under the Goal cycle through investigation → execution → review.
- **The gate:** before editing any file, a tracked Goal must exist. Work happens on `goal/<goalId>` in an isolated worktree, **never on `main`/`biograph-fh` directly**, and changes ship only through the goal's PR, which must pass review and CI. Small interactive changes may use `ibuild off`, but they still land through a hand-opened PR on their own branch.
- **Default branch:** `biograph-fh`. Stable upstream-style branches are `version-14/15/16`. Mergify auto-closes PRs from non-maintainers targeting those branches. It auto-merges PRs with ≥1 approval and passing CI, with a `squash` label variant and a `dont-merge` label to block merging.
- **Commit messages** follow Conventional Commits, enforced by commitlint and the Semantic Commits workflow. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case. Upstream sync commits add a suffix such as `(upstream sync B2)` and use `git cherry-pick -x`.
- **Upstream syncs** from `earthians/marley` follow the ledger in `wiki/upstream-sync-version-16.md`: fork behaviour wins, DocType JSON is a 3-way union, and `patches.txt` is a union.
- **PRs:** follow the PR template (details, screenshots, `closes #XXXX`, server-side validation, docs updated). The labeler workflow applies labels automatically.
