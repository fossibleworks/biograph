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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
  - .github/workflows/codeql.yml
---

**On pull requests:**
- `ci.yml`, Server Tests:
  - Skips PRs that only change css/js/md/html/csv.
  - Sets up Ubuntu, Python 3.14, Node 24, and MariaDB 11.8.
  - Runs `python -m compileall` and a merge-conflict-marker grep.
  - `.github/helper/install.sh` builds a bench with frappe, payments, and erpnext. Fork branches such as `biograph-fh` and `goal/*` fall back to `version-16`.
  - Then `bench run-parallel-tests --app healthcare`, with a 30-minute timeout.
  - Also runs nightly; on scheduled runs it uploads coverage to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, eslint, prettier, pip-audit, detect-secrets), then semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: requires a wiki link on `feat` PRs.
- `labeller.yml`: applies `needs-tests`.
- `codeql.yml`: Python and JavaScript, on develop and weekly.

**Release:**
- `initiate_release.yml` opens a weekly (Tuesday) PR from `version-NN-hotfix` to `version-NN` for 14, 15, and 16 on `earthians/biograph`.
- `on_release.yml` runs `npx semantic-release` on pushes to `version-14/15/16`. It follows `.releaserc`:
  - Angular preset; breaking changes don't trigger a major release.
  - Bumps the version in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
  - Creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded.
- `generate-pot-file.yml` regenerates translations weekly. Crowdin opens `fix: sync translations from crowdin` PRs.
- Dependabot is configured in `.github/dependabot.yml`.

Several of the release workflows hard-code the upstream `earthians` org and its bot tokens, so they may not run on the fork.
