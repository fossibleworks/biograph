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
  - .github/CODEOWNERS
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine):**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. EngineTasks under a Goal cycle through investigation, execution and review.
- Work on the branch `goal/<goalId>` in an isolated worktree. **Never commit or push directly to the main branch (`biograph-fh`).** The engine opens a single PR per Goal, and it merges only after review and CI pass.
- Drive the engine with `ibuild engine goal-create`, `goal queue`, `work`, `report --yes` and `goal accept`, or through the Build web UI. `ibuild off` is only for small interactive changes, and those still go through a hand-opened PR.
- Standing rules live in `.build/RULES.md` (currently unfilled template).

**Commits:** Conventional Commits, enforced by commitlint on PRs. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower-case, with a subject that isn't empty. Scopes are common, for example `docs(wiki): ...`, and upstream-sync work adds a suffix such as `(upstream sync B2)`.

**Upstream sync:** commits from `earthians/marley` `version-16` are brought in with `git cherry-pick -x`. When they conflict, fork intent wins. Each pick is logged in `wiki/upstream-sync-version-16.md` as picked-clean, picked-with-conflict-resolution, already-present or skipped.

**Review:** CODEOWNERS is `@akurungadam @Sajinsr`. Mergify (inherited from upstream) auto-merges once there is at least one approval and CI passes, and it closes outside PRs aimed at the `version-1x` stable branches. A PR template is provided.
