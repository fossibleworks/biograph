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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .github/workflows/codeql.yml
  - codecov.yml
---

**PR checks (GitHub Actions)**
- `ci.yml` (Server Tests):
  - Runs on PRs. It skips PRs that only touch css, js, md, html or csv files.
  - Also runs nightly at 00:00 UTC.
  - Steps: Python 3.14 and Node 24 → `compileall` → grep for merge-conflict markers → `.github/helper/install.sh` (bench with a MariaDB 11.8 service, site `test_site`) → `bench run-parallel-tests --app healthcare`.
  - On non-PR runs it uploads coverage to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets), then semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: `feat` PRs need a wiki link, or `no-docs` in the body.
- `codeql.yml`: Python and JS analysis on `develop` and weekly.
- `labeller.yml`: PR auto-labels.

**Release (inherited from upstream earthians)**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` release PRs for 14, 15 and 16.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16`. Per `.releaserc`, this means:
  - angular preset; breaking changes do not trigger a major release
  - the version is bumped in `healthcare/__init__.py`
  - a `chore(release): Bumped to Version x.y.z` commit is made, along with a GitHub release
- `release_notes.yml` regenerates the release notes.
- `generate-pot-file.yml` refreshes `main.pot` weekly.

**Fork caveats**
- Several workflows hard-code `earthians/biograph` or `develop`, and the release jobs need `EARTHIANS_BOT_TOKEN`. They do not apply to `fossibleworks/biograph` as-is.
- The fork has never had a `ci.yml` run on `biograph-fh`.
- Changes to workflow files need a token with the `workflow` scope. Upstream #86 was deferred for this reason.
- Fork version bumps are manual (`chore: bump version to 16.0.8`).
