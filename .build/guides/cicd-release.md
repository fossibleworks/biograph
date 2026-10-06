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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - codecov.yml
---

**PR checks (GitHub Actions)**
- `ci.yml` (Server Tests) runs on PRs that touch non-css/js/md/html/csv files, and nightly. It uses MariaDB 11.8, Python 3.14 and Node 24. Steps: `compileall`, a check for merge-conflict markers, `.github/helper/install.sh` (bench, ERPNext, healthcare) and `bench run-parallel-tests --app healthcare`. On non-PR runs it uploads coverage to Codecov.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint on the PR commit range.
- `docs_checker.yml` requires a docs link on `feat` PRs.
- `codeql.yml` runs CodeQL for Python and JS on `develop` and weekly.
- `labeller.yml` auto-labels PRs. `dependabot.yml` handles dependency updates.

**Release (inherited from upstream earthians)**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` release PRs for 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. `.releaserc` bumps the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates the notes and drops chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes the translation POT weekly. Crowdin opens `fix: … translations` PRs.

**Fork caveat:** many workflows hard-code `earthians/biograph` or the `develop`/`version-*` branches. The fork's default branch `biograph-fh` has no CI run history. The sync credential cannot push changes under `.github/workflows`, so workflow edits have to be applied by hand.
