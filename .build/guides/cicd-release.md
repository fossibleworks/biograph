---
title: CI/CD & release
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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

**Workflows in `.github/workflows/`:**
- **CI (`ci.yml`):** runs on PRs (except `version-*-beta`), skipping PRs that only change css/js/md/html/csv, plus a nightly cron. Steps:
  - Ubuntu with MariaDB and Python 3.14 / Node 24
  - `.github/helper/install.sh` sets up a bench with frappe, erpnext, and payments. Fork branches such as `biograph-fh` and `goal/*` test against `version-16`.
  - Runs `bench run-parallel-tests --app healthcare` in a matrix and uploads coverage to Codecov.
- **Linters (`linters.yml`, `linters.v2.yml`):** pre-commit (ruff, prettier, eslint, detect-secrets, pip-audit, file checks) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- **Semantic Commits:** commitlint on commit titles.
- **Documentation Required (`docs_checker.yml`):** `feat` PRs need a docs link.
- **CodeQL:** on `develop` and weekly.
- **Labeler:** applies PR labels automatically.
- **Generate POT file:** weekly translation template refresh.

**Release:**
- `initiate_release.yml` opens weekly release PRs on a cron.
- `on_release.yml` runs `npx semantic-release` on `version-14/15/16`:
  - the angular preset computes the version (breaking changes do not trigger a major release)
  - `.releaserc` rewrites the version in `healthcare/__init__.py`
  - commits `chore(release): Bumped to Version x.y.z` and publishes a GitHub release
- `release_notes.yml` regenerates notes for a tag.

**Merging:** Mergify merges once there is ≥1 approval and CI passes. Codecov gates patch coverage at 85%.

**Deployment:** none from this repo. Sites pull the app via `bench get-app` or Frappe Cloud.

**Fork caveat:** `ci.yml` has never run on `biograph-fh`, so there is no baseline. The push credential cannot write workflow files, so workflow changes must be applied by hand.
