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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .github/workflows/docs_checker.yml
  - .releaserc
---

**On pull requests:**
- `ci.yml` (Server Tests). Skipped for css/js/md/html/csv-only changes. It:
  - spins up MariaDB 11.8, Python 3.14 and Node 24;
  - runs `compileall` and a merge-conflict-marker check;
  - installs a bench via `.github/helper/install.sh`;
  - runs `bench run-parallel-tests --app healthcare`.
  It also runs nightly at 00:00 UTC, and coverage goes to Codecov on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets) plus Semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint on the PR.
- `docs_checker.yml`: `feat` PRs need a docs link or `no-docs`.
- `labeller.yml`: auto-labels via `.github/labeler.yml`.
- `codeql.yml`: python and javascript, on the develop branch and weekly.

**Release:**
- `initiate_release.yml` opens weekly (Tuesday) `version-N-hotfix → version-N` release PRs for N = 14/15/16.
- Pushing to `version-14/15/16` triggers `on_release.yml` → `npx semantic-release` (`.releaserc`, Angular preset; breaking changes don't auto-major). This bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml` regenerates notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations weekly.
- Dependabot is configured in `.github/dependabot.yml`.

**Fork caveats:**
- Several workflows still target `earthians/biograph` and `develop`.
- The fork's `biograph-fh` branch has no CI run history, per the sync ledger.
- The push credential cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
