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
---

This repo is connected to **Interactor Build**. `CLAUDE.md` defines the gate that applies before any file edit.

1. **A tracked Goal must exist.** Create it in the Build web UI, or run `ibuild engine goal-create "<title>"` then `ibuild engine goal queue <goalId>`. GitHub issues map to Goals only after an explicit import.
2. **Work on the branch `goal/<goalId>`** in an isolated worktree. Never commit directly to the default branch **`biograph-fh`** (existing examples: `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`).
3. **Ship through the Goal's single PR.** The engine opens it, and it must pass review and CI before it merges. EngineTasks under a Goal cycle through investigation → execution → review. Report phases with `ibuild engine work` / `ibuild engine report --yes`.

**Exception:** an interactive session may run `ibuild off` for a small change. The change must still go on its own branch through a hand-opened PR that runs CI.

**Other conventions**
- Commits follow Conventional Commits (commitlint), with scopes such as `fix(tests):` and `docs(wiki):`.
- Upstream picks use `git cherry-pick -x` and are recorded batch by batch in `wiki/upstream-sync-version-16.md`. The fork's intent wins conflicts.
- Inherited from upstream: Mergify auto-closes PRs against the `version-*` stable branches. It auto-merges after one approval, or squashes when the PR has the `squash` label. A `backport develop` label triggers backports.
- Project rules live in `.build/RULES.md`, which is still a template.
