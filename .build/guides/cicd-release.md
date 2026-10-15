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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .github/workflows/codeql.yml
  - .releaserc
  - .github/release.yml
---

# CI/CD and release

## Pull request checks
- **CI / Server Tests** (`ci.yml`) runs on PRs, skipping changes that touch only css/js/md/html/csv, and nightly. Steps: `compileall` and a merge-conflict-marker check, bench install (`.github/helper/install.sh`) against MariaDB 11.8, then `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`) run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets, file checks) and semgrep with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** runs commitlint over the PR's commits.
- **Documentation Required** applies to `feat` PRs.
- **CodeQL** scans Python and JS on `develop` and weekly.
- **Labeler** adds `needs-tests`. Dependabot is configured.

## Release
- `initiate_release.yml` opens weekly `version-NN-hotfix → version-NN` release PRs on Tuesdays for v14, v15, and v16. It targets the upstream `earthians/biograph`.
- `on_release.yml` runs **semantic-release** (`.releaserc`, angular preset, breaking changes do not trigger major releases) on pushes to `version-14/15/16`. It bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore, ci, test, docs, and style entries. The `skip-release-notes` label excludes a PR.
- `generate-pot-file.yml` refreshes translation strings weekly. Crowdin opens `fix: sync translations from crowdin` PRs.

Several workflows hardcode `earthians/biograph` and the upstream `develop` branch. In this fork the default branch is `biograph-fh`, so branch-filtered jobs (CodeQL, Codecov patch target) may not trigger as written.
