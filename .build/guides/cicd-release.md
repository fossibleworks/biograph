---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

GitHub Actions workflows (`.github/workflows/`):

- **`ci.yml` (Server Tests):**
  - Triggers: PRs (skipped when only css/js/md/html/csv change) and a nightly cron.
  - Environment: Ubuntu, Python 3.14, Node 24 and a MariaDB 11.8 service.
  - Steps:
    1. `compileall` and a merge-conflict-marker check.
    2. `.github/helper/install.sh`, which runs bench init and pulls frappe, payments and erpnext. It uses the PR base branch, falling back to `version-16` for fork branches such as `biograph-fh` and `goal/*`.
    3. `bench run-parallel-tests`.
    4. Coverage upload on non-PR runs, then Codecov.
- **`linters.yml` / `linters.v2.yml`:** pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with `frappe/semgrep-rules` and `r/python.lang.correctness`.
- **Other checks:**
  - `semantic-commits.yml`: commitlint on PR commit titles.
  - `docs_checker.yml`: docs link required on `feat` PRs.
  - `labeller.yml`: PR labels from `.github/labeler.yml`.
  - `codeql.yml`: weekly and on `develop`.
  - `.mergify.yml`: merge automation and backports.
  - Dependabot.
- **Release:**
  - `initiate_release.yml` opens weekly release PRs (Tuesday cron).
  - `on_release.yml` runs `npx semantic-release` on the `version-*` branches. Using the Angular preset, it bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release. Breaking changes do not auto-bump major.
  - `release_notes.yml` regenerates release notes.
  - `generate-pot-file.yml` refreshes translations weekly.
- **Deployment** is by installing the app on a bench or Frappe Cloud. There is no deploy job in this repo.
- **Known limits:**
  - The push credential lacks the `workflow` scope, so workflow-file changes are deferred and applied by hand.
  - `biograph-fh` has no prior CI baseline.
