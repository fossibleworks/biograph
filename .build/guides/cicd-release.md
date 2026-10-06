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
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .mergify.yml
  - .github/helper/install.sh
---

**On pull requests:**
- `ci.yml` (Server Tests) skips PRs that only touch css, js, md, html or csv. Steps:
  1. Run `python -m compileall` and check for merge conflict markers.
  2. Run `.github/helper/install.sh`. It uses bench with frappe, payments and erpnext on the base branch, mapping fork or goal branches to `version-16`, against MariaDB 11.8.
  3. Run `bench run-parallel-tests --app healthcare`.
  It also runs nightly at 00:00 UTC, and those scheduled runs upload coverage to Codecov.
- `linters.yml` and `linters.v2.yml` run pre-commit (ruff, eslint, prettier, pip-audit, detect-secrets…) and semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR commit range.
- `docs_checker.yml` requires a wiki docs link for `feat` PRs.
- `labeller.yml` applies labels via `.github/labeler.yml`.
- `codeql.yml` runs CodeQL for Python and JS, on `develop` and weekly.
- **Mergify** auto-merges on CI success plus review, and auto-closes non-maintainer PRs to stable branches.

**Release (upstream model):**
- `initiate_release.yml` opens a weekly (Tuesday) PR from `version-NN-hotfix` to `version-NN` for 14, 15 and 16.
- `on_release.yml` runs on pushes to `version-14/15/16` and executes **semantic-release** (`.releaserc`). It uses the angular preset (breaking changes don't trigger a major release), rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version X`, and creates the GitHub release.
- `release_notes.yml` regenerates notes and strips chore, ci, test, docs and style entries.
- `generate-pot-file.yml` refreshes translations weekly.

**Fork caveats:** several workflows hard-code `earthians/biograph` and its bot tokens, so they are inert on `fossibleworks/biograph`. `ci.yml` has never run on `biograph-fh`. Editing `.github/workflows/*` needs a credential with `workflow` scope, which the sync automation lacks (B2 #86). There is no deploy pipeline. Deployment means `bench get-app` and `install-app`/`migrate` on Frappe Cloud or self-hosted benches.
