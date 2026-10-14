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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

# CI/CD and release

## On every pull request
- **Server Tests** (`ci.yml`). Skipped for PRs that only touch css/js/md/html/csv. The job:
  1. runs `compileall` and a merge-marker grep
  2. bootstraps a bench via `.github/helper/install.sh` (frappe, payments and erpnext on the base branch, or `version-16` for fork branches; MariaDB 11.8)
  3. installs `healthcare` and runs `bench run-parallel-tests --app healthcare`
  It also runs nightly on a cron, and that is when coverage is uploaded to Codecov.
- **Linters:**
  - `linters.yml` and `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets) and semgrep with the Frappe rules plus `r/python.lang.correctness`. `linters.v2` also runs on push.
  - `semantic-commits.yml` runs commitlint over the PR's commits.
  - `docs_checker.yml` requires a docs link on `feat` PRs.
- `codeql.yml` does security scanning, and `labeller.yml` labels PRs.

## Merge
Mergify auto-merges after at least one approval with CI passing: a merge commit by default, or squash with the `squash` label. The `dont-merge` label blocks merging. Backport labels open PRs against `develop` or the `version-XX-hotfix` branches.

## Release (inherited upstream pipeline)
- `initiate_release.yml` opens weekly PRs (Tuesday 09:30 UTC) from `version-XX-hotfix` to `version-XX` for 14, 15 and 16. Its `owner: earthians` target means it acts on upstream.
- `on_release.yml` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger majors) when `version-14/15/16` is pushed. It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release. `release_notes.yml` handles release notes.
- `generate-pot-file.yml` regenerates translations weekly. Crowdin opens translation PRs.
- In this fork, versions are bumped manually (`chore: bump version to 16.0.8`).

## Fork caveats
- `biograph-fh` has no `ci.yml` run history, so there is no baseline.
- Workflow-file changes can be blocked when the push credential lacks the `workflow` scope (see sync ledger item B2 #86).
