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
  - .releaserc
  - .github/release.yml
  - codecov.yml
---

## On pull requests
- **CI / Server Tests** (`ci.yml`): Ubuntu, Python 3.14, Node 24, MariaDB 11.8. Runs `compileall` and a merge-marker check. `.github/helper/install.sh` sets up a bench (fork branches such as `biograph-fh` and `goal/*` test against frappe/erpnext/payments `version-16`), then runs `bench run-parallel-tests --app healthcare`. The job skips PRs that only change css/js/md/html/csv and times out after 30 minutes. It also runs nightly on cron, and that run uploads coverage to Codecov.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits:** commitlint over the PR's commit range.
- **Documentation Required:** `feat:` PRs need a wiki link or `no-docs`.
- **CodeQL** and the **labeller** run as well.

## Release (inherited from earthians upstream)
- `initiate_release.yml` opens a `chore: release vN` PR from `version-N-hotfix` to `version-N` (N = 14, 15, 16) every Tuesday.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. It uses the Angular preset, breaking changes don't trigger a release, and it bumps `healthcare/__init__.py` and creates a GitHub release with notes. `release.yml` excludes PRs labelled `skip-release-notes` from the changelog.
- `generate-pot-file.yml` regenerates `main.pot` weekly. Crowdin opens `fix: ... translations` PRs.
- Several workflows hard-code `earthians/biograph` and bot tokens, so they are effectively inactive on the fork. The fork has no deploy step: deployment means `bench get-app` / `bench migrate` on Frappe Cloud or self-hosted benches.
- Note: the fork has no ci.yml run history. The push credential cannot change `.github/workflows/*`, so workflow edits must be applied by hand.
