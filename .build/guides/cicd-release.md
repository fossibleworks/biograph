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
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
  - codecov.yml
---

**PR checks (GitHub Actions):**
- **CI / Server Tests** (`ci.yml`)
  - triggers: PRs (skipped when only `.css`, `.js`, `.md`, `.html` or `.csv` files change, and for `version-**-beta` branches) and nightly at 00:00 UTC
  - environment: Ubuntu, MariaDB 11.8, Python 3.14, Node 24
  - steps:
    1. `compileall` and a merge-conflict-marker check
    2. `.github/helper/install.sh` (bench, frappe, erpnext and payments; fork branches use `version-16`)
    3. `bench run-parallel-tests --app healthcare`
  - coverage is uploaded to Codecov on non-PR runs
- **Linters** (`linters.yml` and `linters.v2.yml`): the pre-commit action (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, file checks) plus Semgrep with Frappe rules and `r/python.lang.correctness`.
- **Semantic Commits:** commitlint over the PR commit range.
- **Documentation Required:** `feat` PRs need a docs link, or `no-docs` / `backport` in the body.
- **CodeQL** (python and javascript) runs on `develop` pushes and PRs, plus weekly. **Labeler** adds `needs-tests`.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens a weekly (Tuesday) PR from `version-N-hotfix` to `version-N` for N = 14, 15, 16 against `earthians/biograph`.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16` (`.releaserc`: angular preset, breaking changes do not trigger a major release). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore, ci, test, docs and style entries.
- `generate-pot-file.yml` refreshes translations weekly on `develop`.

**Fork caveats:**
- Several workflows hard-code `earthians/biograph` and earthians bot tokens.
- According to the sync ledger, `ci.yml` has never run on `fossibleworks/biograph`, so there is no CI baseline.
- The goal-branch push credential cannot write `.github/workflows/*`. Workflow edits must be applied by hand (see B2 #86 in the ledger).
- Deployment is through Frappe Bench and Frappe Cloud (`bench get-app` / `install-app`, then `bench migrate` runs `patches.txt`). The repo has no deploy pipeline.
