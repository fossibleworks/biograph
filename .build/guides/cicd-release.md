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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
---

**On every PR:**
- **CI / Server Tests** (`ci.yml`) runs on Ubuntu with MariaDB 11.8, Python 3.14 and Node 24. It skips PRs that only touch css/js/md/html/csv.
  1. `compileall` and a conflict-marker check.
  2. `.github/helper/install.sh` bootstraps a bench (fork branches test against frappe/erpnext `version-16`).
  3. `bench run-parallel-tests --app healthcare`.
  4. A nightly cron runs coverage and uploads it to Codecov.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, eslint, prettier, pip-audit, detect-secrets) plus Semgrep with the frappe rules and `r/python.lang.correctness`.
- **Semantic Commits:** commitlint over the PR's commit range.
- **Documentation Required:** `feat` PRs need a wiki link or `no-docs`.
- **Labeler** applies labels. **CodeQL** (python and javascript) runs on develop pushes and PRs, plus weekly.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly `version-NN-hotfix → version-NN` release PRs (14, 15, 16) every Tuesday.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset with breaking-change major bumps disabled. It bumps `healthcare/__init__.py` with the commit `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml` regenerates release notes and strips chore, ci, test, docs and style entries.
- `generate-pot-file.yml` refreshes translations every Sunday. Crowdin opens `fix: sync translations from crowdin` PRs.

Several of these workflows hard-code `earthians/biograph` and bot tokens, so they only work upstream. Per the sync ledger, the fork (`fossibleworks/biograph`, branch `biograph-fh`) has no `ci.yml` run history. Editing workflow files needs a credential with the `workflow` scope.
