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
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
---

**PR checks (GitHub Actions):**
- `ci.yml` (Server Tests):
  - Triggers on PRs (skipping css/js/md/html/csv-only changes) and nightly at 00:00 UTC.
  - Steps: Python 3.14, Node 24, MariaDB 11.8 → `compileall` and a merge-conflict grep → `.github/helper/install.sh` (bench setup) → `bench run-parallel-tests --app healthcare`.
  - Coverage goes to Codecov on non-PR runs only.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) plus Frappe semgrep rules.
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: `feat` PRs must link docs.
- `codeql.yml`: Python and JS analysis on `develop` and weekly.
- `labeller.yml`: auto-labels PRs.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly `version-N-hotfix` → `version-N` PRs (v14/15/16).
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16`. Per `.releaserc`, it uses the angular preset (breaking changes do not trigger major releases), bumps `healthcare/__init__.py`, and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` strips chore/ci/test/docs/style lines from GitHub release notes.
- `generate-pot-file.yml` regenerates translations weekly.

**Fork caveats:**
- Several workflows hardcode `earthians/biograph` and bot secrets (`EARTHIANS_BOT_TOKEN`).
- The fork's `biograph-fh` branch has no CI run history.
- Pushing changes to `.github/workflows/` requires a credential with `workflow` scope, which blocked one upstream pick (B2 #86).

**Deploy:** via Frappe bench / Frappe Cloud (`bench get-app`, `install-app`, migrate runs `patches.txt` and `after_migrate`).
