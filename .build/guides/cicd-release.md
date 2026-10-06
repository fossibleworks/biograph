---
title: CI/CD and release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/linters.v2.yml
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
  - .github/helper/install.sh
---

**Checks on pull requests** (GitHub Actions)
- `linters.v2.yml` runs on PRs, pushes and manual dispatch with Python 3.14 and Node 24. It runs **pre-commit** (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast/merge-conflict/debug-statement checks), and a separate **Semgrep** job with the Frappe semgrep rules plus `r/python.lang.correctness`. `linters.yml` is the older PR-only variant of the same checks.
- `semantic-commits.yml` runs commitlint over the PR's commits.
- `docs_checker.yml` makes `feat` PRs include a wiki docs link (or `no-docs`).
- `codeql.yml` runs CodeQL security analysis. `labeller.yml` applies PR labels (`.github/labeler.yml`).
- **Tests:** there is no test workflow in this fork yet. `.github/helper/install.sh` (bench, MariaDB and Redis setup; fork branches test against `version-16`) is ready for one. Codecov is configured for an 85% patch target.

**Release** (inherited from upstream earthians and targeting the `earthians/biograph` repo/secrets)
- `initiate_release.yml` runs weekly (Tuesday 09:30 UTC). It opens `chore: release vN` PRs from `version-N-hotfix` → `version-N` for 14, 15 and 16.
- `on_release.yml`: on a push to `version-14/15/16`, **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major release) bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` and `.github/release.yml` handle release-note generation.
- `generate-pot-file.yml` regenerates translation strings weekly on `develop`.
- `dependabot.yml` handles dependency updates.

**Deployment:** none happens from this repo. Sites install the app with `bench get-app` / `install-app` and `bench migrate`, or use Frappe Cloud.

For `biograph-fh`, the release workflows reference upstream branches and secrets, so treat them as inactive unless they are adapted.
