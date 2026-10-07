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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/dependabot.yml
---

**On pull requests:**
- **CI / Server Tests** (`ci.yml`) is skipped for PRs that only touch css/js/md/html/csv, and it also runs nightly. It compiles all Python, fails on merge-conflict markers, builds a bench with `.github/helper/install.sh` (MariaDB 11.8, Python 3.14, Node 24), then runs `bench run-parallel-tests --app healthcare`. Coverage is captured on scheduled runs and uploaded to Codecov.
- **Linters** (`linters.yml` and `linters.v2.yml`) run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) and **semgrep** with the Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** runs commitlint on the commit range.
- **Documentation Required** applies to `feat` PRs.
- **Labeler** adds `needs-tests`.
- **CodeQL** scans Python and JS on `develop` and weekly.

**Release (upstream style):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` PRs for 14, 15 and 16. Note that it targets `earthians/biograph`.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15`. The Angular preset bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release. Breaking changes do not trigger a major bump.
- `release_notes.yml` regenerates notes and strips chore/style entries.
- `generate-pot-file.yml` refreshes translation strings weekly.
- Dependabot is configured.

In this fork (`fossibleworks/biograph`), `ci.yml` has no run history yet, and the push credential cannot write workflow files.
