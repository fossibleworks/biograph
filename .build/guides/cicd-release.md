---
title: CI/CD and release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/workflows/linters.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - codecov.yml
  - .mergify.yml
  - .github/dependabot.yml
---

**PR checks** (GitHub Actions)
- `ci.yml` runs **Server Tests**.
  - Triggers: PRs, except those that change only css/js/md/html/csv files or target `version-**-beta`, plus a nightly cron.
  - Steps: Python 3.14 and Node 24, `compileall`, a merge-conflict marker grep, `.github/helper/install.sh` (bench, payments, erpnext, healthcare on `test_site` with MariaDB 11.8), then `bench run-parallel-tests --app healthcare`. Timeout is 30 minutes.
  - Coverage is uploaded to Codecov only on non-PR runs. Codecov sets an 85% patch target.
- `linters.yml` and `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, …) and Frappe semgrep rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR's commits.
- `docs_checker.yml` requires a wiki docs link on `feat` PRs (or `no-docs` in the body).
- `codeql.yml` runs security analysis. `labeller.yml` (with `labeler.yml`) applies labels automatically.
- Dependabot updates GitHub Actions weekly.

**Merge:** Mergify merges after at least 1 approval once CI passes. The default method is a merge commit; the `squash` label squashes and `dont-merge` blocks.

**Release** (inherited from upstream earthians)
- `initiate_release.yml` opens `chore: release vNN` PRs every Tuesday, from `version-NN-hotfix` into `version-NN` for 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. It uses the angular preset, and breaking changes do not trigger a major bump.
  - It rewrites the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
  - It publishes a GitHub release. `release_notes.yml` and `.github/release.yml` produce the notes.
- Weekly POT regeneration (`generate-pot-file.yml`) and Crowdin keep translations in sync.

**Fork caveats**
- Several workflows hard-code `earthians/biograph` and the `EARTHIANS_BOT_TOKEN` secret.
- The sync ledger records that `ci.yml` had never run on `fossibleworks/biograph` before the goal PRs, so there is no earlier CI history to compare against.
- The push credential cannot write workflow files, which is why B2 #86 was skipped. Changes under `.github/workflows/` need a human with the `workflow` scope.
- The fork bumps versions by hand (`chore: bump version to 16.0.8`).
