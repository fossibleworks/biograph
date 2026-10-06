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
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

# CI/CD and release

## On pull requests
| Workflow | What it does |
|---|---|
| `ci.yml` (**Server Tests**) | Python 3.14 + Node 24 + MariaDB 11.8. Runs `compileall`, checks for merge-conflict markers, sets up a bench via `.github/helper/install.sh`, then runs `bench run-parallel-tests --app healthcare`. It skips PRs that only touch css/js/md/html/csv, also runs nightly at 00:00 UTC, and uploads coverage to Codecov on non-PR runs. |
| `linters.yml` / `linters.v2.yml` | pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, file checks) + Semgrep with `frappe/semgrep-rules` and `r/python.lang.correctness` |
| `semantic-commits.yml` | commitlint on every commit in the PR range |
| `docs_checker.yml` | `feat` PRs need a `/wiki` docs link (or `no-docs` / `backport`) |
| `codeql.yml` | CodeQL for python + javascript (PRs to develop + weekly) |
| `labeller.yml` | Auto-labels PRs via `.github/labeler.yml` |

## Merge and release
- **Mergify** auto-merges after 1 approval and handles backports through labels.
- `initiate_release.yml` (weekly on Tuesday) opens `version-N-hotfix → version-N` release PRs for versions 14, 15, and 16. Note that it targets the upstream `earthians/biograph` repo.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset with breaking changes not auto-releasing. It rewrites `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version X`, and creates the GitHub release. `release_notes.yml` and `.github/release.yml` shape the release notes.
- `generate-pot-file.yml` regenerates translations weekly. Dependabot updates GitHub Actions weekly.
- Deployment is outside this repo, by `bench get-app` / Frappe Cloud.

**Fork caveat:** per the sync ledger, `fossibleworks/biograph` has no `ci.yml` run history on `biograph-fh`. Treat CI results as new signal, not as a regression baseline. Pushing changes to `.github/workflows/*` requires a credential with workflow scope.
