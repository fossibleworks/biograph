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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - commitlint.config.js
  - .github/CODEOWNERS
---

This repo is driven by **Interactor Build's engine** (see `CLAUDE.md`):

1. **A tracked Goal must exist before any file edit.** Create one in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` then `ibuild engine goal queue <goalId>`.
2. **Work on branch `goal/<goalId>` in an isolated worktree, never on the default branch.** The default branch of this fork is `biograph-fh`. Existing remote branches follow `goal/<slug>-<id>` (e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`).
3. **Each Goal ships through one PR** that must pass review and CI. EngineTasks under the Goal go through investigation → execution → review (`ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <goalId>`).
4. Small interactive changes can use `ibuild off`. Those still go through a branch and a hand-opened PR with CI.

**Inherited upstream conventions (earthians/biograph):**
- Conventional Commit titles, enforced by commitlint on PRs.
- No PRs onto stable branches `version-14/15/16`. Mergify auto-closes them except from maintainers. Target `develop` or `version-XX-hotfix`, and backport with labels `backport develop` / `backport version-1X-hotfix`.
- Mergify merges after ≥1 approval. The `squash` label squashes, and `dont-merge` blocks merging.
- The PR template asks for details, screenshots/GIFs, server-side validation, docs updates, and `closes #XXXX`.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- Project rules live in `.build/RULES.md`, which is still an unfilled template, and are mirrored to `.claude/rules`, `.cursor/rules` and `.github/instructions`.
