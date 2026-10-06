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
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - codecov.yml
---

**PR checks** (GitHub Actions)
- **`ci.yml` – Server Tests:**
  - Runs on pull requests (except `version-*-beta`) and nightly at 00:00 UTC.
  - Skipped when a PR only touches `.css/.js/.md/.html/.csv`.
  - Uses Ubuntu, Python 3.14, Node 24, and a MariaDB 11.8 service.
  - `compileall` and a merge-conflict-marker check run first.
  - `.github/helper/install.sh` builds a bench with frappe, payments, and erpnext. Fork branches such as `biograph-fh` and `goal/*` fall back to `version-16` of those apps.
  - Runs `bench --site test_site run-parallel-tests --app healthcare` with a 30-minute timeout.
  - On non-PR runs, coverage goes to Codecov (patch target 85%).
- **`linters.yml` / `linters.v2.yml`:** pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets) and Semgrep with `frappe/semgrep-rules` + `r/python.lang.correctness`.
- **`semantic-commits.yml`:** commitlint over the PR commit range.
- **`docs_checker.yml`:** `feat` PRs must link to wiki docs. The check calls the earthians API.
- **`codeql.yml`:** Python and JS analysis on `develop` and weekly.
- **`labeller.yml`:** path-based labels.

**Release** (inherited from upstream earthians and wired to the `earthians/biograph` repo and secrets)
- `initiate_release.yml` opens weekly `version-N-hotfix` → `version-N` PRs for versions 14, 15, and 16.
- `on_release.yml` runs `semantic-release` on pushes to `version-14/15/16` (`.releaserc`). It uses the angular preset, rewrites `healthcare/__init__.py` `__version__`, commits `chore(release): Bumped to Version X`, and creates a GitHub release. Breaking changes do not trigger a major bump.
- `release_notes.yml` regenerates the notes and strips chore, ci, test, docs, and style entries. `.github/release.yml` excludes the `skip-release-notes` label.
- `generate-pot-file.yml` regenerates the translations weekly.

**Fork reality:** `biograph-fh` has no CI history; the sync ledger reports zero runs. The fork bumps its version by hand (`chore: bump version to 16.0.8`). Changes to workflow files need a token with the `workflow` scope, so the sync ledger defers them.
