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
  - .mergify.yml
  - codecov.yml
  - .github/helper/install.sh
---

**PR checks (GitHub Actions)**
- `ci.yml` **Server Tests**: runs on PRs (skipped when only css/js/md/html/csv files change) and nightly. It uses Ubuntu, Python 3.14, Node 24 and a MariaDB 11.8 service. Steps: `compileall` plus a merge-marker check, then `.github/helper/install.sh` (bench with frappe, payments and erpnext, falling back to `version-16` for fork branches), then `bench run-parallel-tests --app healthcare`. On non-PR runs, coverage goes to Codecov (`fail_ci_if_error`).
- `linters.yml` / `linters.v2.yml`: run all pre-commit hooks (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, …) and Semgrep (Frappe rules plus `r/python.lang.correctness`).
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a docs link (or `no-docs`).
- `codeql.yml`: CodeQL for Python and JS on `develop` and weekly.
- `labeller.yml`: adds labels, e.g. `needs-tests`.
- Merging: Mergify auto-merges after one approval and green CI.

**Release (upstream model, inherited)**
- `initiate_release.yml`: every Tuesday it opens `version-N-hotfix → version-N` release PRs for 14/15/16.
- `on_release.yml`: a push to `version-14/15/16` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger major releases). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates release notes and drops chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded (`.github/release.yml`).
- `generate-pot-file.yml`: regenerates the translation POT weekly.
- **Deployment:** installs pull the app with bench (`bench get-app` / `install-app` / `migrate`), or run on Frappe Cloud. The repo has no deploy pipeline of its own.

**Fork notes:** several workflows still point at `earthians/biograph` and use earthians bot secrets. `biograph-fh` has never run `ci.yml`, so the first goal-PR run sets the baseline. The current push credential cannot modify `.github/workflows/*`, so changes there must be applied by hand.
