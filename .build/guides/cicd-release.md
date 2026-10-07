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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .mergify.yml
---

**On pull requests:**
- `ci.yml` (Server Tests) runs on PRs, skipping changes that touch only css/js/md/html/csv, and nightly at 00:00 UTC. It uses Ubuntu, MariaDB 11.8, Python 3.14 and Node 24. It runs `python -m compileall`, fails on merge-conflict markers, installs a bench through `.github/helper/install.sh`, and runs `bench run-parallel-tests --app healthcare` with a 30-minute timeout. Coverage is uploaded to Codecov only on non-PR runs.
- `linters.yml` / `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, file checks) and semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint over the PR's commits.
- `docs_checker.yml` requires a wiki docs link on `feat` PRs.
- `labeller.yml` applies labels such as `needs-tests`.
- `codeql.yml` runs CodeQL for Python and JS on `develop` and weekly.

**Merge:** Mergify merges after one approval (merge commit, or squash with the `squash` label).

**Release** (upstream-style, on stable branches):
- `initiate_release.yml` opens weekly `version-1x-hotfix` → `version-1x` release PRs for 14, 15 and 16 (Tuesdays).
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. `.releaserc` uses the angular preset with breaking changes set to *not* trigger a major. It bumps the version in `healthcare/__init__.py` with the commit `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes, stripping chore/ci/test/docs/style entries.
- `generate-pot-file.yml` regenerates translations weekly. Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork caveats:** many workflows still point at `earthians/biograph` and its secrets. The ledger notes that `ci.yml` had never run on `fossibleworks/biograph` `biograph-fh`, so the first goal-PR run is the baseline. Changes to workflow files need a credential with `workflow` scope.
