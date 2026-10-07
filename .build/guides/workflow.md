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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This repo is connected to **Interactor Build**. Every change ships through the **engine**:

1. **A tracked Goal must exist before any file is edited.** A Goal is the objective. A GitHub issue maps to one Goal, but only after an explicit import. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. The engine generates EngineTasks under the Goal. Each task cycles through investigation → execution → review.
2. **Work on `goal/<goalId>` in an isolated worktree.** Never commit on the default branch **`biograph-fh`**, and never push to it directly.
3. **One PR per Goal.** The engine opens it, and it must pass review and CI before merge. Use `ibuild engine work <task>` / `ibuild engine report --yes` and `ibuild engine goal accept <goalId>`.
4. For small changes, an interactive session may use `ibuild off` (and `ibuild on` to restore) if the project allows it. The change still goes on its own branch with a hand-opened PR that runs CI.

**Commits:** Conventional Commits, enforced by commitlint and the `semantic-commits.yml` workflow. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, lower-case, non-empty subject. Recent history uses scopes and suffixes like `docs(wiki): ...` and `fix: ... (upstream sync B2)`.

**Upstream sync:** pick from `upstream` (`earthians/marley` `version-16`) with `git cherry-pick -x`, so the commit names its upstream sha. Fork intent wins conflicts. Doctype JSON gets a 3-way union of `fields` / `field_order`, and `patches.txt` is unioned. Record each commit's outcome in `wiki/upstream-sync-version-16.md`.

**Upstream conventions you may see referenced:** stable branches `version-14/15/16`, which accept PRs only from maintainers (Mergify auto-closes others), plus `version-N-hotfix` and `develop`. Mergify auto-merges after one approval, or squashes with the `squash` label. CODEOWNERS: `@akurungadam @Sajinsr`. A PR template and issue forms are in `.github/`.

**Project rules:** `.build/RULES.md` (currently unfilled placeholders).
