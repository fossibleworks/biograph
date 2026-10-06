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
  - .github/helper/install.sh
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
  - codecov.yml
---

# CI/CD and release

## PR checks (GitHub Actions)
- **CI / Server Tests** (`ci.yml`)
  - Runs on pull requests, skipping changes that touch only css, js, md, html or csv and skipping `version-*-beta` branches. Also runs nightly at 00:00 UTC.
  - Setup: Python 3.14, Node 24, a MariaDB 11.8 service, `python -m compileall`, and a merge-conflict-marker check.
  - `install.sh` bootstraps a bench with frappe, erpnext and payments. Fork branches such as `biograph-fh` and `goal/*` clone Frappe and ERPNext `version-16`.
  - Then runs `bench run-parallel-tests --app healthcare`. Coverage goes to Codecov only on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets, …) plus Frappe Semgrep rules.
- **Semantic Commits**: commitlint over the PR's commits.
- **Documentation Required**: `feat` PRs need a docs link. This is an upstream-oriented check.
- **CodeQL**, a **labeller**, and Dependabot.

## Release (inherited from upstream)
- `initiate_release.yml` opens a weekly PR (Tuesdays) from `version-N-hotfix` into `version-N` for N = 14, 15, 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset with breaking changes not auto-releasing.
  - It rewrites the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
  - It then creates the GitHub release. `release.yml` excludes PRs labelled `skip-release-notes` from the changelog.
- `generate-pot-file.yml` regenerates the translation template every week, and Crowdin opens translation PRs.
- Deployment runs through bench or Frappe Cloud (`bench get-app` + `install-app` / `migrate`). The repo has no deploy workflow.
- Several workflows point at the upstream `earthians/biograph` repo and its secrets. On the fork, the PR checks are what matter.
