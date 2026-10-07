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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/codeql.yml
  - .github/release.yml
  - .mergify.yml
---

**PR checks (GitHub Actions)**
- `ci.yml` (**Server Tests**): runs on PRs, ignoring changes limited to `*.css/js/md/html/csv` and `version-*-beta` branches, and nightly at 00:00 UTC. Steps: `compileall` and a merge-conflict-marker check, then `.github/helper/install.sh` (bench, Frappe, payments, ERPNext and healthcare on MariaDB 11.8, with fork branches such as `biograph-fh`/`goal/*` falling back to the `version-16` dependencies), then `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov only on non-PR runs.
- `linters.v2.yml` (PR, push, dispatch): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, ...) and Semgrep with `frappe/semgrep-rules` + `r/python.lang.correctness`. `linters.yml` is the older equivalent and runs on PRs.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: `feat` PRs need a wiki docs link.
- `codeql.yml`: CodeQL on `develop` pushes and PRs, and weekly.
- `labeller.yml` / `.github/labeler.yml`: auto-labels PRs.

**Release**
- `initiate_release.yml`: every Tuesday at 09:30 UTC, opens `chore: release v<N>` PRs from `version-<N>-hotfix` → `version-<N>` for 14, 15 and 16 (on `earthians/biograph`).
- `on_release.yml`: a push to `version-14/15/16` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger major releases). It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` + `.github/release.yml`: release notes exclude PRs labelled `skip-release-notes`.
- `generate-pot-file.yml`: weekly POT regeneration on `develop`.
- Mergify merges PRs after ≥1 approval and passing CI.
- Dependabot is configured in `.github/dependabot.yml`.

**Fork caveats:** several workflows hard-code `earthians` (owner, bot token secrets, the docs checker API URL). `biograph-fh` has no CI run history. The current push credential cannot modify `.github/workflows/*` (see B2 #86 in the sync ledger), so workflow changes have to be applied by hand.
