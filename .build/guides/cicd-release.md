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
  - .github/workflows/codeql.yml
---

**Runs on PRs**
- `ci.yml` (Server Tests): compileall plus a merge-conflict-marker check. It then sets up a bench with MariaDB 11.8 through `.github/helper/install.sh` and runs `bench run-parallel-tests --app healthcare`. It skips PRs that only touch css/js/md/html/csv, and also runs nightly. Nightly runs collect coverage and upload it to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a wiki docs link.
- `labeller.yml`: labels such as `needs-tests`.
- `codeql.yml`: Python and JS analysis on `develop`, plus weekly.

**Release (inherited from upstream earthians config)**
- `initiate_release.yml` opens weekly `version-NN-hotfix` → `version-NN` release PRs for v14/15/16.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. Per `.releaserc`, it uses the angular preset, never bumps majors automatically (breaking → no release), rewrites the version in `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes without chore/ci/test/docs/style entries. `.github/release.yml` excludes the `skip-release-notes` label.
- `generate-pot-file.yml` regenerates translations weekly.

Note: according to the sync ledger, `ci.yml` has never run on `fossibleworks/biograph`, so the first goal-PR run becomes the baseline. The release workflows target upstream `earthians/biograph` with upstream secrets.
