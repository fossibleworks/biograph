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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
---

**On PRs:**
- `ci.yml` (Server Tests): compiles all Python, checks for merge-conflict markers, sets up a bench with frappe, payments, and erpnext (fork branches such as `biograph-fh` and `goal/*` test against `version-16`), installs `healthcare` on `test_site` with MariaDB 11.8, and runs `bench run-parallel-tests`. It skips PRs that only touch js/css/md/html/csv and also runs nightly. Coverage goes to Codecov on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: requires a docs link for `feat` PRs.
- `labeller.yml`: auto-labels PRs.
- `codeql.yml`: Python and JS analysis on develop and weekly.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly `version-1x-hotfix` → `version-1x` PRs for 14, 15, and 16.
- `on_release.yml` runs semantic-release on pushes to `version-14/15/16`. It uses the angular preset, rewrites the version in `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x`.
- `release_notes.yml` regenerates GitHub release notes. `generate-pot-file.yml` refreshes translations weekly.

The fork has no CI run history on `biograph-fh`, so the first goal-PR run sets the baseline. Pushing workflow-file changes needs a credential with the `workflow` scope.
