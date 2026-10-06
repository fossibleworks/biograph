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
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
  - codecov.yml
---

**On every PR**
- `ci.yml` (Server Tests) runs Ubuntu with Python 3.14, Node 24 and MariaDB 11.8. Steps: `compileall`, a merge-conflict-marker check, then `.github/helper/install.sh`. That script runs bench init and installs frappe, payments and erpnext on the matching branch (or version-16 for fork branches), then installs healthcare. Finally `bench run-parallel-tests --app healthcare`, with a 30-minute timeout. PRs touching only css, js, md, html or csv files skip this workflow. It also runs nightly on cron `0 0 * * *` and uploads coverage to Codecov.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a docs link.
- `codeql.yml` (security scanning) and `labeller.yml` (labels from `.github/labeler.yml`).

**Release** (upstream-style, earthians bot token)
- `initiate_release.yml` opens weekly release PRs every Tuesday 09:30 UTC, from `version-1x-hotfix` into `version-1x` for 14, 15 and 16.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. `.releaserc` uses the angular preset, where breaking changes do not trigger a release. It bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates the GitHub release.
- `release_notes.yml` and `.github/release.yml` build the changelog. The `skip-release-notes` label excludes a PR.
- `generate-pot-file.yml` regenerates translations weekly. Dependabot (`.github/dependabot.yml`) handles dependency bumps.
- On the fork, manual version bumps also happen (`chore: bump version to 16.0.8`). The sync ledger notes the fork had no CI history before the B2 batch.
