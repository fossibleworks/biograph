---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - codecov.yml
  - .mergify.yml
---

**On every PR** (GitHub Actions):
- `linters.yml` / `linters.v2.yml` (v2 also runs on push and dispatch): run pre-commit on Python 3.14 and Node 24 (ruff, ruff-format, eslint, prettier, pip-audit, detect-secrets, yaml/json/toml/ast checks), then Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: `feat` PRs need a docs link or `no-docs`.
- `codeql.yml`: CodeQL security scan. `labeller.yml`: auto-labels.
- Codecov gates: 85% patch coverage, and project coverage may drop by at most 0.5%.
- **No server-test workflow** is present on the fork. `.github/helper/install.sh` is the bench setup script for one. Adding workflow files needs a credential with `workflow` scope (see B2 #86 in the sync ledger).

**Release (inherited from upstream):**
- `initiate_release.yml` opens a weekly (Tuesday 09:30 UTC) `chore: release vN` PR from `version-N-hotfix` to `version-N` for N = 14/15/16.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16`. It uses the angular preset, bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates the GitHub release. Breaking changes do not trigger a major release.
- `release_notes.yml` and `.github/release.yml` build the changelog (excluding the `skip-release-notes` label).
- `generate-pot-file.yml` regenerates translations weekly.
- Mergify auto-closes PRs aimed directly at stable `version-*` branches.
- Deployment target: Frappe Cloud (the README has a "try on Frappe Cloud" link).
