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
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/release.yml
---

# CI/CD and release

## On pull requests
- **CI (`ci.yml`)**: runs server tests. It skips PRs that change only css/js/md/html/csv, and it also runs nightly at 00:00 UTC. Steps:
  1. `python -m compileall` plus a merge-conflict-marker grep.
  2. `.github/helper/install.sh` builds a bench. Fork branches (`biograph-fh`, `goal/*`) are tested against frappe/erpnext `version-16`.
  3. `bench run-parallel-tests --app healthcare` on MariaDB 11.8, Python 3.14, Node 24. 30-minute timeout.
  4. Coverage goes to Codecov on non-PR runs only.
- **Linters (`linters.yml`, `linters.v2.yml`)**: pre-commit (ruff, eslint, prettier, pip-audit, detect-secrets, …) plus semgrep with the Frappe rules and `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR's commits.
- **Documentation Required**: `feat` PRs need a wiki docs link.
- **Labeler**: adds `needs-tests`. **CodeQL** runs on develop pushes/PRs and weekly.

## Release (inherited from upstream earthians)
- `initiate_release.yml` (weekly, Tuesday) opens `version-N-hotfix → version-N` PRs for 14/15/16 in `earthians/biograph`.
- `on_release.yml`: pushes to `version-14/15/16` run **semantic-release** (angular preset; breaking changes do not trigger a major bump). It rewrites the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes and drops chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded.
- `generate-pot-file.yml` regenerates translations weekly.

## Fork notes
Many workflows hard-code `earthians/biograph` and its secrets, so release automation does not apply to `fossibleworks/biograph` as is. The fork had no `ci.yml` run history, so the first goal-PR run becomes the baseline. The sync push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
