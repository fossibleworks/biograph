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
  - .github/workflows/semantic-commits.yml
---

Interactor Build's **engine** tracks the work (see `CLAUDE.md`):
1. **Every code change needs a tracked Goal.** Create it in the Build web UI, or run `ibuild engine goal-create "<title>"` and then `ibuild engine goal queue <goalId>`. GitHub issues map to Goals only after an explicit import.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. Never commit to the integration branch directly.
3. Each Goal ships as **one PR**, opened by the engine, into **`biograph-fh`** (the fork's main branch). It merges after review and CI pass.
4. An EngineTask goes through investigation, then execution, then review. Report progress with `ibuild engine work` / `ibuild engine report --yes`.

For a small change, an interactive session may run `ibuild off` (if the project allows it). The change still goes on its own branch through a hand-opened PR.

**Upstream sync:** pull earthians/marley `version-16` in with `git cherry-pick -x`, in numbered batches (B1, B2, ...). On conflict, fork intent wins. Doctype JSON gets a 3-way union of fields. `patches.txt` gets a union. Log every outcome in `wiki/upstream-sync-version-16.md`.

**Commits:** Conventional Commits, checked by commitlint on PRs. Upstream-sync commits add a suffix such as `(upstream sync B2)`.

**Upstream conventions** (in config inherited from earthians): `version-1x` stable branches don't accept outside PRs (Mergify auto-closes them). Mergify merges after one approval, or squashes when the PR has the `squash` label. CODEOWNERS: @akurungadam @Sajinsr.
