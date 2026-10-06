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

**Work tracking (Interactor Build engine):** every code change needs a tracked **Goal**. A GitHub issue maps to a Goal, and the engine generates EngineTasks beneath it. Each task cycles investigation → execution → review. Create Goals in the Build web UI or with `ibuild engine goal-create "<title>"` / `ibuild engine goal queue <id>`.

**Branching:**
- The fork's main integration branch is **`biograph-fh`**.
- Work happens on **`goal/<goalId>`** in an isolated worktree, and ships via a single PR the engine opens.
- Never commit or push directly to the main branch. A small change may bypass the gate with `ibuild off`, but it still goes through its own branch and a hand-opened PR.
- Upstream (earthians) uses `develop`, `version-NN-hotfix` and the stable `version-14/15/16` branches. Mergify auto-closes PRs to stable branches from non-maintainers, and auto-merges after one approval plus CI. The `squash` label squashes; `dont-merge` blocks the merge.

**Commits:** Conventional Commits, enforced by commitlint. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`, in lower case, with a non-empty subject. Scopes are common, e.g. `docs(wiki): ...`, `chore(rules): ...`.

**Upstream sync:** cherry-pick with `git cherry-pick -x`. Conflicts follow the "fork intent wins" policy, and every pick is recorded in `wiki/upstream-sync-version-16.md`.

**Code owners:** @akurungadam and @Sajinsr. Project rules live in `.build/RULES.md`.
