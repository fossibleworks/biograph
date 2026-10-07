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

**On every PR**
- `ci.yml` (Server Tests):
  - Skipped when a PR changes only css/js/md/html/csv files.
  - Also runs nightly at 00:00 UTC.
  - Steps: Python 3.14, Node 24, MariaDB 11.8, then `compileall`, then a conflict-marker grep, then `.github/helper/install.sh`. That script sets up a bench with frappe, payments and erpnext. It uses the PR base branch, and fork branches such as `biograph-fh` and `goal/*` fall back to `version-16`.
  - Then `install-app healthcare`, then `run-parallel-tests`.
  - Coverage is uploaded to Codecov only on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: docs link required for `feat` PRs.
- `labeller.yml`: adds `needs-tests` when relevant.
- `codeql.yml`: Python and JS analysis for `develop` and weekly.
- Dependabot is configured in `.github/dependabot.yml`.

**Release (inherited from upstream earthians):**
- `initiate_release.yml`: every Tuesday, opens `version-1X-hotfix` → `version-1X` release PRs.
- `on_release.yml`: on push to `version-14/15/16`, runs `npx semantic-release` (`.releaserc`, angular preset, breaking changes don't bump major). It rewrites the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml`: regenerates GitHub release notes and strips chore, ci, test, docs and style entries. `.github/release.yml` excludes the `skip-release-notes` label.
- `generate-pot-file.yml`: weekly POT refresh.

**Caveats**
- The release, POT and initiate workflows target `earthians/biograph` with earthians bot tokens, so they don't apply to the fork as written.
- There is no deploy pipeline in the repo. Deployment happens via bench or Frappe Cloud.
- The fork has no CI history on `biograph-fh` yet.
- Changes under `.github/workflows/` can't be pushed by the sync credential, which lacks workflow scope.
