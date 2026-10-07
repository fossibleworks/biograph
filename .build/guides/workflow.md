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
  - .github/helper/install.sh
---

# Workflow

## Interactor Build engine (CLAUDE.md)
- Every code change needs a tracked **Goal**. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <id>`. A GitHub issue becomes a Goal only after an explicit import.
- Work on branch **`goal/<goalId>`** in an isolated worktree, never on the main branch.
- Each Goal ships as **one PR** that the engine opens and that must pass review and CI. Don't push directly.
- EngineTasks under a Goal cycle through investigation, execution and review.
- For small changes, `ibuild off` lets a session skip the gate, but the change still goes through its own branch and a hand-opened PR.

## Branches
- The fork's integration branch is **`biograph-fh`** (the default base for PRs).
- Upstream releases come from `version-14`, `version-15` and `version-16`. Mergify auto-closes outside PRs against stable branches.
- CI's `install.sh` maps fork branches (`biograph-fh`, `goal/*`) to Frappe/ERPNext `version-16`.

## Commits
- Use **Conventional Commits**; `commitlint.config.js` is enforced on PRs.
- Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. Types are lowercase and the subject can't be empty.
- Scopes are common (`docs(wiki): ...`, `fix(tests): ...`), and work for a batch or goal gets a suffix like `(upstream sync B2)`.
- Upstream picks use `git cherry-pick -x`.

## Review / merge
- CODEOWNERS: `@akurungadam` and `@Sajinsr`.
- Mergify merges after one or more approvals; the `squash` label squashes and `dont-merge` blocks the merge.
- The labeler adds `needs-tests`.
- `.build/RULES.md` holds the project rules. Its Always/Never sections are still placeholders.
