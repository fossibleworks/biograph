---
title: Work tracking and branching
category: workflow
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - CLAUDE.md
  - AGENTS.md
  - .build/RULES.md
  - .mergify.yml
  - commitlint.config.js
  - .github/CODEOWNERS
---

# Work tracking and branching

## Interactor Build engine (this fork)
- Every code change needs a **tracked Goal** first. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
- Work happens on branch **`goal/<goalId>`** in an isolated worktree. Never commit to the integration branch (`biograph-fh`) or push to it directly.
- Each Goal produces exactly **one PR**, opened by the engine, and it must pass review and CI before merge. EngineTasks under a Goal cycle through investigation → execution → review. Use `ibuild engine work` / `report --yes` / `goal accept`.
- For a small change, an interactive session may use `ibuild off`. It still needs its own branch and a hand-opened PR that runs CI.
- Standing rules live in `.build/RULES.md` (currently a template) and `AGENTS.md`.

## Upstream conventions (inherited)
- **Branches:** `develop` is the upstream default. `version-14/15/16` are stable branches, and PRs against them are auto-closed by Mergify. `version-N-hotfix` receives fixes, and backports use labels like `backport develop` / `backport version-15-hotfix`.
- **Merging:** Mergify merges after 1 approval. Add the `squash` label to squash, or `dont-merge` to block.
- **Commits and PR titles:** Conventional Commits (`fix:`, `feat:`, `docs(wiki):`, `chore:` ...). Upstream sync picks use `git cherry-pick -x` and are logged in `wiki/upstream-sync-version-16.md`.
- **Code owners:** @akurungadam and @Sajinsr own everything.
