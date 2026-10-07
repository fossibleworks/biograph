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
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - .mergify.yml
---

# CI/CD & release

## On pull requests
- **CI / Server Tests** (`ci.yml`):
  - Skips PRs that only touch css/js/md/html/csv. Also runs nightly at 00:00 UTC.
  - Checks: `compileall`, then a scan for merge-conflict markers.
  - Bench install via `.github/helper/install.sh` against MariaDB 11.8, then `bench run-parallel-tests --app healthcare`.
  - Coverage is uploaded to Codecov on non-PR runs only.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, hygiene) and semgrep with Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR range.
- **Documentation Required**: `feat` PRs need a docs link or `no-docs`.
- **Labeler**: auto-labels PRs. **CodeQL**: runs on develop pushes and PRs, plus weekly.
- Mergify auto-merges after approval and green CI.

## Release
- `initiate_release.yml` opens a release PR every **Tuesday**, from `version-1x-hotfix` into `version-1x` for 14/15/16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. `.releaserc` uses the Angular preset, and breaking changes do not trigger a major bump.
  - It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and publishes a GitHub release.
- `release_notes.yml` / `.github/release.yml` generate release notes.
- `generate-pot-file.yml` refreshes translatable strings weekly on Sunday. Crowdin opens `fix: sync translations from crowdin` PRs.

## Fork caveats
- Several workflows still point at `earthians/biograph` with earthians bot tokens.
- `biograph-fh` has no CI run history yet.
- The current push credential cannot modify `.github/workflows/*`. Workflow edits must be applied by hand.
