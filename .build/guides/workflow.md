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
---

**Work tracking (Interactor Build engine), from `CLAUDE.md`:**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. The engine generates EngineTasks under a Goal, and each task runs investigation → execution → review.
- Work on the branch `goal/<goalId>` in an isolated worktree. Never commit to the main branch directly. Existing branches follow this pattern, e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`.
- Each Goal ships through one PR that the engine opens and that must pass review and CI. CLI: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`. Small interactive changes can use `ibuild off`, but still go through a hand-opened PR.

**Branches:** this fork's integration branch is **`biograph-fh`** (the default). Upstream marley's model uses `develop` plus `version-1x-hotfix` → `version-1x` stable branches. Mergify auto-closes PRs from non-maintainers that target `version-14/15/16`.

**Commits:** use Conventional Commits (commitlint). Add a scope when it helps, e.g. `docs(wiki):` or `fix(tests):`. Append the work-stream tag in parentheses when relevant, e.g. `(upstream sync B2)`. Upstream cherry-picks use `git cherry-pick -x` and are logged in `wiki/upstream-sync-version-16.md`.

**Merging:** Mergify merges automatically once there is at least one approving review and no `dont-merge` label. The `squash` label switches it to a squash merge.

`.build/RULES.md` holds the project rule placeholders (not filled in yet).
