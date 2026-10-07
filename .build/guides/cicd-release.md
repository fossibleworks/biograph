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
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
  - .mergify.yml
  - .github/helper/install.sh
  - codecov.yml
---

**CI on pull requests** (GitHub Actions)
- `ci.yml` (Server Tests):
  - Skipped for PRs that change only css/js/md/html/csv. It also runs nightly.
  - Compiles all Python and greps for merge-conflict markers.
  - Builds a bench via `.github/helper/install.sh`, installing frappe, payments, erpnext and healthcare on MariaDB 11.8.
  - Runs `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov on non-PR runs.
- `linters.yml` / `linters.v2.yml`: the pre-commit action (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: checks that commit and PR titles are conventional.
- `docs_checker.yml`: docs-link requirement for `feat` PRs.
- `codeql.yml`: Python and JavaScript CodeQL on `develop`, plus a weekly run.
- `labeller.yml`: auto-labels PRs, including `needs-tests`.
- Dependabot is configured.

**Merging**: Mergify auto-merges after 1 approval and green CI, and handles backports to hotfix branches.

**Release**
- `initiate_release.yml` opens weekly PRs from `version-N-hotfix` → `version-N` for N = 14, 15, 16 (Tuesdays).
- `on_release.yml` runs **semantic-release** (`.releaserc`) on pushes to version branches:
  - Angular preset; breaking changes do not trigger a major release.
  - Bumps `__version__` in `healthcare/__init__.py`.
  - Commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml` and `.github/release.yml`: changelog generation, excluding PRs labelled `skip-release-notes`.
- `generate-pot-file.yml` regenerates translation strings weekly.
- Deployment itself is outside this repo. Sites install the app with `bench get-app` and `install-app`, or through Frappe Cloud.
