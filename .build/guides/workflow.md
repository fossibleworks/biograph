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
---

- **Interactor Build engine:** every change is tracked by a **Goal**, the unit a GitHub issue maps to. Engine tasks under the Goal cycle through investigation → execution → review.
  - Work happens on branch `goal/<goalId>` in an isolated worktree, never on the main branch (`biograph-fh`).
  - Each goal ships through a single PR opened by the engine.
  - CLI: `ibuild engine goal-create`, `goal queue`, `work`, `report --yes`, `goal accept`.
  - For small changes, an interactive session may run `ibuild off`; the change still goes through its own branch and PR.
- **Commits:** Conventional Commits, enforced by commitlint in the `semantic-commits` workflow. Scopes are common (e.g. `feat(appointment):`, `docs(wiki):`, `fix(linters):`).
- **Upstream sync work:**
  - Use `git cherry-pick -x` from `earthians/marley` `version-16`.
  - Fork intent wins conflicts.
  - For doctype JSON, take a 3-way union of fields and field_order.
  - For `patches.txt`, take the union.
  - Keep the fork's `.releaserc`.
  - Record each outcome (picked-clean / picked-with-conflict-resolution / already-present / skipped) in the wiki ledger.
- **Upstream branching model (Mergify):** PRs target `develop` or `version-N-hotfix`. Direct PRs to stable `version-14/15/16` are auto-closed. Backports use labels like `backport version-16-hotfix`. Merge happens after ≥1 approval; the `squash` label squashes and `dont-merge` blocks.
- **PR template:** state the target branch, explain the problem solved, put business logic server-side, update docs, and include `closes #XXXX`.
