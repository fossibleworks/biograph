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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
---

**On pull requests**
- `ci.yml` (Server Tests):
  - Runs on Ubuntu with Python 3.14, Node 24 and MariaDB 11.8.
  - Checks with `compileall` and rejects merge conflict markers.
  - `install.sh` sets up a bench with frappe, payments and erpnext at the matching branch. Fork branches (`biograph-fh`, `goal/*`) fall back to `version-16`.
  - Installs healthcare on `test_site` and runs `run-parallel-tests`.
  - Skips PRs that change only `.js`, `.css`, `.md`, `.html` or `.csv` files. It also runs nightly at 00:00 UTC.
  - Coverage goes to Codecov only on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and Semgrep with Frappe rules plus `python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a docs link or `no-docs`.
- `labeller.yml`: auto-labels PRs.
- `codeql.yml`: Python and JS analysis on develop and weekly.

**Release (inherited from upstream earthians)**
- `initiate_release.yml` opens a weekly (Tuesday) `chore: release v1x` PR for each version, from `version-1x-hotfix` into `version-1x`.
- `on_release.yml` runs semantic-release on pushes to `version-14/15/16`.
  - The angular preset applies, with breaking changes not bumping the major version.
  - It rewrites `__version__` in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates notes and strips chore, ci, test, docs and style lines.
- `generate-pot-file.yml` regenerates translations weekly.

**Fork caveats**
- Several workflows hard-code `earthians/biograph` and `EARTHIANS_BOT_TOKEN`.
- `ci.yml` has no run history on `fossibleworks/biograph` `biograph-fh`, so the first goal-PR run is the baseline.
- The push credential cannot modify `.github/workflows/*`. Workflow changes must be applied by hand (see B2 #86 in the sync ledger).

**Deployment**
- Users install with `bench get-app` and `install-app` (Frappe Cloud signup is linked in the README). There is no deploy pipeline in the repo.
