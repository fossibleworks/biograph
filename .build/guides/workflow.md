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

- **Engine gate (Interactor Build):** every code change needs a tracked **Goal**. Do the work on its branch `goal/<goalId>` in an isolated worktree and ship it through the goal's single PR. Never commit directly to the default branch **`biograph-fh`**. Create and queue goals with `ibuild engine goal-create "<title>"` / `ibuild engine goal queue <id>`. Work and report tasks with `ibuild engine work` / `ibuild engine report --yes`. GitHub issues become Goals only after an explicit import. `ibuild off` exists for small changes the project allows, and those still go through a hand-opened PR.
- **Commits:** Conventional Commits, checked by `semantic-commits.yml` (commitlint). Use a scope when it helps, for example `docs(wiki): …` or `fix: … (upstream sync B2)`.
- **Upstream syncs:** use `git cherry-pick -x` from `earthians/marley version-16` in numbered batches. Fork intent wins conflicts. Merge doctype JSON as a 3-way union and take the union of `patches.txt`. Record every commit's outcome in `wiki/upstream-sync-version-16.md` (picked-clean / picked-with-conflict-resolution / already-present / skipped).
- **Review and merge (inherited upstream config):** CODEOWNERS are @akurungadam and @Sajinsr. Mergify auto-merges after ≥1 approval and passing CI, squashes when the `squash` label is set, and blocks with `dont-merge`. It closes PRs against stable `version-1x` branches; target a hotfix branch or develop instead. Upstream-origin workflows still reference `develop`/`version-*` branches.
- **Rules source:** `.build/RULES.md`, which is still a template with nothing filled in.
