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
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
---

**PR checks (`.github/workflows/`):**
- `ci.yml` (**Server Tests**):
  - Runs on PRs and nightly. It ignores changes that touch only `**.css/js/md/html/csv` and skips `version-**-beta`.
  - Steps: Ubuntu with MariaDB 11.8, Python 3.14 and Node 24; `compileall` plus a merge-marker grep; `.github/helper/install.sh`; then `bench --site test_site run-parallel-tests --app healthcare`.
  - `install.sh` builds a bench against `frappe` at the base branch, or `version-16` for `biograph-fh` / `goal/*`.
  - Coverage goes to Codecov only on non-PR runs.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus **semgrep** with Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR's commits.
- `docs_checker.yml` makes `feat` PRs include a `/wiki` docs link, `no-docs` or `backport`. Note that it queries `earthians/biograph`.
- `labeller.yml` adds `needs-tests`.
- `codeql.yml` covers Python and JS on `develop`, plus a weekly run.
- Dependabot is configured in `.github/dependabot.yml`.

**Release (inherited from upstream earthians, targeting `version-14/15/16`):**
- `initiate_release.yml` opens a weekly `chore: release vN` PR from `version-N-hotfix` to `version-N`.
- `on_release.yml` runs **semantic-release** (`.releaserc`, angular preset, breaking changes do not trigger a major) on push to `version-14/15/16`. It bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml` regenerates release notes and strips `chore|ci|test|docs|style` entries. `.github/release.yml` excludes the `skip-release-notes` label.
- `generate-pot-file.yml` regenerates translations weekly on `develop`.

**Fork caveats:**
- `fossibleworks/biograph` has never run `ci.yml` on `biograph-fh`, so the first goal-PR run is the baseline.
- Release, notes and docs workflows hard-code the `earthians` owner and its tokens, so they are effectively upstream-only.
- The sync push credential cannot write `.github/workflows/*`. Workflow-file changes have to be applied by hand.
- Deployment is via Frappe bench or Frappe Cloud (`bench get-app` / `install-app`). There is no deploy workflow in this repo.
