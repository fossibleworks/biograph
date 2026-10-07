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
  - .mergify.yml
  - .github/CODEOWNERS
---

- **Work tracking:** this repo uses Interactor Build's engine.
  - Every code change needs a tracked **Goal** (created in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create`).
  - Work happens on branch `goal/<goalId>` in an isolated worktree and ships through one PR per goal.
  - Never commit or push directly to the default branch `biograph-fh`.
  - EngineTasks under a Goal cycle through investigation → execution → review.
  - Small interactive changes may use `ibuild off` but still go through a PR.
- **Rules:** standing rules live in `.build/RULES.md`, currently an unfilled template. The copies in `.github/instructions/` and `.claude/rules/` are generated from it.
- **Commits:** Conventional Commits, enforced by commitlint. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style and test. The type must be lower-case and the subject non-empty. Upstream cherry-picks use `git cherry-pick -x`. Fork commits often add a scope suffix such as `(upstream sync B2)`.
- **Upstream workflow (earthians):**
  - PRs target `develop` or `version-XX-hotfix`.
  - Mergify auto-closes PRs against the stable `version-14/15/16` branches unless a maintainer opened them.
  - Mergify auto-merges with at least one approval, or squashes when labelled `squash`.
- **Ownership:** CODEOWNERS is `@akurungadam @Sajinsr`.
- **PRs:** follow the PR template: explain the change, update docs, and add `closes #XXXX`.
