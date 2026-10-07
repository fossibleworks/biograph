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
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
---

# CI/CD & release

## On pull requests
- **CI / Server Tests** (`ci.yml`):
  - Ubuntu with a MariaDB 11.8 service, Python 3.14 and Node 24.
  - Runs `compileall` and checks for merge-conflict markers.
  - Builds a bench via `.github/helper/install.sh` (frappe + payments + erpnext + healthcare), then runs `bench run-parallel-tests --app healthcare`.
  - Skipped for PRs that only touch css/js/md/html/csv. Also runs nightly at 00:00 UTC.
  - Coverage is uploaded to Codecov only on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`, which also runs on push): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, file checks) and Semgrep with the Frappe rules + `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR range.
- **Documentation Required**: `docs_checker.yml`.
- **CodeQL**: `codeql.yml`.
- **Labeller**: `labeller.yml` + `.github/labeler.yml`.
- Dependabot is configured in `.github/dependabot.yml`.

## Release (upstream model, inherited)
- `initiate_release.yml` opens weekly (Tuesday) `chore: release vN` PRs from `version-N-hotfix` → `version-N` for N = 14, 15, 16.
- `on_release.yml` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger major bumps) on pushes to `version-14/15/16`. It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates the GitHub release.
- `release_notes.yml` + `.github/release.yml` generate notes and exclude PRs labelled `skip-release-notes`.
- `generate-pot-file.yml` regenerates translations weekly on `develop`. Crowdin opens translation PRs.

## Fork caveats
- Several workflows still reference `earthians/biograph` and the `EARTHIANS_BOT_TOKEN` secret.
- The fork's `biograph-fh` branch has no CI history yet.
- Pushes that modify `.github/workflows/*` need a token with workflow scope (see the B2 #86 note in the sync ledger).
- Deployment is by `bench get-app` / Frappe Cloud. This repo has no deploy pipeline.
