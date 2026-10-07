---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
  - .github/helper/install.sh
  - .github/dependabot.yml
---

**On pull requests:**
- `linters.v2.yml` (also on push): runs the pre-commit hooks on Python 3.14 and Node 24, plus a Frappe semgrep job. The older `linters.yml` runs the same checks.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: requires a docs link for `feat` PRs.
- `labeller.yml`: applies PR labels.
- CodeQL runs on `develop` and weekly.
- Codecov gates patch coverage at 85%.
- Server tests need a bench built by `.github/helper/install.sh`. The `ci.yml` test workflow from upstream is **not present** on the fork yet: the push credential cannot write workflow files, so the fork has no CI test history.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` release PRs for 14, 15 and 16, on Tuesdays at 09:30 UTC.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. It uses the Angular preset, and breaking changes do not trigger a major release. It bumps the version string in `healthcare/__init__.py` and commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes and drops chore, ci, test, docs and style entries.

**Housekeeping:**
- `generate-pot-file.yml` refreshes `main.pot` weekly.
- Crowdin opens `fix: sync translations from crowdin` PRs.
- Dependabot is configured.

**Deploy:** install or update with bench on a Frappe site (self-hosted or Frappe Cloud). `after_migrate` and `patches.txt` run on `bench migrate`.
