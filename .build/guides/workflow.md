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
  - commitlint.config.js
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Engine-tracked work (Interactor Build).** `CLAUDE.md` makes this binding.
1. Before editing any file there must be a tracked **Goal**. Create one in the Build web UI or with `ibuild engine goal-create "<title>"`, then `ibuild engine goal queue <goalId>`. A GitHub issue becomes a Goal only after an explicit import.
2. Work on branch **`goal/<goalId>`** in an isolated worktree. **Never commit to the default branch** (`biograph-fh` on this fork).
3. All changes ship through the Goal's single PR, which must pass review and CI. Each EngineTask goes through investigation → execution → review. Interactive sessions may run `ibuild off` for small changes, but the change must still go through its own branch and a hand-opened PR with CI.

**Repository conventions**
- **Commits:** Conventional Commits, checked by commitlint in `semantic-commits.yml`. Add a scope where it helps, for example `fix(tests):`, `docs(wiki):`, `test:`, `chore:`. Upstream cherry-picks use `git cherry-pick -x` and carry the batch tag, for example `(upstream sync B2)`.
- **PRs:** follow the template. Name the target branch, use a conventional title, make sure tests pass, keep logic server-side, update docs, and include `closes #XXXX`.
- **Branches:**
  - Upstream-style branches are `develop` for features, `version-NN-hotfix` for fixes, and `version-14/15/16` for stable.
  - Mergify auto-closes PRs against stable branches unless the author is a maintainer.
  - Mergify merges after 1 approval: a merge commit by default, or a squash with the `squash` label. The `dont-merge` label blocks merging.
- **Code owners:** `@akurungadam` and `@Sajinsr` for `*`.
- **Upstream sync policy:** fork intent wins. Keep biograph-fh behaviour and add the upstream fix on top. For DocType JSON, take the 3-way union. Record each pick in `wiki/upstream-sync-version-16.md`.
- `.build/RULES.md` holds the project rules. It is currently an unfilled template.
