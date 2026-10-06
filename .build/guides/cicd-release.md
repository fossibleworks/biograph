---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - codecov.yml
---

**On pull requests**
- **CI / Server Tests** (`ci.yml`) sets up a bench on Python 3.14 and Node 24 with a MySQL service, installs frappe, payments, and erpnext (fork branches map to `version-16` in `.github/helper/install.sh`), and runs `bench run-parallel-tests --app healthcare`. It skips PRs that only touch css/js/md/html/csv and branches named `version-**-beta`, and it also runs nightly. Coverage goes to Codecov on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`) run pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** checks PR and commit titles with commitlint.
- **Documentation Required** fails `feat` PRs that lack a wiki docs link (or `no-docs`).
- **Labeler**, plus **CodeQL** on `develop` and weekly.
- Editing `.github/workflows/*` needs a credential with the `workflow` scope. The sync ledger records B2 #86 as skipped for exactly this reason.

**Release**
- `initiate_release.yml` opens weekly release PRs for versions 14, 15, and 16 every Tuesday.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16` using the Angular preset (breaking changes don't trigger majors). It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and publishes a GitHub release.
- `release_notes.yml` updates notes for a given tag. `generate-pot-file.yml` regenerates the POT file weekly.
- Deployment is via `bench get-app` / Frappe Cloud. No container or deploy pipeline exists in the repo.
