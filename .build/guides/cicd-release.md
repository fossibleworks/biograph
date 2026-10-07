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
  - .github/workflows/codeql.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
---

**On pull requests**
- **CI / Server Tests** (`ci.yml`) runs on Ubuntu with a MariaDB 11.8 service, Python 3.14 and Node 24. Steps:
  1. `compileall` plus a merge-conflict-marker grep.
  2. `.github/helper/install.sh` builds a bench and installs frappe, payments, erpnext and healthcare. Fork branches such as `biograph-fh` and `goal/*` fall back to `version-16` of the dependencies.
  3. `bench run-parallel-tests --app healthcare`.
  It skips PRs that change only css/js/md/html/csv and branches matching `version-*-beta`. It also runs nightly at 00:00 UTC, uploading coverage to Codecov on non-PR runs. Concurrency cancels superseded runs.
- **Linters**: `linters.yml` runs on PRs; `linters.v2.yml` runs on PRs, pushes and manual dispatch. They run pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, file checks) and **semgrep** with `frappe/semgrep-rules` plus `r/python.lang.correctness`.
- **Semantic Commits**: commitlint over the PR's commit range.
- **Documentation Required** (`docs_checker.yml`): `feat` PRs need a wiki link or `no-docs`.
- **CodeQL**: Python and JavaScript, on `develop` pushes and PRs, plus weekly.
- **Labeler**: adds `needs-tests` and other path-based labels.
- **Dependabot** config lives in `.github/dependabot.yml`.

**Release** (inherited from upstream earthians; it uses org tokens and repo names, so it may not run as-is in the fork)
- `initiate_release.yml` (weekly, Tuesday) opens `version-N-hotfix` → `version-N` PRs for 14, 15 and 16.
- `on_release.yml` runs on pushes to `version-14/15/16` and executes **semantic-release** (`.releaserc`). It uses the angular preset; breaking changes do not trigger a major bump. The version string in `healthcare/__init__.py` is rewritten and committed as `chore(release): Bumped to Version x.y.z`, then a GitHub release is created.
- `release_notes.yml` regenerates release notes and strips `chore|ci|test|docs|style` entries. The `skip-release-notes` label excludes a PR (`.github/release.yml`).
- `generate-pot-file.yml` (weekly) refreshes translations, and Crowdin opens translation PRs.

**Deployment:** there is no deploy pipeline in this repo. Sites install the app through bench (`bench get-app` / `install-app` / `migrate`) or Frappe Cloud. Migrations ship as patches registered in `healthcare/patches.txt`.

**Fork caveat:** the wiki notes that `biograph-fh` has no CI run history, and the bot token cannot push workflow-file changes. Edits under `.github/workflows/` may need to be applied by hand.
