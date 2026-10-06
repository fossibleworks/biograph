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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
---

Work is tracked through **Interactor Build**. Read `CLAUDE.md` before editing.

- **Goal first:** every code change needs a tracked **Goal** (the bug, feature or outcome). A GitHub issue maps to a Goal only after an explicit import. EngineTasks under a Goal cycle through investigation → execution → review.
- **Branching:** work on `goal/<goalId>` in an isolated worktree. **Never commit to the default branch `biograph-fh` (or `main`).** Existing branches follow this pattern, e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`.
- **One PR per Goal.** The engine opens it, and it merges after review and the CI gates.
- **CLI:** `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. For a small change in an interactive session, `ibuild off` is allowed if the project permits it, but the change still lands on its own branch through a PR.
- **Commits:** Conventional Commits, enforced by commitlint. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Use lower-case types and a non-empty subject. Scopes are used (e.g. `docs(wiki): ...`), and sync-batch commits add a suffix such as `(upstream sync B2)`.
- **Upstream sync:** cherry-pick from earthians/marley `version-16` with `git cherry-pick -x`. Fork intent wins conflicts. Doctype JSON gets a 3-way union of `fields` and `field_order`, and `patches.txt` gets a union. Log every commit's outcome in `wiki/upstream-sync-version-16.md`.
- Project rules live in `.build/RULES.md` (currently a template) and `.build/guides/`, rendered into `AGENTS.md`.
