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
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - commitlint.config.js
---

**Interactor Build engine (this fork's contract, from CLAUDE.md)**
- Every code change needs a tracked **Goal**. You can create one in the Build web UI, by importing a GitHub issue, or with `ibuild engine goal-create "<title>"` followed by `ibuild engine goal queue <goalId>`.
- Work happens on the branch **`goal/<goalId>`** in an isolated worktree. Never commit to the main branch directly. Existing branches follow this pattern, e.g. `goal/remove-mandatory-flag-validation-on-healthcare-service-unit-339bf0a8`.
- Each Goal ships through **one PR** opened by the engine. Its EngineTasks cycle through investigation → execution → review. `ibuild off` is an escape hatch for small interactive changes, but those still go through a hand-opened PR with CI.
- The integration (default) branch is **`biograph-fh`**.

**Commits and PRs**
- Use Conventional Commits, enforced by commitlint. For upstream sync work, suffix the subject with the batch, e.g. `fix: ... (upstream sync B2)`. Upstream picks use `git cherry-pick -x`, and fork behaviour wins conflicts.
- The PR template asks you to pick the target branch, follow the commit convention, pass tests locally, keep logic server-side, update docs, and add `closes #XXXX`.
- Inherited upstream rules: Mergify auto-closes PRs to stable `version-14/15/16` from non-maintainers (use a hotfix branch or develop). It auto-merges after CI plus at least one approval. CODEOWNERS is `@akurungadam @Sajinsr`.
- Project rules: `.build/RULES.md` (currently placeholders) is the source for the generated mirrors.
