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
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .github/workflows/codeql.yml
  - .github/helper/install.sh
  - codecov.yml
  - .github/release.yml
  - .github/dependabot.yml
---

**On every PR**
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast and merge-conflict checks) and Semgrep with the Frappe rules plus `r/python.lang.correctness`. v2 also runs on push.
- `semantic-commits.yml` runs commitlint over the PR's commit range.
- `ci.yml` (Server Tests) skips PRs that only touch css/js/md/html/csv and `version-**-beta` branches. It runs `compileall` and a merge-marker grep, then `.github/helper/install.sh`, which bench-inits Frappe, ERPNext and payments on the base branch with MariaDB 11.8 and installs healthcare on `test_site`. Finally it runs `bench run-parallel-tests --app healthcare` (30 min timeout).
- `docs_checker.yml` requires a docs link for `feat` PRs.
- `labeller.yml` adds the `needs-tests` label. `codeql.yml` analyses Python and JS on `develop`.

**Scheduled**
- Nightly CI with coverage uploaded to Codecov (patch target 85%).
- Weekly POT regeneration on `develop` (`generate-pot-file.yml`).
- Weekly `initiate_release.yml` (Tuesday) opens `version-NN-hotfix` → `version-NN` release PRs for 14, 15 and 16.

**Release**
- A push to `version-14/15/16` triggers `on_release.yml`, which runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not auto-major). It bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates notes and strips chore, ci, test, docs and style entries. PRs labelled `skip-release-notes` are excluded.
- Dependabot updates GitHub Actions weekly.
- Deployment is by `bench get-app` and `install-app` / `migrate` on Frappe sites (Frappe Cloud signup link in README). There is no container or deploy pipeline in this repo.

Note: several workflows still reference the upstream `earthians/biograph` repo and bot tokens.
