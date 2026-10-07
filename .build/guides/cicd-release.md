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
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - codecov.yml
---

**PR checks** (GitHub Actions):
- `ci.yml` (Server Tests):
  - Ubuntu with MariaDB 11.8, Python 3.14 and Node 24.
  - Runs `compileall` and a merge-conflict-marker scan.
  - `.github/helper/install.sh` sets up a bench with frappe, payments and erpnext on the matching branch (fork branches fall back to `version-16`) and installs `healthcare`.
  - Then `bench run-parallel-tests`.
  - Skips PRs that touch only css/js/md/html/csv.
  - Also runs nightly at 00:00 UTC; nightly runs upload coverage to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, eslint, prettier, detect-secrets, pip-audit, ...) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: `feat` PRs need a wiki docs link.
- `codeql.yml`: Python and JS analysis on `develop` and weekly.
- `labeller.yml`: auto-labels PRs.

**Release (upstream model, inherited):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` PRs for N = 14, 15, 16. It targets `earthians/biograph`.
- On push to `version-14/15/16`, `on_release.yml` runs **semantic-release** (`.releaserc`). This bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release. Breaking changes do not trigger a major release.
- `release_notes.yml` regenerates notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations weekly.

**Fork caveats:**
- Several workflows hard-code `earthians/biograph` and bot secrets, so they are effectively inert on `fossibleworks/biograph`.
- `biograph-fh` has no CI run history.
- The goal push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
- There is no deploy pipeline; deployment is via bench or Frappe Cloud (`bench get-app` / `install-app` / `migrate`).
