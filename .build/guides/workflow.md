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
  - .github/CODEOWNERS
  - .github/helper/install.sh
---

**This fork (`fossibleworks/biograph`) is driven by Interactor Build.**
- Every code change needs a tracked **Goal**. Create one in the Build web UI or with `ibuild engine goal-create "<title>"` and admit it with `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
- Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the main branch `biograph-fh` directly.**
- Each Goal ships through a single PR that the engine opens. The PR must pass review and CI. EngineTasks under the Goal each go through investigation, execution and review.
- Small interactive changes may use `ibuild off`. They still land on their own branch through a hand-opened PR that runs CI.
- Project rules live in `.build/RULES.md`. That file is mirrored to `.claude/rules/`, `.cursor/rules/`, `.github/instructions/` and `AGENTS.md`; edit the source, not the mirrors.

**Upstream conventions that still apply**
- Conventional Commit titles (commitlint).
- Upstream (earthians) releases from `version-14/15/16`, and PRs go to `develop` or `version-N-hotfix`. Mergify closes PRs that target stable branches. Mergify also automerges after at least one approval (squash with the `squash` label) and backports with `backport <branch>` labels.
- Upstream syncs: use `git cherry-pick -x` from `earthians/marley version-16`, and record each pick in `wiki/upstream-sync-version-16.md`. Conflict policy: **the fork's intent wins**.
- Code owners: @akurungadam, @Sajinsr.
