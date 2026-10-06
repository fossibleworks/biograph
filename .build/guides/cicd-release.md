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
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/helper/install.sh
  - codecov.yml
---

**PR checks (GitHub Actions):**
- `ci.yml`, **Server Tests**:
  - Runs on PRs, skipping changes that only touch css/js/md/html/csv, and nightly at 00:00 UTC.
  - Steps: `compileall` and a merge-conflict-marker grep, then `.github/helper/install.sh` (bench, Frappe, payments, ERPNext and healthcare on MariaDB 11.8, with fork branches mapped to `version-16`), then `bench run-parallel-tests --app healthcare`.
  - Coverage is uploaded to Codecov only on non-PR runs.
- `linters.v2.yml` runs pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets) and Semgrep with the Frappe rules plus `python.lang.correctness`. `linters.yml` is an older duplicate that runs on PRs.
- `semantic-commits.yml` runs commitlint over the PR commit range.
- `docs_checker.yml` requires a wiki docs link for `feat` PRs.
- `codeql.yml` runs CodeQL security analysis.
- `labeller.yml` adds the `needs-tests` label.
- Dependabot is configured in `.github/dependabot.yml`.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` runs weekly (Tuesday 09:30 UTC). It opens `version-N-hotfix → version-N` release PRs for 14, 15 and 16 on `earthians/biograph`.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. Per `.releaserc`, the Angular preset turns breaking changes into no release. The version string in `healthcare/__init__.py` is bumped and committed as `chore(release): Bumped to Version X`, and a GitHub release is created.
- `release_notes.yml` regenerates release notes and strips `chore/ci/test/docs/style` entries.
- `generate-pot-file.yml` regenerates translations weekly on `develop`.

**Fork caveats:**
- Release and docs workflows point at `earthians/*` and need the `EARTHIANS_BOT_TOKEN` / `RELEASE_TOKEN` secrets.
- The fork (`fossibleworks/biograph`, default branch `biograph-fh`) has no `ci.yml` run history (see the wiki ledger).
- Pushes made with the agent credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
- Deployment goes through Frappe Cloud or bench (`bench get-app` + `install-app`, then `migrate`). There is no deploy workflow in the repo.
