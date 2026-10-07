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
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
---

**PR checks** (GitHub Actions)
- `ci.yml` (Server Tests) runs on PRs except those touching only css/js/md/html/csv, and every night at 00:00 UTC. It runs on Python 3.14, Node 24 and MariaDB 11.8, compiles all Python, checks for leftover merge-conflict markers, sets up a bench with `.github/helper/install.sh`, and runs `bench run-parallel-tests --app healthcare`. On runs that are not PRs, coverage goes to Codecov.
- `linters.yml` and `linters.v2.yml` run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets and others) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint on the PR's commit range.
- `docs_checker.yml` fails `feat` PRs that have no wiki docs link.
- `labeller.yml` applies labels (`needs-tests`). `codeql.yml` runs CodeQL for Python and JS on `develop` and every week.

**Release** (built for upstream earthians)
- `initiate_release.yml` opens a PR every Tuesday from `version-NN-hotfix` to `version-NN` for versions 14, 15 and 16.
- `on_release.yml` runs **semantic-release** (`.releaserc`, Angular preset; breaking changes do not trigger a release) on pushes to `version-14/15/16`. It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes, leaving out PRs labelled `skip-release-notes` (see `.github/release.yml`).
- `generate-pot-file.yml` regenerates translations every week. Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork caveats:** the wiki ledger notes that the fork has never run `ci.yml` on `biograph-fh`, so there is no CI baseline. The release workflows still point at `earthians/biograph` and use earthians bot tokens. The push credential cannot change files under `.github/workflows/`, so workflow changes must be applied by hand.
