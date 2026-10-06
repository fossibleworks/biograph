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
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - codecov.yml
  - .mergify.yml
---

**On pull requests (GitHub Actions):**
- `ci.yml` **Server Tests**: Ubuntu, MariaDB 11.8, Python 3.14, Node 24. Runs `compileall`, a merge-conflict-marker grep, a bench install (`.github/helper/install.sh`), then `bench run-parallel-tests --app healthcare`. Skipped for PRs that touch only css/js/md/html/csv. Also runs nightly at 00:00 UTC, when coverage is uploaded to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit) and Frappe semgrep rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a docs link.
- `codeql.yml`: Python and JS analysis on `develop` and weekly.
- `labeller.yml`: auto-labels PRs.
- Mergify: auto-merge after one approval once CI passes. Backport labels.

**Release (inherited upstream earthians flow):**
- `initiate_release.yml`: every Tuesday, opens `version-XX-hotfix → version-XX` release PRs for 14, 15 and 16.
- `on_release.yml`: a push to `version-14/15/16` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do *not* trigger a major bump). It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml`: regenerates release notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml`: weekly POT regeneration on `develop`.
- Deployment happens downstream in Frappe Cloud or bench (`bench get-app` / `migrate`). There is no deploy job in this repo.

**Fork caveats:** several workflows hard-code `earthians/biograph` (release, docs checker, release notes). On `fossibleworks/biograph`, `ci.yml` has never run on `biograph-fh`. Pushing workflow-file changes needs a credential with `workflow` scope.
