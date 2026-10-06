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
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/release.yml
  - codecov.yml
---

**On pull requests:**
- `ci.yml` (Server Tests) runs Python 3.14 and Node 24 against a MariaDB 11.8 service. It runs `compileall` plus a merge-conflict-marker scan, installs bench, frappe, payments and erpnext through `.github/helper/install.sh` (fork branches fall back to `version-16`), then runs `bench run-parallel-tests --app healthcare`. Paths matching css/js/md/html/csv are ignored. It also runs nightly, and nightly runs collect coverage for Codecov.
- `linters.yml` / `linters.v2.yml` run the pre-commit action (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, file checks) and **semgrep** with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR's commits.
- `docs_checker.yml` makes `feat` PRs link to `/wiki` docs or say `no-docs`.
- `codeql.yml` runs CodeQL for Python and JavaScript on `develop` and weekly.
- `labeller.yml` auto-labels PRs (`needs-tests`).
- Merging is handled by Mergify after at least 1 approval.

**Release (inherited from upstream earthians, wired to `version-14/15/16`):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` release PRs (Tuesdays).
- `on_release.yml` runs `npx semantic-release` on pushes to `version-*`. `.releaserc` uses the angular preset, sets breaking changes to not cut a major, bumps the version in `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes and strips chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded (`.github/release.yml`).
- `generate-pot-file.yml` regenerates `main.pot` weekly. Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork notes:** several workflows hard-code `earthians/biograph` and need upstream secrets (`EARTHIANS_BOT_TOKEN`, `RELEASE_TOKEN`). The ledger records that `ci.yml` has never run on `fossibleworks/biograph` `biograph-fh`. Editing `.github/workflows/*` needs a credential with the `workflow` scope.
