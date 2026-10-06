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
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/workflows/codeql.yml
---

**On pull requests**
- `ci.yml` (Server Tests) runs on PRs, except those touching only css/js/md/html/csv or targeting `version-*-beta`, and nightly at 00:00 UTC. It compiles all Python and fails on merge-conflict markers. It then installs a bench with MariaDB 11.8 (`.github/helper/install.sh`) and runs `bench run-parallel-tests --app healthcare`. On non-PR runs it also collects coverage and uploads it to Codecov.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, ruff-format, eslint, prettier, pip-audit, detect-secrets) and Semgrep with Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint on the PR's commits.
- `docs_checker.yml` requires a wiki docs link on `feat` PRs.
- `labeller.yml` auto-labels PRs (`.github/labeler.yml`).
- `codeql.yml` runs CodeQL for Python and JavaScript on `develop` pushes and PRs, plus a weekly schedule.

**Release (upstream model)**
- `initiate_release.yml` opens weekly (Tuesday) PRs from `version-N-hotfix` to `version-N` for 14, 15 and 16.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16`, using the angular preset; breaking changes do not trigger major releases. It bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes `main.pot` weekly. Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork caveats:** several workflows hardcode `earthians/biograph` and earthians bot secrets. Per the sync ledger, `ci.yml` has never run on `fossibleworks/biograph` `biograph-fh`. Pushes that change `.github/workflows/*` need a token with `workflow` scope.
