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
  - .github/CODEOWNERS
  - .mergify.yml
---

Work is tracked through **Interactor Build**.

- **Goal first:** every code change needs a tracked **Goal**, created in the Build web UI or with `ibuild engine goal-create "<title>"` and admitted with `ibuild engine goal queue <goalId>`. A GitHub issue maps to one Goal, but only after an explicit import. The engine generates **EngineTasks** under the Goal, and each task cycles through investigation → execution → review.
- **Branching:** work on `goal/<goalId>` in an isolated worktree. **Never commit to `main`/`biograph-fh` directly.** The fork's default and integration branch is `biograph-fh`. Upstream (`earthians/marley`) uses `develop`, plus `version-14/15/16` stable branches with `version-N-hotfix` branches.
- **One PR per Goal:** the engine opens it, and it must pass the review and CI gates before merge. For small interactive changes the gate can be disabled with `ibuild off`, but the change still goes through its own branch and a hand-opened PR.
- **Commits:** Conventional Commits (enforced by commitlint): `type(scope): subject` with a lower-case type. Recent history uses scopes such as `docs(wiki): ... (upstream sync B2)` and `fix: ...`.
- **Upstream sync:** cherry-pick with `git cherry-pick -x` (so the upstream sha is recorded). Fork behaviour wins conflicts. Doctype JSON is merged as a union of `fields`/`field_order`, and `patches.txt` as a union. Log every outcome in `wiki/upstream-sync-version-16.md`.
- **Ownership:** CODEOWNERS is `@akurungadam @Sajinsr`. Upstream Mergify auto-closes PRs to stable branches from non-maintainers.
- **Project rules:** `.build/RULES.md` is the source, mirrored to `.claude/rules`, `.cursor/rules`, `.github/instructions` and `AGENTS.md`. It is currently an unfilled template.
