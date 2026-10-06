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
  - .github/CODEOWNERS
  - commitlint.config.js
---

This repo is driven by **Interactor Build's engine** (see `CLAUDE.md`):

1. **No edits without a tracked Goal.** Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
2. **Work on `goal/<goalId>` in an isolated worktree. Never commit to the default branch `biograph-fh`.**
3. **One PR per Goal.** The engine opens it, and it must pass review and CI. Each EngineTask under a Goal goes through investigation → execution → review.
4. A small change can use `ibuild off` only if the project allows it. It still needs its own branch and a hand-opened PR.

**Branches:** `biograph-fh` is the fork's integration/default branch. `version-14/15/16` are stable release branches, and Mergify auto-closes PRs from non-maintainers to them. Upstream `earthians/marley` `version-16` arrives through `git cherry-pick -x`, and fork intent wins conflicts. Record every pick in `wiki/upstream-sync-version-16.md`.

**Commits:** Conventional Commits (commitlint). Upstream-sync commits add the suffix `(upstream sync B<n>)`.

**Merging:** Mergify merges once CI passes and there is ≥1 approving review (or squashes with the `squash` label). `dont-merge` blocks merging. CODEOWNERS: @akurungadam @Sajinsr.

Project rules live in `.build/RULES.md`. Mirrors such as `AGENTS.md` and `.claude/rules/` are generated from it.
