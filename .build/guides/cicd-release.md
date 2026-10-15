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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - codecov.yml
  - .github/release.yml
---

**On pull requests**
- `ci.yml`, **Server Tests**: compiles all Python and fails on leftover merge-conflict markers. It then installs bench + frappe + erpnext + payments (branch = PR base), installs `healthcare` on `test_site` (MariaDB 11.8, Python 3.14, Node 24) and runs `bench run-parallel-tests --app healthcare`. It skips PRs that change only css/js/md/html/csv, and also runs nightly. On non-PR runs it collects coverage and uploads it to Codecov (`fail_ci_if_error`).
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) plus **Semgrep** with Frappe rules and `r/python.lang.correctness`. v2 also runs on push.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a wiki docs link or `no-docs`.
- `labeller.yml`: auto-labels PRs. `codeql.yml`: CodeQL for Python/JS on develop, plus weekly.
- Mergify auto-merges after ≥1 approval and passing checks.

**Release**
- `initiate_release.yml` (weekly, Tue 09:30 UTC) opens `version-N-hotfix → version-N` release PRs for 14/15/16.
- `on_release.yml`: on push to `version-14/15/16`, **semantic-release** (angular preset, breaking changes don't trigger a major) bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml` regenerates notes and strips chore/ci/test/docs/style entries. Labels `skip-release-notes` exclude PRs.
- `generate-pot-file.yml` (weekly) refreshes the translation POT. Crowdin opens `fix: sync translations from crowdin` PRs.

Several workflows still point at `earthians/biograph` and `develop`, but this fork's default branch is `biograph-fh`. Confirm which triggers actually fire here before relying on them. Deployment is by installing the app into a bench or Frappe Cloud. The repo has no deploy pipeline.
