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
  - .github/helper/install.sh
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/CODEOWNERS
---

# Work tracking and branching

## Interactor Build engine (this fork)
- Every code change needs a tracked **Goal**. The Goal owns one branch and one PR. A GitHub issue maps to a Goal only after an explicit import.
- Each Goal is broken into **EngineTasks**, and each task goes through investigation, execution and review.
- Work on **`goal/<goalId>`** in an isolated worktree. **Never commit to `biograph-fh`** (the fork's default and integration branch) or push to it directly. All changes go through the Goal's PR, which must pass review and CI.
- From the CLI:
  - `ibuild engine goal-create "<title>"` creates a Goal, and `ibuild engine goal queue <goalId>` admits it.
  - `ibuild engine work <task>` and `ibuild engine report --yes` work a task and report each phase.
  - `ibuild engine goal accept <goalId>` delivers the merged Goal.
- An interactive session may run `ibuild off` for a small change. That change still goes on its own branch through a hand-opened PR that runs CI.
- Standing rules live in `.build/RULES.md`, which CLAUDE.md imports.

## Upstream sync
- Upstream earthians/marley `version-16` commits are brought in with `git cherry-pick -x` in numbered batches. The conflict policy is **fork intent wins**:
  - DocType JSON gets a 3-way union of `fields` and `field_order`.
  - `patches.txt` gets a union.
  - The fork keeps its own `.releaserc` version.
- Each pick is logged as picked-clean, picked-with-conflict-resolution, already-present, skipped or deferred in `wiki/upstream-sync-version-16.md`.

## PRs and commits
- Commit titles use conventional commits, enforced by the Semantic Commits workflow.
- Follow the PR template:
  - explain the problem and the change
  - make sure tests pass
  - keep logic on the server side
  - put `closes #XXXX` in the PR
- Upstream Mergify rules (inherited) auto-close PRs on `version-*` stable branches from non-maintainers and auto-merge after one approval. CODEOWNERS: `@akurungadam @Sajinsr`.
