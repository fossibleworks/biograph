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
  - .releaserc
  - .github/workflows/initiate_release.yml
  - codecov.yml
---

# CI/CD and release

## Workflows (`.github/workflows`)
- **ci.yml (Server Tests):**
  - Runs on PRs, skipping `.js`, `.css`, `.md`, `.html` and `.csv`-only changes and `version-*-beta` bases. It also runs nightly at 00:00 UTC.
  - Uses Ubuntu, a MariaDB 11.8 service, Python 3.14 and Node 24.
  - `.github/helper/install.sh` builds a bench (frappe, payments, erpnext), installs the app and reinstalls `test_site`. Then `run-parallel-tests` runs, with coverage artifacts going to Codecov.
  - 30-minute timeout.
- **linters.yml / linters.v2.yml:** the pre-commit action (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets), plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- **semantic-commits.yml:** commitlint across the PR's commits.
- **codeql.yml:** on `develop` and weekly.
- **docs_checker.yml:** `feat` PRs need a wiki docs link or `no-docs`.
- **labeller.yml:** path labels such as `needs-tests`.
- **generate-pot-file.yml:** weekly POT regeneration.

## Release
- **on_release.yml:** `npx semantic-release` on the `version-14/15/16` branches (`.releaserc`):
  - angular preset; breaking changes don't trigger a major release
  - `@semantic-release/exec` bumps `healthcare/__init__.py`
  - commits `chore(release): Bumped to Version X`
  - publishes a GitHub release
- **initiate_release.yml:** weekly (Tuesday) release PRs for versions 14, 15 and 16. **release_notes.yml** regenerates notes for a tag.
- The fork also bumps the version by hand to follow upstream (`chore: bump version to 16.0.8`).

## Caveats for this fork
- Several workflows still target upstream names (`develop`, `earthians/biograph`).
- `biograph-fh` has no CI run history, so the first goal-PR run is the baseline.
- The automation credential can't push changes under `.github/workflows/`. Workflow edits must be applied by hand (see upstream sync item B2 #86).
- Deployment goes through Frappe Cloud / bench (`bench get-app`, `install-app`, `migrate`). No deploy job exists in the repo.
