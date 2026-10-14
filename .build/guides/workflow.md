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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - commitlint.config.js
  - .github/helper/install.sh
---

**Work tracking: Interactor Build engine** (`CLAUDE.md`)
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. EngineTasks under a Goal go through investigation → execution → review.
- **Gate before any file write:**
  1. A Goal exists. Create it with `ibuild engine goal-create "<title>"` and queue it with `ibuild engine goal queue <id>`, or use the Build web UI.
  2. Work on branch **`goal/<goalId>`** in an isolated worktree, never on the default branch.
  3. All changes ship through the Goal's single PR, which the engine opens.
- Interactive sessions may run `ibuild off` for a small change. That change still goes through its own branch and a hand-opened PR with CI.
- Repo rules: `.build/RULES.md` (currently a placeholder). Guides live under `.build/guides/`. The mirrors (`AGENTS.md`, `.claude/rules/`, `.github/instructions/`) are generated.

**Branches**
- The default/integration branch of this fork is **`biograph-fh`**. Goal branches look like `goal/<slug>-<hash>`.
- The upstream lineage (earthians) uses `develop`, `version-1x-hotfix` and stable `version-14/15/16`. Mergify auto-closes PRs against stable branches. Backports are done with labels (`backport develop`, `backport version-16-hotfix`).
- Upstream sync means cherry-picking from earthians/marley `version-16` with `git cherry-pick -x` and the policy "fork intent wins". Each batch is logged in `wiki/upstream-sync-version-16.md`, and commit subjects carry a suffix such as `(upstream sync B2)`.

**Commits & PRs**
- Commits follow Conventional Commits, enforced by commitlint in CI. Examples from history: `fix: …`, `docs(wiki): …`, `test: …`, `chore: bump version …`.
- PRs follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`: explain the problem, add screenshots/GIFs for UI, keep logic server-side, update docs, and use `closes #N`.
- Merging (Mergify) needs at least 1 approving review and passing CI. Add the label `squash` for a squash merge or `dont-merge` to block it.
- CODEOWNERS: `@akurungadam @Sajinsr`.
