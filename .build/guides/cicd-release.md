---
title: CI/CD & Release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/release.yml
  - .github/helper/install.sh
---

# CI/CD and release

## PR checks (GitHub Actions)
- **`ci.yml` (Server Tests).** Runs on PRs, but skips changes that only touch css/js/md/html/csv. It also runs nightly at 00:00 UTC.
  - Steps: `compileall` and a merge-marker grep, then `.github/helper/install.sh` (bench init plus Frappe/ERPNext). On fork branches it falls back to `version-16`.
  - Then: `bench run-parallel-tests --app healthcare` on MariaDB 11.8. Coverage goes to Codecov on non-PR runs.
- **`linters.v2.yml`** runs on push and PR. It runs pre-commit (ruff, eslint, prettier, detect-secrets, pip-audit, ...) and Semgrep with the frappe rules plus `r/python.lang.correctness`. `linters.yml` is an older PR-only duplicate.
- **`semantic-commits.yml`**: commitlint over the PR commit range.
- **`docs_checker.yml`**: requires a docs link for `feat` PRs.
- **`codeql.yml`**: CodeQL for Python and JS, on `develop` and weekly.
- **`labeller.yml`**: applies `needs-tests`.

## Release (inherited from upstream earthians)
- **`initiate_release.yml`** opens weekly `chore: release vN` PRs from `version-N-hotfix` to `version-N` (N = 14/15/16) on `earthians/biograph`.
- **`on_release.yml`** runs **semantic-release** on pushes to `version-14/15/16`. It uses the angular preset; breaking changes do not trigger a major release.
  - It rewrites `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- **`release_notes.yml`** regenerates the notes and drops `chore/ci/test/docs/style` entries. The `skip-release-notes` label excludes a PR.
- **`generate-pot-file.yml`** regenerates translations weekly.

## Fork specifics
In this fork, the default branch is `biograph-fh` and changes land through engine Goal PRs. At the time the wiki ledger was written, `ci.yml` had no run history on `biograph-fh`. Release workflows point at the `earthians` repo and secrets, so they do not release this fork. Manual version bumps use `chore: bump version to x.y.z`.

Deployment is to Frappe sites via bench (`bench get-app` + `install-app` / `migrate`). Frappe Cloud is advertised as the hosted option.
