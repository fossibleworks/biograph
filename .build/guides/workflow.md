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
  - commitlint.config.js
---

**Work tracking (Interactor Build engine), per `CLAUDE.md`:**
- Every code change needs a tracked **Goal** (one GitHub issue maps to one Goal, after an explicit import). The engine breaks Goals into **EngineTasks** (investigation → execution → review).
- **No edits without a Goal.** Create one via build.interactor.com or `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`.
- Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the default branch** (`biograph-fh` in this fork). Everything ships through the goal's single PR, which must pass review and CI.
- An interactive session may temporarily run `ibuild off` for a small change. It still needs its own branch and a hand-opened PR.
- Standing rules live in `.build/RULES.md` (currently placeholders), mirrored into `.claude/rules`, `.cursor/rules` and `.github/instructions`. `AGENTS.md` lists guides from `.build/guides/`.

**Upstream branching (inherited from earthians/biograph):** `develop` is the integration branch. `version-14/15/16` are stable branches fed by `version-N-hotfix`. Mergify auto-closes PRs to stable branches from non-maintainers, auto-merges after ≥1 approval (merge commit by default, squash with the `squash` label, skip with `dont-merge`), and backports with the `backport develop` label.

**PR conventions:** Conventional Commit titles and commits (commitlint), `closes #XXXX`, an explanation of the change, screenshots for UI changes, and a docs link or `no-docs` for `feat`. Default code owners: @akurungadam @Sajinsr.
