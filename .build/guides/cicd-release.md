---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .github/helper/install.sh
  - .github/workflows/codeql.yml
---

**PR checks (GitHub Actions):**
- `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets) and semgrep (Frappe rules plus `r/python.lang.correctness`). Runs on PR, push and dispatch. `linters.yml` is the older variant.
- `ci.yml` **Server Tests** run on PRs, except changes that only touch css/js/md/html/csv, and nightly at 00:00 UTC. Steps:
  - `compileall` and a merge-conflict-marker check
  - `.github/helper/install.sh` bootstraps a bench (frappe, payments, erpnext on the matching branch; fork branches fall back to `version-16`) against MariaDB 11.8
  - `bench run-parallel-tests --app healthcare`
  - Coverage is uploaded to Codecov on non-PR runs
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: `feat` PRs need a docs link.
- `codeql.yml`: python and javascript analysis on `develop`.
- `labeller.yml`: auto-labels PRs.

**Release (upstream-style):**
- `initiate_release.yml` opens weekly (Tuesday 09:30 UTC) `chore: release vNN` PRs from `version-NN-hotfix` → `version-NN` for 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset; breaking changes do not trigger a major release. It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` and `.github/release.yml` handle release notes.
- `generate-pot-file.yml` regenerates translations weekly.

**Fork note:** these workflows still target earthians branches and secrets (`EARTHIANS_BOT_TOKEN`). `ci.yml` has never run on `biograph-fh`. Pushing workflow-file changes needs a credential with `workflow` scope.
