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
  - .github/CODEOWNERS
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Work is tracked through **Interactor Build's engine** (see `CLAUDE.md`).

- **Goal first.** Every code change needs a tracked **Goal**, created in the Build web UI or with `ibuild engine goal-create`. GitHub issues become Goals only after an explicit import. EngineTasks under a Goal go through investigation, then execution, then review.
- **Branching.** Work on `goal/<goalId>` in an isolated worktree, never on the default branch. In this fork the default branch is **`biograph-fh`**. Each Goal gets one PR into `biograph-fh`. Never push directly to it. `ibuild off` allows small ungated changes, but those still go through a hand-opened PR with CI.
- **Commits.** Use Conventional Commits, enforced by commitlint. Common scopes are `fix(tests):` and `docs(wiki):`. Add a suffix such as `(upstream sync B2)` for batch work.
- **Upstream sync.** Cherry-pick from `upstream` (earthians/marley `version-16`) with `git cherry-pick -x`.
  - Fork intent wins conflicts.
  - Doctype JSON gets a 3-way union of fields.
  - `patches.txt` gets a union.
  - Record each commit's outcome in `wiki/upstream-sync-version-16.md`.
- **PRs.** Follow the PR template: explain the problem, add screenshots for UI changes, write `closes #N`, and keep logic server-side. CODEOWNERS (`@akurungadam`, `@Sajinsr`) review. Inherited Mergify rules auto-merge after one approval and green CI, and close PRs opened against stable `version-*` branches.
- **Project rules** live in `.build/RULES.md`, currently an unfilled template. Guides go in `.build/guides/` and are rendered into `AGENTS.md`.
