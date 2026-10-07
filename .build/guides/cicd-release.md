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
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - codecov.yml
---

**On every PR:**
- `ci.yml` (Server Tests): skipped for PRs that only touch CSS/JS/MD/HTML/CSV and for `version-*-beta` branches. It runs `compileall`, scans for merge-conflict markers, installs a bench with MariaDB 11.8 (`.github/helper/install.sh`), and runs `bench run-parallel-tests --app healthcare`. A nightly cron run collects coverage and uploads it to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, eslint, prettier, pip-audit, detect-secrets, …) plus Semgrep with Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint on commit titles.
- `docs_checker.yml`: `feat` PRs need a wiki docs link or `no-docs`.
- `codeql.yml`: Python and JavaScript analysis on `develop`, plus a weekly run.
- `labeller.yml`: auto-labels PRs.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly `chore: release vN` PRs from `version-N-hotfix` to `version-N` (N = 14, 15, 16).
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16` (`.releaserc`, angular preset, breaking changes never auto-major). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml` regenerates release notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes `main.pot` weekly. Crowdin opens translation PRs.
- Several release workflows still target the `earthians/biograph` repo and use earthians bot secrets, so they are not wired for the fork.
- Fork caveat: `ci.yml` has never run on `biograph-fh`, and the push credential cannot modify `.github/workflows/*`, so workflow-file changes must be applied by hand.
