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
  - .github/workflows/linters.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - codecov.yml
---

**PR checks (GitHub Actions):**
- **CI / Server Tests** (`ci.yml`): runs on PRs that change more than css, js, md, html or csv files, and nightly at 00:00 UTC. It compile-checks Python and greps for merge-conflict markers. `.github/helper/install.sh` builds a bench with frappe, payments and erpnext. Fork branches (`biograph-fh`, `goal/*`) are tested against `version-16`. Then it installs healthcare and runs `bench run-parallel-tests --app healthcare` on MariaDB 11.8. Coverage is uploaded to Codecov on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) and Frappe semgrep rules plus `r/python.lang.correctness`.
- **Semantic Commits:** commitlint over the PR's commit range.
- **Documentation Required:** `feat` PRs need a docs link or `no-docs`.
- CodeQL, the labeller, and Dependabot.

**Release (upstream model, kept in the fork):**
- `initiate_release.yml`: every Tuesday it opens PRs from `version-1x-hotfix` into `version-1x` for 14, 15 and 16 (this targets earthians/biograph).
- `on_release.yml`: on push to `version-14/15/16`, `semantic-release` (angular preset; breaking changes don't trigger a major bump) writes the version into `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` tidies the release notes. `generate-pot-file.yml` regenerates translations weekly.
- Deployment is to Frappe Cloud / bench sites via `bench get-app` and `install-app`. Schema changes ship as patches registered in `patches.txt`.

Fork caveat: the ledger records that `ci.yml` had never run on `biograph-fh`, so the first goal-PR run is the baseline. Edits to workflow files need a token with the `workflow` scope.
