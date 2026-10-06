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
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - codecov.yml
---

**PR checks (GitHub Actions)**
- `ci.yml` (**Server Tests**) runs on PRs that touch more than css/js/md/html/csv, and nightly.
  - It sets up Python 3.14, Node 24 and MariaDB 11.8, compiles all Python, and greps for merge-conflict markers.
  - Then `.github/helper/install.sh` builds a bench with frappe, payments and erpnext. It uses the PR base branch, or `version-16` for fork branches such as `biograph-fh` and `goal/*`.
  - Finally it runs `bench run-parallel-tests --app healthcare`. Non-PR runs upload coverage to Codecov.
- `linters.yml` and `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit) and Frappe semgrep rules.
- `semantic-commits.yml` runs commitlint on PR commit titles.
- `docs_checker.yml` requires a wiki link on `feat` PRs.
- `labeller.yml` adds the `needs-tests` label.
- `codeql.yml` runs Python and JS analysis on `develop`, plus a weekly run.
- Dependabot handles action updates.

**Release (inherited from upstream earthians)**
- semantic-release (`.releaserc`, angular preset) runs on pushes to `version-14/15/16`. It bumps `healthcare/__init__.py` with the commit `chore(release): Bumped to Version x.y.z`. Breaking changes do not trigger major releases.
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` PRs.
- `release_notes.yml` regenerates notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations weekly.
- Several of these workflows target the `earthians/biograph` repo and need secrets this fork may not have.
- The fork bumps its version by hand on `biograph-fh`, for example `chore: bump version to 16.0.8`.
- Pushes cannot change workflow files without the `workflow` token scope. Such changes are deferred and applied by hand.
