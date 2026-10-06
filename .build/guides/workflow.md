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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Work is tracked through **Interactor Build** (the engine), as set out in `CLAUDE.md`.

- **Goal first.** Every code change needs a tracked **Goal**, which maps to a GitHub issue after import. Create one with the Build web UI or `ibuild engine goal-create "<title>"` and admit it with `ibuild engine goal queue <goalId>`. EngineTasks under the Goal move through investigation, then execution, then review.
- **Branching.** Work on `goal/<goalId>` in an isolated worktree. Never commit to the integration branch **`biograph-fh`** (this fork's default) directly. Each Goal has one PR targeting `biograph-fh`, opened by the engine, which merges after review and CI. A small interactive change may use `ibuild off` but still needs its own branch and a hand-opened PR.
- **Commits.** Use Conventional Commits, enforced by the `Semantic Commits` workflow (commitlint). Add a parenthetical context where useful, for example `fix: ... (upstream sync B2)` or `docs(wiki): ...`.
- **Upstream sync.** Cherry-pick from `earthians/marley version-16` with `git cherry-pick -x`, in numbered batches. Fork intent wins. Record every commit's outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped or deferred) in `wiki/upstream-sync-version-16.md`.
- **PR content** (template): details of the problem and fix, screenshots, a docs link (or `no-docs`) for `feat`, and `closes #N`. Business logic goes server-side.
- **Inherited upstream rules** (Mergify and CODEOWNERS): PRs to stable `version-14/15/16` from non-maintainers are auto-closed; target develop or hotfix. A merge needs at least 1 approval, and the `squash` label squashes. CODEOWNERS is `@akurungadam @Sajinsr`.
- Project rules live in `.build/RULES.md`, which is still mostly placeholders.
