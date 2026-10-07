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
  - .github/workflows/release_notes.yml
  - .github/helper/install.sh
  - .mergify.yml
  - .github/dependabot.yml
---

# CI/CD and release

## On pull requests
| Workflow | What it does |
|---|---|
| `ci.yml` (Server Tests) | Runs `compileall` and a merge-marker check. Bootstraps a bench (`.github/helper/install.sh`, MariaDB 11.8, frappe/erpnext/payments on the base branch, or `version-16` for fork branches like `biograph-fh`/`goal/*`). Then runs `bench run-parallel-tests --app healthcare`. Skips PRs that only touch js/css/md/html/csv and `version-*-beta` branches. Also runs nightly at 00:00 UTC with coverage → Codecov. |
| `linters.yml` / `linters.v2.yml` | pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, basic checks) + semgrep with Frappe rules and `r/python.lang.correctness`. |
| `semantic-commits.yml` | commitlint over the PR commit range. |
| `docs_checker.yml` | `feat` PRs must link docs. |
| `codeql.yml` | CodeQL for python and javascript (PRs and pushes to develop, weekly). |
| `labeller.yml` | Adds a `needs-tests` label. |

Mergify merges once there is at least 1 approval and CI passes, using merge or squash depending on the label.

## Release (upstream model)
- `initiate_release.yml` (weekly, Tue 09:30 UTC): opens `version-NN-hotfix` → `version-NN` PRs for 14/15/16.
- `on_release.yml`: runs semantic-release on pushes to `version-14/15/16`. It uses the angular preset (breaking changes do not trigger major bumps), rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates notes and strips chore/ci/test/docs/style entries. The `skip-release-notes` label excludes a PR.
- `generate-pot-file.yml` (weekly): refreshes `main.pot`. Crowdin opens translation PRs.
- Dependabot is configured.

## Fork notes
- Several workflows still point at `earthians/biograph` (release, docs checker) and at the `develop` branch. On `fossibleworks/biograph`, the `biograph-fh` trunk has no CI run history.
- Workflow-file edits need a push credential with `workflow` scope (upstream sync B2 #86 was skipped for this reason).
- Deployment is to Frappe Cloud or a bench (`bench get-app` / `install-app`, then `bench migrate` runs `patches.txt`).
