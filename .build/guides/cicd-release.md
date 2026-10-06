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
  - .github/workflows/linters.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .mergify.yml
  - codecov.yml
---

# CI/CD and release

## On pull requests
- **CI / Server Tests** (`ci.yml`): Ubuntu, Python 3.14, Node 24, a MariaDB 11.8 service. It runs `python -m compileall` and a merge-conflict-marker grep, bootstraps a bench with `.github/helper/install.sh`, then runs `bench --site test_site run-parallel-tests --app healthcare`. It skips PRs that only touch css/js/md/html/csv, ignores `version-**-beta`, and also runs nightly at 00:00 UTC. Coverage goes to Codecov on non-PR runs.
- **Linters** (`linters.yml`, `linters.v2.yml`): the pre-commit action runs ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets and yaml/json/toml/ast checks. Semgrep runs with Frappe rules plus `r/python.lang.correctness`.
- **Semantic Commits** (`semantic-commits.yml`): commitlint over the PR's commits.
- **Documentation Required** (`docs_checker.yml`): checks `feat` PRs for a docs link.
- **CodeQL**: Python and JavaScript, on PRs and pushes to `develop`, and weekly.
- **Labeler**: auto-labels PRs.
- Mergify auto-merges after at least 1 approval.

## Release (upstream-oriented)
- **Weekly release PRs** (`initiate_release.yml`, Tuesdays): open `version-N-hotfix → version-N` PRs for 14/15/16 on `earthians/biograph`.
- **semantic-release** (`on_release.yml` + `.releaserc`): on push to `version-14/15/16`, it bumps the version string in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release. Breaking changes do **not** auto-release a major version.
- **Release notes** (`release_notes.yml`): regenerate notes and strip chore/ci/test/docs/style lines.
- **POT file** (`generate-pot-file.yml`): weekly translation template refresh on `develop`.

## Caveats for this fork
Several workflows hard-code `earthians/biograph` and earthians bot secrets. On `fossibleworks/biograph`, `ci.yml` has never run (there is no baseline), so the first goal-PR CI run becomes the baseline. The push credential in sync sessions cannot modify `.github/workflows/*`. Changes to workflow files must be applied by hand.
