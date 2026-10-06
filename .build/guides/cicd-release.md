---
title: CI/CD and release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
---

**On pull requests**
- `ci.yml` (**Server Tests**): Python 3.14, Node 24, MariaDB 11.8. It runs `compileall` and checks for merge-conflict markers, sets up the bench with `.github/helper/install.sh`, then runs `bench run-parallel-tests --app healthcare`. It skips PRs touching only `js/css/md/html/csv` and `version-*-beta` branches. It also runs nightly at 00:00 UTC, with coverage captured and uploaded to Codecov on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit hooks (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, file checks) plus Semgrep with `frappe/semgrep-rules` and `r/python.lang.correctness`. The v2 workflow also runs on push.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: `feat` PRs need a wiki docs link.
- `codeql.yml`: CodeQL for python and javascript on `develop` and weekly.
- `labeller.yml`: auto-labels PRs (`.github/labeler.yml`).
- `codecov.yml`: patch target 85%, project threshold 0.5%.

**Release (upstream-style)**
- `initiate_release.yml`: every Tuesday it opens `chore: release vN` PRs from `version-N-hotfix` to `version-N` (N = 14, 15, 16). These target `earthians/biograph`.
- `on_release.yml`: on push to `version-14/15/16` it runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major release). This bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates release notes and strips `chore/ci/test/docs/style` entries.
- `generate-pot-file.yml`: weekly POT regeneration. Crowdin then opens translation PRs.
- Dependabot is configured in `.github/dependabot.yml`.

**Deploy:** there is no deploy workflow in the repo. Sites install the app via `bench get-app` / `install-app` or Frappe Cloud, and run `bench migrate`, which executes `patches.txt`.

Several release workflows hard-code `earthians` as owner/repo and use the `EARTHIANS_BOT_TOKEN` secret, so they are upstream artefacts and likely inert on this fork.
