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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine, from CLAUDE.md):**
- Every code change needs a tracked **Goal**. A GitHub issue maps to a Goal only after an explicit import. The engine creates **EngineTasks** under each Goal, and each task cycles investigation → execution → review.
- Work on the branch `goal/<goalId>` in an isolated worktree. Never commit to the main branch (`biograph-fh` in this fork). Changes ship through the Goal's single PR, which must pass review and CI.
- Use the CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. You can also use the Build web UI.
- `ibuild off` lets an interactive session skip the Goal for a small change. That change still goes through a branch and a hand-opened PR.
- Standing rules live in `.build/RULES.md` (currently unfilled).

**Branching and merging:**
- The upstream model (earthians) uses `develop`, `version-NN-hotfix` and stable `version-NN` branches. Mergify auto-closes PRs against stable `version-14/15/16` from non-maintainers. It merges after at least 1 approval (the `squash` label switches to squash merge) and backports through `backport <branch>` labels.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- The PR template asks for the target branch, a conventional title, passing tests, server-side validation, docs updates, and `closes #XXXX`.
- **Upstream sync:** cherry-pick with `git cherry-pick -x` from `earthians/marley` `version-16`. Fork behaviour wins on conflicts. Record every commit's outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped) in `wiki/upstream-sync-version-16.md`, and tag those commits with `(upstream sync Bn)`.
