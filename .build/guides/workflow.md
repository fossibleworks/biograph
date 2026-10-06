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
  - AGENTS.md
  - .build/RULES.md
  - .mergify.yml
  - .github/CODEOWNERS
  - commitlint.config.js
---

This repo (`fossibleworks/biograph`, Build project **fossibleHIS**) is driven by **Interactor Build's engine**.

- **Issue → Goal:** a **Goal** is the tracked objective and owns one branch and one PR. Goals are broken into **EngineTasks**, and each task cycles through investigation, execution and review. Creating a GitHub issue does not create a Goal. The issue must be imported explicitly.
- **Gate before editing:** no tracked Goal means no file edits. Work on branch `goal/<goalId>` in an isolated worktree, **never on `main` or the default branch `biograph-fh`**. All changes ship through the goal's PR, which must pass review and CI. No direct pushes.
- **CLI:** `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <goalId>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <goalId>`. The web UI at build.interactor.com always works as a fallback. `ibuild off` disables the gate for small changes in an interactive session, if the project allows it. Those changes still go through their own branch and PR.
- **Commits:** conventional commits, enforced by commitlint on PRs. Upstream-sync work uses `git cherry-pick -x` and tags fork-side commits with a suffix such as `(upstream sync B2)`.
- **Upstream branch model (earthians):** `develop` is the integration branch. `version-NN-hotfix` branches are released into `version-NN` by weekly automated PRs. Mergify auto-closes PRs against stable `version-14/15/16` branches from non-maintainers. CODEOWNERS is `@akurungadam @Sajinsr`.
- **Project rules:** standing rules live in `.build/RULES.md`, which currently contains placeholders.
