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
  - .github/workflows/semantic-commits.yml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
  - .github/CODEOWNERS
  - .mergify.yml
---

**Interactor Build engine (fork policy, from CLAUDE.md)**
- Every code change needs a tracked **Goal**. Create it in the Build web UI or with `ibuild engine goal-create "<title>"`; GitHub issues must be explicitly imported to become a Goal.
- Work on the goal branch `goal/<goalId>` in an isolated worktree, and ship through the goal's single PR into **`biograph-fh`**, the fork's main branch.
- Never commit or push directly to `biograph-fh`.
- Goals break down into EngineTasks, each going investigation → execution → review.
- `ibuild off` is allowed only for small changes, and those still land via a hand-opened PR that runs CI.

**Standing rules**
- `.build/RULES.md` holds the standing rules and is mirrored to the AGENTS.md, Claude, Cursor and Copilot rules files. It is currently unfilled.

**Commits**
- Conventional Commits, enforced by commitlint on PRs. Allowed types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test.
- Fork convention is to append context, for example `fix: ... (upstream sync B2)`. Documentation goes in `docs(wiki): ...`.

**Upstream sync**
- Pull Marley `version-16` fixes with `git cherry-pick -x`.
- Conflict policy: the fork's intent wins. DocType JSON is a three-way union of fields and field_order, and `patches.txt` is a union.
- Record every commit's outcome (picked-clean, picked-with-conflict-resolution, already-present, skipped) in `wiki/upstream-sync-version-16.md`.

**PRs**
- Follow `.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md`: explain the problem, add screenshots for UI changes, keep logic on the server, update docs, and add `closes #N`.
- Code owners are @akurungadam and @Sajinsr.
- Inherited upstream Mergify rules apply: one approval auto-merges, the `squash` label squashes, `backport <branch>` labels backport, and PRs against `version-1x` stable branches are auto-closed.
