---
title: CI/CD & Release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
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
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/release.yml
  - .mergify.yml
---

**On pull requests** (GitHub Actions):
- **CI / Server Tests** (`ci.yml`)
  - Skips PRs that only touch css/js/md/html/csv. Also runs nightly at 00:00 UTC.
  - Setup: Python 3.14 + Node 24 + MariaDB 11.8. Runs `compileall` and checks for merge-conflict markers. `.github/helper/install.sh` builds a frappe-bench with frappe, erpnext and payments on the **same branch name as the PR base**, then installs `healthcare`.
  - Then runs `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, and others) and Frappe semgrep rules + `r/python.lang.correctness`.
- **Semantic Commits** (`semantic-commits.yml`): runs commitlint over the PR's commits.
- **Documentation Required** (`docs_checker.yml`): `feat` PRs need a wiki link or `no-docs`.
- **CodeQL** (python, javascript) runs on PRs and pushes to `develop`, and weekly.
- **Labeler:** adds `needs-tests` to Python changes that don't touch tests.

**Release** (inherited from upstream earthians):
- `initiate_release.yml` opens weekly (Tuesday) `chore: release vNN` PRs from `version-NN-hotfix` → `version-NN` for 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, configured by `.releaserc` (angular preset; breaking changes do not trigger major bumps). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries. The `skip-release-notes` label excludes a PR.
- `generate-pot-file.yml` regenerates translation strings weekly on `develop`. Crowdin opens `fix: sync translations from crowdin` PRs.
- Dependabot updates GitHub Actions weekly.
- Mergify auto-merges after approval + CI.

**Caveats:**
- Several workflows hard-code `earthians/biograph` and the `develop` / `version-*` branches. In this fork, the default branch is `biograph-fh`.
- `install.sh` clones frappe/erpnext at the base-branch name, so CI for PRs into `biograph-fh` may need that branch mapping adjusted.
- Deployment itself happens outside this repo (Frappe Cloud / bench `get-app` + `migrate`).
