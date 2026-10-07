---
title: CI/CD and release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/helper/install.sh
---

## On pull requests

- **CI / Server Tests** (`ci.yml`)
  - Skips PRs that only touch css/js/md/html/csv, and skips `version-*-beta` branches. Also runs nightly at 00:00 UTC.
  - Runs on Python 3.14 and Node 24, with a mariadb:11.8 service.
  - Steps: `compileall` plus a merge-conflict-marker check, then `install.sh` (bench, with Frappe/ERPNext on the matching branch or `version-16` for fork branches), then `bench run-parallel-tests --app healthcare`.
  - On non-PR runs, coverage is uploaded to Codecov.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep (frappe rules and `r/python.lang.correctness`).
- **Semantic Commits:** commitlint over the PR commit range.
- **Documentation Required:** `feat` PRs need a wiki link.
- **Labeler:** adds `needs-tests`.
- **CodeQL:** Python and JS, on `develop` and weekly.

## Release (inherited from upstream earthians)

- `initiate_release.yml` opens weekly `version-N-hotfix` → `version-N` release PRs for 14, 15 and 16.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16`. Per `.releaserc`, it uses the angular preset, sets breaking changes to not release, bumps `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x`.
- `release_notes.yml` regenerates release notes. `generate-pot-file.yml` refreshes translations weekly.

## Fork caveat

Release and bot workflows reference `earthians/biograph` and its secrets, so they don't apply to `fossibleworks/biograph`. Here, the fork version (e.g. `chore: bump version to 16.0.8`) is bumped manually. The ledger notes that `ci.yml` has never run on `biograph-fh`. The push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
