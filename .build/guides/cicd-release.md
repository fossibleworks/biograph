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
  - .github/workflows/linters.v2.yml
  - .github/workflows/codeql.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
  - .github/dependabot.yml
---

**On PRs:**
- `ci.yml` runs the server tests. It sets up MariaDB 11.8, Python 3.14, and Node 24, runs `.github/helper/install.sh` to build a frappe-bench with erpnext, and runs `run-parallel-tests`. It is skipped for PRs that change only css/js/md/html/csv and for `version-*-beta` branches. It also runs nightly at 00:00 UTC, uploading coverage to Codecov on non-PR runs.
- `linters.yml` and `linters.v2.yml` run pre-commit and Semgrep (Frappe rules plus python correctness). v2 also runs on push.
- `semantic-commits.yml` lints commit messages.
- `docs_checker.yml` requires a docs link for `feat` PRs.
- `labeller.yml` applies labels such as `needs-tests`.
- `codeql.yml` runs CodeQL for python and javascript on `develop` and weekly.

**Release (inherited from upstream earthians and aimed at earthians/biograph):**
- `initiate_release.yml` opens weekly `version-N-hotfix` → `version-N` PRs for 14, 15, and 16.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. `.releaserc` uses the angular preset with breaking changes set to not trigger releases, bumps `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x`.
- `release_notes.yml` strips chore/ci/test/docs/style entries from the GitHub release notes.
- `generate-pot-file.yml` regenerates the POT file weekly.
- Dependabot is configured.

**Notes for the fork:**
- Many workflows hard-code `earthians/biograph` and earthians secrets.
- `fossibleworks/biograph` has never run `ci.yml` on `biograph-fh`.
- Deployment is via bench / Frappe Cloud, not a CD pipeline in this repo.
- Editing workflow files needs a credential with `workflow` scope (the ledger records upstream #86 as skipped for this reason).
