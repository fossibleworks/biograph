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
  - .build/CLAUDE.md
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .mergify.yml
  - .github/CODEOWNERS
---

**Work tracking: Interactor Build (engine).** These rules come from `CLAUDE.md`.
- Every code change needs a tracked **Goal**. A GitHub issue becomes a Goal only after an explicit import step. EngineTasks under a Goal cycle through investigation → execution → review.
- Before writing any file, a Goal must exist (`ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`, or use the Build web UI).
- Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the default branch**, which is `biograph-fh` in this fork.
- Changes ship through the goal's single PR, which the engine opens and which must pass review and CI. Interactive sessions may use `ibuild off` for small changes, but those still go through their own branch and a hand-opened PR.
- `.build/` holds `vision.md` (read it before planning), `RULES.md`, tasks, phases and sprints. Don't put `[interactor-sync]` in your own commit messages.

**Commits and PRs** (inherited from upstream):
- **Conventional commit titles**, enforced by commitlint on every PR. Allowed types: `build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test`. The type is lower-case and the subject must not be empty.
- Follow the PR template: say which branch to target, explain *why* the change exists, add screenshots or GIFs for UI, make sure tests pass locally, keep business logic server-side, update docs, and add `closes #NNN`.
- `feat` PRs need a wiki docs link or `no-docs` in the body.
- Default reviewers are `@akurungadam` and `@Sajinsr` (CODEOWNERS).

**Upstream branch model** (encoded in `.mergify.yml` and `.releaserc`):
- Development happens on `develop`. Stable branches are `version-14/15/16`, with matching `version-XX-hotfix` branches.
- PRs opened directly against stable branches by non-maintainers are auto-closed.
- Mergify merges after 1 approval (squash if the PR has the `squash` label; `dont-merge` blocks it). Labels `backport develop` and `backport version-XX-hotfix` auto-backport.
- Translation PRs from Crowdin carry `translation` and `skip-release-notes`.
