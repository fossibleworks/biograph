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
  - .mergify.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - .github/workflows/semantic-commits.yml
---

## Engine gate (CLAUDE.md, Interactor Build)
Every code change is tracked as a **Goal** in Interactor Build. A GitHub issue maps to a Goal, but only after an explicit import.

**Before editing any file:**
1. A tracked Goal must exist. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then admit it with `ibuild engine goal queue <goalId>`.
2. Work on the branch `goal/<goalId>` in an isolated worktree. **Never commit to the default branch** (`biograph-fh` in this fork).
3. Ship through the goal's single PR, which the engine opens. That PR passes the review and CI gates before it merges.

EngineTasks under a Goal cycle through investigation → execution → review (`ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <goalId>`). For a small change, an interactive session may use `ibuild off` (if the project allows it). The change still goes on its own branch through a hand-opened PR that runs CI.

## Upstream conventions that still apply
- **Conventional Commit** titles, enforced by the `Semantic Commits` workflow.
- PRs follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`:
  - Explain the problem and change, and attach screenshots.
  - Use `closes #XXXX`.
  - Tests pass.
  - Business logic stays server-side.
  - Docs are updated (`feat` PRs need a docs link or `no-docs`).
- **Mergify:**
  - PRs into stable `version-14/15/16` from non-maintainers are auto-closed. Target `develop` or a `version-N-hotfix` branch.
  - PRs merge automatically after 1 approval plus CI. The `squash` label switches to squash merge; `dont-merge` blocks merging.
  - `backport <branch>` labels open backports.
- CODEOWNERS: `@akurungadam @Sajinsr` own everything.
- Project rules in `.build/RULES.md` are currently unfilled placeholders.
