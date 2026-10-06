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
---

**Work tracking: Interactor Build engine.** Every code change must belong to a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. EngineTasks under a Goal cycle through investigation, execution and review.
- Before editing any file, a Goal must exist. Create it in the Build web UI or with `ibuild engine goal-create "<title>"` and then `ibuild engine goal queue <goalId>`.
- Work on branch **`goal/<goalId>`** in an isolated worktree. Never commit directly to `biograph-fh` (this fork's default branch).
- Each Goal ships as **one PR**, opened by the engine. The PR must pass review and CI before it merges. Interactive sessions may use `ibuild off` for small changes, but those still go through a hand-opened PR.
- Standing rules live in `.build/RULES.md`, which `CLAUDE.md` imports. `AGENTS.md` and `.github/instructions/*.md` are rendered from it.

**Commits:** use Conventional Commits, enforced by commitlint on PRs. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test, all lower-case. Scopes are optional (`fix(tests): ...`, `docs(wiki): ...`). For upstream sync work, add a suffix such as `(upstream sync B2)` and cherry-pick with `git cherry-pick -x` so the upstream sha is recorded.

**Branches:** `biograph-fh` is the fork integration branch. `upstream` points to `earthians/marley` `version-16`. Upstream's model is `develop` for development, `version-N-hotfix` for fixes and `version-N` for stable. Mergify auto-closes PRs against stable `version-*` branches from non-maintainers.

**Review:** CODEOWNERS (`@akurungadam @Sajinsr`) review everything. Mergify merges after one approval and green CI; the `squash` label squashes and `dont-merge` blocks the merge.
