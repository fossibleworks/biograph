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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - .mergify.yml
---

**Work tracking: Interactor Build engine** (`CLAUDE.md`)
- Every code change needs a tracked **Goal**. GitHub issues map to Goals only after an explicit import. Create a Goal with the Build web UI or `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`.
- Do the work on branch **`goal/<goalId>`** in an isolated worktree and **never on the integration branch**. In this fork the integration branch is **`biograph-fh`**, the default and PR base. Existing goal branches look like `goal/<slug>-<hash>`.
- Each Goal ships through **one PR** that must pass review and CI. Do not push directly to `biograph-fh`.
- Drive EngineTasks with `ibuild engine work <task>` / `ibuild engine report --yes`. A merged goal is delivered with `ibuild engine goal accept <goalId>`.
- Standing rules live in `.build/RULES.md` and are mirrored to `.claude/rules/` and `.github/instructions/`. Those mirrors are generated, so edit the source.

**Commits and PRs**
- Commit messages follow **Conventional Commits** (commitlint `type-enum`). Scope is optional (`fix(tests): ...`, `docs(wiki): ...`). Upstream-sync commits append a batch tag like `(upstream sync B2)`.
- The PR template asks for an explanation of the problem and change, screenshots or GIFs, passing tests, server-side validation, docs, and `closes #XXXX`.
- CODEOWNERS: `@akurungadam @Sajinsr`.

**Upstream sync** (`wiki/upstream-sync-version-16.md`)
- Cherry-pick from `earthians/marley` `version-16` with `git cherry-pick -x`.
- Conflict policy: **fork intent wins**. Doctype JSON gets a 3-way union of `fields`/`field_order`, `patches.txt` gets a union, and `.releaserc` keeps the fork version.
- Record every pick in the ledger as picked-clean, picked-with-conflict-resolution, already-present or skipped.

**Inherited upstream rules** (`.mergify.yml`): PRs against the stable `version-14/15/16` branches are auto-closed. Use `develop` or a hotfix branch upstream. Mergify merges after one or more approvals; the `squash` label squashes and `dont-merge` blocks. A `backport <branch>` label triggers backports.
