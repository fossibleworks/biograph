---
title: Work tracking & branching
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
---

**Build engine (this fork's contract, from CLAUDE.md)**
- Every code change needs a tracked **Goal** in Interactor Build. Create it with the web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`.
- Work happens on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the default branch `biograph-fh`** (the upstream equivalent is `develop`).
- Each Goal maps to one PR, which the engine opens. The PR merges after review and CI pass.
- EngineTasks under a Goal go through investigation → execution → review. Report with `ibuild engine report --yes`.
- Exception: an interactive session may run `ibuild off` for a small change, but that change still goes on its own branch and through a hand-opened PR that runs CI.
- Standing rules: `.build/RULES.md`, mirrored to `.claude/rules`, `.cursor/rules`, `.github/instructions` and `AGENTS.md`.

**Inherited upstream conventions (still configured)**
- Commits follow Conventional Commits (commitlint).
- PR template: pick the target branch, run tests, keep validations server-side, update docs, and use `closes #NNN`.
- Mergify:
  - Closes PRs to stable `version-14/15/16` from non-maintainers.
  - Auto-merges with ≥1 approval (squash if labelled `squash`; `dont-merge` blocks).
  - Backports through `backport develop` / `backport version-1x-hotfix` labels.
- CODEOWNERS: `@akurungadam @Sajinsr`.

**Upstream sync work**: cherry-pick upstream earthians/marley commits with `git cherry-pick -x`. Fork behaviour wins conflicts. Log every commit in `wiki/upstream-sync-version-16.md` using the fixed outcome vocabulary. Fix-ups use a suffix such as `(upstream sync B2)`.
