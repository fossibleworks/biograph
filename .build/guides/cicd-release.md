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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
  - healthcare/__init__.py
---

**On pull requests (GitHub Actions):**
- `ci.yml` (Server Tests): runs `compileall` and a merge-conflict-marker check, installs bench, frappe and erpnext through `.github/helper/install.sh`, then runs `bench run-parallel-tests --app healthcare` on MariaDB 11.8 with Python 3.14 and Node 24. It skips PRs that only touch css/js/md/html/csv, and also runs nightly. Coverage goes to Codecov on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a docs link.
- `labeller.yml`: auto-labels such as `needs-tests`.
- `codeql.yml`: Python and JS analysis on `develop` plus a weekly run.

**Release (inherited from upstream earthians):**
- `initiate_release.yml`: every Tuesday it opens `version-N-hotfix → version-N` PRs for N = 14, 15, 16.
- `on_release.yml`: on push to `version-14/15/16`, `npx semantic-release` (`.releaserc`, angular preset; breaking changes do not trigger a major bump) bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates release notes and strips chore/ci/test/docs/style entries. The `skip-release-notes` label excludes PRs (`.github/release.yml`).
- `generate-pot-file.yml`: weekly POT regeneration. Crowdin opens translation PRs.

**Fork caveats:** several workflows hard-code `earthians/biograph` and the `develop` branch. Per the sync ledger, this fork (`biograph-fh`) has never run `ci.yml`. Deployment is bench- or Frappe Cloud-based (`bench get-app` / `install-app`). There is no in-repo deploy pipeline. The current version is 16.0.8.
