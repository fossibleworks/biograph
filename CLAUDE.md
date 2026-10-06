<!-- BEGIN INTERACTOR ENGINE WORKFLOW (managed by Interactor Build - edits inside this block are overwritten) -->
# Interactor Build — Engine Workflow

This repository is connected to [Interactor Build](https://build.interactor.com).
Build tracks and ships every change to **fossibleHIS** (`fossibleworks/biograph`) through the **engine**: a tracked
**Goal**, work on the goal's branch, and a single pull request. This guide is the
contract for how work is structured here — read it before editing code.

## The model: Goals and EngineTasks

- **Goal** — the *objective*: a bug, feature, or outcome to address. A Goal owns the
  integration **branch and pull request**, and is the unit a **GitHub issue maps to**
  (**issue → Goal**). A single-repo goal is one branch + one PR.
- **EngineTask** — a *unit of work beneath a Goal*: the breakdown that fulfils it
  (a planning task, then implementation tasks, …). EngineTasks are **not** 1:1 with
  GitHub issues — the engine generates them under the Goal.
- Each EngineTask cycles through **investigation → execution → review**. Those are
  phases *of a task*, not separate tasks or issues.

## The gate — before you edit any code

Every code change ships through the engine. Reading (files, `git log`, `git diff`,
grep) is always fine; the gate applies the moment you would write a file. In order:

1. **A tracked Goal must exist.** No Goal → no edits. Create one (see entry points
   below) before touching a file.
2. **Work on the goal branch `goal/<goalId>`, in an isolated worktree — never on
   `main`.** Direct commits to `main` bypass review and cannot be reverted cleanly.
3. **All changes ship via the goal's PR.** The engine opens the PR; it passes the
   review + CI gates before it merges. No direct pushes to `main`.

If you find yourself about to edit a file with no tracked Goal: **stop**, create the
Goal, and start it — then work on its branch.

An interactive Claude Code session may turn this gate off for itself for a small change with
`ibuild off` (and back on with `ibuild on`) if the project allows it — the change still lands
on its own branch through a hand-opened pull request that runs CI, just without a tracked Goal.

## How to drive it

**Primary entry point (always available):**

- **The Build web UI** — create and manage Goals at
  [build.interactor.com](https://build.interactor.com). This is the entry point that
  always works, including on a freshly-connected repo.
- **Open a GitHub issue** — issue creation alone does **not** create a Goal. The
  importer does not run automatically; landing it as a Goal takes an explicit import
  step (ask the PM AI assistant to import it, or call the bulk-import API), and once
  imported it lands as a **Goal**, with the engine generating the tasks beneath it.

**From the terminal — the `ibuild` binary (v1.1+):** the same CLI that syncs this
repo also carries the engine commands, so a connected repo drives the full lifecycle
locally with no extra setup:

- `ibuild engine goal-create "<title>"` — create a Goal;
  `ibuild engine goal queue <goalId>` — admit it.
- `ibuild engine work <task>` / `ibuild engine report --yes` — work a task and
  report the phase; `ibuild engine goal accept <goalId>` — deliver the merged goal.
  (A claim or a success report changes state shared with the fleet, so it confirms
  first — `--yes` is the non-interactive form, `--dry-run` previews it.)
- Run `ibuild engine` for the full command list, and see the scaffolded
  `.claude/commands/i/engine-*.md` docs (the `/i/engine-*` skills) for
  per-command walkthroughs.

No `ibuild` on this machine (or an older binary without `engine`)? Install or
update it per this repo's Build setup (brew/winget/curl installer) — or just use the
web UI / GitHub issue path above, which always works.
<!-- END INTERACTOR ENGINE WORKFLOW -->

<!-- BEGIN INTERACTOR RULES IMPORT (managed by ibuild — edits inside this block are overwritten) -->
This repo's standing rules for AI sessions live in `.build/RULES.md`, and Claude
Code only auto-loads the repo-root CLAUDE.md, so the line below pulls it in. To stop this
being managed, delete this whole block and leave `<!-- ibuild:rules-import: off -->` somewhere
in this file; it will not come back.

@.build/RULES.md
<!-- END INTERACTOR RULES IMPORT -->
