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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/linters.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/dependabot.yml
---

**On every PR** (`.github/workflows`)
- **CI / Server Tests** (`ci.yml`)
  - Skips PRs that only touch css, js, md, html or csv files. Also runs nightly at 00:00 UTC.
  - Runs on Ubuntu with Python 3.14, Node 24 and a MariaDB 11.8 service, with a 30-minute timeout.
  - Steps: `compileall`, then the merge-marker grep, then `.github/helper/install.sh` (sets up the bench; fork branches like `biograph-fh` and `goal/*` test against Frappe/ERPNext `version-16`), then `bench run-parallel-tests --app healthcare`.
  - Coverage is uploaded to Codecov only on non-PR runs.
- **Linters**
  - `linters.v2.yml` runs on PR, push and dispatch: the pre-commit action plus Semgrep with Frappe rules and `r/python.lang.correctness`.
  - `linters.yml` is an older PR-only duplicate.
- **Semantic Commits**: commitlint over the PR's commits.
- **Documentation Required**: checks `feat:` PRs for a docs link.
- **PR Labeler**: adds `needs-tests`.
- **CodeQL**: Python and JS, on `develop` pushes and PRs, plus weekly.

**Release** (upstream-oriented: workflows target the `earthians/biograph` repo and bot tokens)
- `initiate_release.yml`: every Tuesday it opens `version-NN-hotfix` → `version-NN` PRs for versions 14, 15 and 16.
- `on_release.yml`: on push to `version-14`, `version-15` or `version-16`, runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major release). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates release notes and strips chore, ci, test, docs and style entries. `.github/release.yml` excludes `skip-release-notes` items.
- `generate-pot-file.yml`: weekly POT regeneration. Crowdin opens translation PRs.
- Dependabot updates GitHub Actions weekly.

**Fork notes**
- `biograph-fh` has no CI history (see the wiki ledger), so the first goal-PR run is the baseline.
- The credential that pushes goal branches **cannot modify `.github/workflows/`**. Workflow changes must be applied by hand.
- Deployment is through bench and Frappe Cloud (README "Try on Frappe Cloud"). The repo contains no deploy pipeline.
