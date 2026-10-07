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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - codecov.yml
  - .github/dependabot.yml
---

**GitHub Actions** (`.github/workflows/`):
- `ci.yml` runs **Server Tests** on PRs (skipped for js/css/md/html/csv-only changes and `version-**-beta` branches) and nightly at 00:00 UTC. It uses Python 3.14 and Node 24, installs a bench via `.github/helper/install.sh`, runs `bench run-parallel-tests --app healthcare`, and uploads coverage to Codecov in a wrap-up job.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and Frappe semgrep rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR commit range.
- `docs_checker.yml` runs the Documentation Required check for `feat` PRs.
- `codeql.yml` runs CodeQL on `develop` and weekly.
- `labeller.yml` labels PRs automatically.
- `generate-pot-file.yml` regenerates translations weekly (Sunday).

**Release:**
- `initiate_release.yml` opens weekly release PRs (Tuesday) for the version-14, version-15 and version-16 lines.
- `on_release.yml` runs `npx semantic-release` on the release branches. `.releaserc` uses the angular preset, with breaking changes configured not to trigger a major bump. It bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes for a given tag.
- Dependabot (`.github/dependabot.yml`) keeps dependencies up to date.

Caveat: the `fossibleworks` fork (`biograph-fh`) has no recorded `ci.yml` runs yet (see the sync ledger). Some helpers, such as the docs checker, still point at upstream repos. Changes to workflow files require a credential with `workflow` scope.
