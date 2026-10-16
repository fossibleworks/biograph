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
  - .github/workflows/linters.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .mergify.yml
  - .github/dependabot.yml
---

**GitHub Actions** (`.github/workflows/`):
- `ci.yml`: Server Tests. Runs on pull requests (except `version-**-beta`) and nightly at 00:00 UTC.
  - Setup: Python 3.14, Node 24, MariaDB 11.8 service. Bench installs through `.github/helper/install.sh`.
  - Then: `bench --site test_site run-parallel-tests --app healthcare`, and coverage is uploaded to Codecov (non-PR runs).
  - Skipped for changes that only touch `**.js`, `**.css`, `**.md`, `**.html` or `**.csv`. 30-minute timeout; concurrency cancels in-progress runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint on PR commit titles.
- `docs_checker.yml`: docs-link requirement for `feat` PRs.
- `codeql.yml`: CodeQL on develop and weekly.
- `labeller.yml`: PR labels (`.github/labeler.yml`).
- `generate-pot-file.yml`: weekly POT regeneration.
- `initiate_release.yml`: weekly (Tuesday) release PRs for versions 14, 15 and 16.
- `on_release.yml`: `npx semantic-release` on release branches.
- `release_notes.yml`: manual release-notes update by tag.

**Release:**
- `.releaserc` runs semantic-release on `version-14/15/16`, with the angular preset; breaking changes do not trigger a major bump.
- `@semantic-release/exec` bumps the version string in `healthcare/__init__.py`, and `@semantic-release/git` commits `chore(release): Bumped to Version x.y.z`.
- GitHub releases are created automatically.

**Merge automation:** Mergify merges once CI is green and the PR is approved.

**Dependency updates:** Dependabot updates GitHub Actions weekly.

**Fork caveat:** per the sync ledger, the fork `fossibleworks/biograph` has never run `ci.yml`, so there is no CI baseline on `biograph-fh`. Pushing workflow-file changes also requires a credential with `workflow` scope.
