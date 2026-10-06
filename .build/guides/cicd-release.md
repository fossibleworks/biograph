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
  - .github/workflows/linters.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
---

**Pull request checks** (GitHub Actions)
- `ci.yml` **Server Tests**: runs on PRs (skipped when only css/js/md/html/csv changed, and on `version-*-beta` branches) and nightly at 00:00 UTC. The job:
  1. Sets up Python 3.14 and Node 24 with a MariaDB 11.8 service.
  2. Runs `compileall` and the merge-conflict marker grep.
  3. Runs `.github/helper/install.sh` (bench, payments, erpnext; fork branches resolve to `version-16`).
  4. Runs `bench run-parallel-tests`.
  5. On non-PR runs, uploads coverage to Codecov (`fail_ci_if_error`).
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets), plus Frappe semgrep rules and `r/python.lang.correctness`. v2 also runs on push.
- `semantic-commits.yml`: commitlint across the PR's commits.
- `docs_checker.yml`: requires a docs link on `feat` PRs.
- `codeql.yml`: CodeQL security scan. `labeller.yml` with `labeler.yml`: path labels. `dependabot.yml`.

**Release** (inherited from upstream earthians and wired to the earthians bot and repo)
- `initiate_release.yml`: every Tuesday at 09:30 UTC it opens `chore: release v1x` PRs from `version-1x-hotfix` into `version-1x` (14, 15, 16).
- `on_release.yml`: on push to `version-14/15/16`, `npx semantic-release` (`.releaserc`, angular preset, breaking changes do not trigger a major release) bumps `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` and `.github/release.yml`: release-notes generation.
- `generate-pot-file.yml`: regenerates `main.pot` weekly on `develop`. Crowdin opens translation PRs.

**Fork caveats:** the fork's `biograph-fh` had no CI run history before the upstream sync. Workflow-file edits need the `workflow` token scope (one upstream CI change was deferred for that reason). Deployment is through Frappe Cloud / bench (`bench get-app`, `install-app`, `migrate`). There is no deploy job in the repo.
