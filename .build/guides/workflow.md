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
  - .github/helper/install.sh
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Work tracking (Interactor Build engine), from CLAUDE.md:**
- Every code change needs a tracked **Goal**. A GitHub issue becomes a Goal only after an explicit import. A Goal owns one branch and one PR. EngineTasks under it go through investigation, then execution, then review.
- Before editing any file, the Goal must exist. Work on branch **`goal/<goalId>`** in an isolated worktree and never commit to the default branch. Ship through the goal's PR, which must pass review and CI.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. An interactive session may use `ibuild off` for a small change, which still lands as a hand-opened PR.
- Standing rules: `.build/RULES.md`, also mirrored in `.claude/rules/`, `.cursor/rules/` and `.github/instructions/`. AGENTS.md renders the Build guides index.

**Branches:**
- The fork's integration branch is **`biograph-fh`**, the PR base. CI's install script maps fork branches (`biograph-fh`, `goal/*`) to Frappe/ERPNext `version-16`.
- Upstream (earthians) has `develop`, `version-1x-hotfix` and `version-1x`. Mergify auto-closes PRs against stable `version-*` branches from non-maintainers. PRs need at least one approval. The `squash` label squash-merges; otherwise the PR is merge-committed.
- **Upstream sync:** cherry-pick from `earthians/marley version-16` with `git cherry-pick -x`. Fork intent wins in conflicts: take a 3-way union of doctype JSON fields and a union of `patches.txt`. Record every commit in `wiki/upstream-sync-version-16.md`.

**Commits and PRs:** Conventional Commit titles are checked by commitlint on every PR. Follow the PR template (explain the change, `closes #XXXX`, tests pass, server-side validation, docs). CODEOWNERS is `@akurungadam @Sajinsr`.
