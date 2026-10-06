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
  - AGENTS.md
  - .build/RULES.md
  - .mergify.yml
  - .github/CODEOWNERS
  - commitlint.config.js
---

- **Tracked through Interactor Build.** Every code change needs a **Goal**, created in the Build web UI or with `ibuild engine goal-create`. Do the work on the goal branch **`goal/<goalId>`** in an isolated worktree and ship it through that goal's single PR. Never commit or push to the default branch **`biograph-fh`**. EngineTasks under a Goal go through investigation → execution → review. A GitHub issue becomes a Goal only after an explicit import.
- For small interactive changes, the gate can be switched off with `ibuild off`, if the project allows it. The change still goes on its own branch through a hand-opened PR that runs CI.
- **Commits** follow Conventional Commits (commitlint runs on PRs). Releases strip `chore|ci|test|docs|style` entries from release notes.
- **Upstream sync:** pull from `upstream` (`earthians/marley` `version-16`) with `git cherry-pick -x`. Fork intent wins conflicts. Record every commit's outcome in `wiki/upstream-sync-version-16.md`.
- **Upstream branch model** (inherited config): `develop` for features, `version-NN-hotfix` → `version-NN` for stable. Mergify auto-closes outside PRs to stable branches and merges after 1 approval. CODEOWNERS: @akurungadam @Sajinsr.
- Project rules: `.build/RULES.md` (currently placeholders).
