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
  - commitlint.config.js
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Workflow

## Interactor Build engine (this fork)
- Every code change needs a tracked **Goal** in Interactor Build. A GitHub issue maps to one Goal. EngineTasks under a Goal go through investigation → execution → review.
- Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to `biograph-fh` (main) directly.** Each Goal ships as one PR, which must pass review and CI gates.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. You can also use the web UI at build.interactor.com.
- `ibuild off` lets an interactive session make a small change on its own branch with a hand-opened PR. Use it only if the project allows it.
- Project rules live in `.build/RULES.md`. They are mirrored to `AGENTS.md`, `.claude/rules/`, `.cursor/rules/`, and `.github/instructions/`, so edit the source, not the mirrors.

## Commits and PRs
- Use **Conventional Commits** (commitlint enforces this on PRs), e.g. `fix: …`, `feat(appointment): …`, `docs(wiki): … (upstream sync B2)`.
- Fill in the PR template: target branch, reasoning, screenshots, and `closes #XXXX`.
- PRs need ≥1 approving review. Mergify merges automatically, or squashes with the `squash` label; `dont-merge` blocks it. CODEOWNERS: @akurungadam @Sajinsr.
- Mergify auto-closes PRs from non-maintainers that target stable branches (`version-14/15/16`). Use hotfix or develop branches. The label `backport develop` backports.

## Upstream sync
Use `git cherry-pick -x` from `earthians/marley version-16` in numbered batches. Fork intent wins conflicts. Record every commit's outcome in `wiki/upstream-sync-version-16.md`.
