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
  - commitlint.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
---

**This fork (fossibleworks/biograph, "fossibleHIS") is driven by Interactor Build.** See `CLAUDE.md`.

- Every code change needs a tracked **Goal**. A GitHub issue becomes a Goal only through an explicit import. The engine breaks each Goal into EngineTasks, and each task goes through investigation, execution and review.
- Work on the branch **`goal/<goalId>`** in an isolated worktree. Never commit straight to the default branch, which is **`biograph-fh`** here.
- Each Goal ships through a single PR that the engine opens. Review and CI gates must pass before merge.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. The Build web UI always works as well. An interactive session may use `ibuild off` for a small change, but it still needs its own branch and a hand-opened PR.
- Project rules live in `.build/RULES.md`; it is currently a placeholder. `.claude/rules/`, `.cursor/rules/` and `.github/instructions/` mirror it, and `AGENTS.md` lists the guides.

**Inherited upstream conventions** (earthians/biograph):
- Conventional Commit titles, checked by commitlint on every PR.
- PR template: pick the target branch, keep logic and validations server-side, update docs, and use `closes #XXXX`.
- Mergify (upstream branches): PRs against stable `version-14/15/16` are auto-closed; target `develop` or `version-N-hotfix` instead. PRs auto-merge after 1 approval (the `squash` label switches to squash merge, and `dont-merge` blocks merging). `backport <branch>` labels open backports.
- CODEOWNERS: `@akurungadam @Sajinsr`.
- Use the labels `skip-release-notes` and `translation` where they apply.
