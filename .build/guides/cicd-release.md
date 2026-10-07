---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/codeql.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - codecov.yml
---

**PR checks** (`.github/workflows/`)
- **CI / Server Tests** (`ci.yml`) runs on PRs, except PRs touching only css/js/md/html/csv and branches matching `version-*-beta`, and nightly at 00:00 UTC. Steps: `compileall` and a merge-conflict-marker grep, then a bench install with Python 3.14, Node 24, and a MariaDB 11.8 service (`.github/helper/install.sh`), then `bench --site test_site run-parallel-tests --app healthcare`. The timeout is 30 min. Coverage is uploaded to Codecov only on non-PR runs (`fail_ci_if_error`).
- **Linters** (`linters.yml`, `linters.v2.yml`) run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** (`semantic-commits.yml`) runs commitlint.
- **Documentation Required** (`docs_checker.yml`): `feat` PRs need a wiki link.
- **CodeQL** (python, javascript) runs on `develop` pushes and PRs, plus weekly.
- **Labeler** (`labeler.yml`) adds `needs-tests`.

**Release** (inherited from upstream earthians and configured for `version-14/15/16`)
- `initiate_release.yml` opens weekly (Tue) PRs from `version-N-hotfix` to `version-N`.
- `on_release.yml`: a push to `version-14/15/16` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger major releases). It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates notes, stripping chore/ci/test/docs/style entries.
- `generate-pot-file.yml` regenerates the POT file weekly. Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork notes:** the fork's default branch is `biograph-fh`, which matches none of the release branch triggers. Several workflows hard-code `earthians/biograph` and earthians secrets. The fork had no `ci.yml` run history, and the first goal-PR run is the baseline. The workflow-file change from upstream sync B2 #86 could not be pushed because the push credential lacks workflow scope, so apply `.github/workflows/*` changes by hand.

Deployment itself is outside this repo. Sites install the app through bench / Frappe Cloud.
