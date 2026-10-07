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

**Interactor Build engine (this fork, `fossibleworks/biograph`)**
- Every code change needs a tracked **Goal**. The engine generates **EngineTasks** under it, and each task cycles through investigation → execution → review.
- Work on branch `goal/<goalId>` in an isolated worktree. **Never commit to `biograph-fh`**, the default and main branch.
- All changes ship through the Goal's single PR, which must pass review and CI before merge.
- CLI: `ibuild engine goal-create "<title>"`, `ibuild engine goal queue <id>`, `ibuild engine work <task>`, `ibuild engine report --yes`, `ibuild engine goal accept <id>`. Goals can also be managed in the Build web UI, or created by importing a GitHub issue.
- An interactive session can switch the gate off for a small change with `ibuild off`, but the change still goes through its own branch and a hand-opened PR.

**Commit conventions:** Conventional Commits, enforced by commitlint in CI. Upstream sync work tags commits with a suffix such as `(upstream sync B2)` and records each batch in `wiki/upstream-sync-version-16.md`.

**Upstream sync policy:** cherry-pick with `git cherry-pick -x`. Fork intent wins on conflicts. DocType JSON gets a 3-way union of `fields` and `field_order`; `patches.txt` gets a union; keep the fork's `.releaserc`.

**Inherited upstream rules:**
- Mergify auto-closes PRs from non-maintainers that target `version-14/15/16`.
- PRs auto-merge after 1 approval; the `squash` label switches to squash merge.
- `backport <branch>` labels trigger backports.
- CODEOWNERS: @akurungadam @Sajinsr.
