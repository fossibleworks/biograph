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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/release.yml
---

## On pull requests
- **CI / Server Tests** (`ci.yml`) runs on PRs, except changes that touch only css/js/md/html/csv, and nightly at 00:00 UTC. Steps:
  1. Run `compileall` and a merge-marker check.
  2. `install.sh` sets up a bench with frappe, erpnext and payments. They use the base branch, or `version-16` for fork branches.
  3. Install the app.
  4. Run `bench run-parallel-tests --app healthcare` against MariaDB 11.8, with a 30-minute timeout.
  5. On non-PR runs, upload coverage to Codecov.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Frappe semgrep rules and `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR's commits.
- **Documentation Required**: `feat` PRs must link wiki docs.
- **Labeler**: adds `needs-tests`. **CodeQL**: python and JS, on develop and weekly.

## Release (inherited from upstream earthians/biograph)
- `initiate_release.yml` opens a release PR from `version-1x-hotfix` into `version-1x` (14, 15, 16) every Tuesday.
- `on_release.yml`: pushes to `version-14/15/16` run **semantic-release** (angular preset; breaking changes do not trigger a major release). It rewrites the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style lines. The `skip-release-notes` label excludes a PR.
- `generate-pot-file.yml` refreshes translations weekly.

Fork note: the release workflows target the `earthians/biograph` repo and use earthians bot tokens. On `biograph-fh`, versions are bumped by hand with `chore: bump version to x.y.z` commits that follow upstream. Workflow-file changes need the `workflow` token scope, so they may be deferred (see the sync ledger).
