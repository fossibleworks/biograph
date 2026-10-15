---
title: CI/CD & Release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/workflows/generate-pot-file.yml
  - .mergify.yml
  - codecov.yml
---

# CI/CD and release

## On pull requests
| Workflow | What it does |
|---|---|
| `ci.yml` (Server Tests) | Ubuntu, Python 3.14, Node 24, MariaDB 11.8. Runs `compileall` and a merge-conflict-marker check. `.github/helper/install.sh` sets up a bench with frappe, payments, erpnext (same branch as the base) and healthcare. Then `run-parallel-tests`. Skipped for PRs that change only css/js/md/html/csv. Also runs nightly at 00:00 UTC with coverage uploaded to Codecov. |
| `linters.yml` / `linters.v2.yml` | pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) and Semgrep with `frappe/semgrep-rules` plus `r/python.lang.correctness` |
| `semantic-commits.yml` | commitlint over every commit in the PR range |
| `docs_checker.yml` | `feat` PRs need a docs `/wiki` link or `no-docs` |
| `labeller.yml` | Adds `needs-tests` when Python changes have no test changes |
| `codeql.yml` | CodeQL for Python and JS on `develop`, plus a weekly run |

## Merging
- Mergify merges once there is at least one approval and CI passes, using a merge commit or a squash with the `squash` label. The `dont-merge` label blocks merging. `backport <branch>` labels open backport PRs.
- In this fork, changes land on `biograph-fh` through the Build engine Goal PR.

## Release (upstream-style)
- `initiate_release.yml` opens a PR every Tuesday from `version-NN-hotfix` to `version-NN` for NN in 14, 15 and 16.
- `on_release.yml` runs on push to `version-14/15/16` and executes **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major). It rewrites `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded (`.github/release.yml`).
- `generate-pot-file.yml` regenerates `main.pot` weekly on `develop`. Crowdin opens `fix: sync translations from crowdin` PRs.
- Dependabot is configured in `.github/dependabot.yml`.

The workflows reference `earthians/biograph` and `develop` from the upstream. Check the targets before relying on release automation in this fork.

## Deployment
There is no deploy pipeline in the repo. Sites pick up releases with `bench update` / `bench get-app` plus `bench migrate` (Frappe Cloud signup is linked from the README).
