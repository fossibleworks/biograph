---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
---

## Pull request checks (GitHub Actions)
- **CI** (`ci.yml`): server tests.
  - Skipped for PRs that only change css/js/md/html/csv. Also runs nightly.
  - Python 3.14 and Node 24 on a `mariadb:11.8` service.
  - Runs `compileall` and a merge-conflict-marker check, then `.github/helper/install.sh` sets up the bench.
  - Then runs `bench run-parallel-tests --app healthcare`.
  - On non-PR runs it also collects coverage and uploads it to Codecov.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets, …) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR commit range.
- **Documentation Required**: `feat` PRs need a docs link.
- **CodeQL** (python and javascript) runs on develop pushes, PRs and weekly.
- **Labeler** adds `needs-tests`.
- **Mergify** auto-merges after review.

## Release (upstream-style)
- `initiate_release.yml` opens weekly `chore: release v<N>` PRs from `version-N-hotfix` to `version-N`, for N = 14, 15, 16.
- When a version branch is pushed, `on_release.yml` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not cut a major).
  - It bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations weekly.

## Fork caveats
- These workflows still target `earthians/biograph` and `develop` and use earthians bot secrets.
- On the fork (`fossibleworks/biograph`, branch `biograph-fh`), CI has never run, so the first goal-PR run is the baseline.
- The push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
- Deployment is via Frappe Cloud or `bench`. There is no deploy job in the repo.
