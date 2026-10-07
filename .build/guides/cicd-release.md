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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
---

**PR checks (GitHub Actions):**
- `ci.yml` (Server Tests):
  - Runs on PRs, skipping css/js/md/html/csv-only changes and `version-*-beta` branches, and nightly at 00:00 UTC.
  - Uses Python 3.14, Node 24 and MariaDB 11.8.
  - Runs `compileall` plus a merge-conflict marker check, then `.github/helper/install.sh` to set up a bench, then `run-parallel-tests`.
  - On non-PR runs it uploads coverage to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: a docs link is required for `feat` PRs.
- `codeql.yml`: Python/JS CodeQL on `develop` and weekly.
- `labeller.yml`: auto-labels PRs.

**Release (inherited from upstream earthians):**
- `initiate_release.yml`: every Tuesday, opens `version-XX-hotfix` → `version-XX` PRs for versions 14, 15 and 16.
- `on_release.yml`: on push to `version-14/15/16`, runs `semantic-release` (`.releaserc`, angular preset, breaking changes do not trigger major bumps). It writes the version into `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml`: regenerates GitHub release notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml`: weekly POT regeneration on `develop`.

**Fork notes:**
- Several workflows hard-code `earthians/biograph` and earthians bot tokens.
- On `fossibleworks/biograph`, `ci.yml` has never run, so there is no CI baseline.
- The current push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
