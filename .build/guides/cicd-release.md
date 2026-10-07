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
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .mergify.yml
---

## PR checks (GitHub Actions)

- **CI** (`ci.yml`) runs on PRs except to `version-**-beta`, and nightly. It is skipped for PRs that only touch js, css, md, html or csv. It sets up MariaDB, Python 3.14 and Node 24. `.github/helper/install.sh` builds a bench with frappe, erpnext and payments on the base branch; fork branches such as `biograph-fh` and `goal/*` fall back to `version-16`. It then runs `bench run-parallel-tests` in a matrix and uploads coverage to Codecov (coverage is collected only on non-PR runs).
- **Linters** (`linters.yml`, `linters.v2.yml`) run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets and others) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** runs commitlint on the PR commit range.
- **Documentation Required** fails `feat` PRs that have no wiki link and no `no-docs`.
- **Labeler** adds labels such as `needs-tests`. **CodeQL** runs on `develop` and weekly.

## Merge

Mergify auto-merges after at least 1 approval with CI green. The `squash` label switches to squash merge.

## Release

- `initiate_release.yml` opens weekly (Tuesday) release PRs for versions 14, 15 and 16, from hotfix to stable.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. `.releaserc` uses the angular preset (breaking changes do not trigger major releases), rewrites the version in `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x.y.z` along with a GitHub release.
- `release_notes.yml` generates notes for a tag. `generate-pot-file.yml` refreshes `main.pot` weekly.
- Deployment is via Frappe Cloud or `bench get-app` and `bench migrate`, which runs `patches.txt`.

**Note:** workflow-file changes may not be pushable by the automation credential (see the B2 #86 note in the sync ledger). The fork has no CI run history yet.
