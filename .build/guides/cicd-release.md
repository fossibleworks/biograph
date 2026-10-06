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
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
---

**On every PR**
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, detect-secrets, pip-audit, file checks) plus Frappe semgrep rules and `r/python.lang.correctness`. v2 also runs on push.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `ci.yml` (Server Tests): checks that the Python compiles and that there are no merge-conflict markers. It then sets up a bench through `.github/helper/install.sh`: frappe, payments and erpnext on the base branch, or on `version-16` for fork branches such as `biograph-fh` and `goal/*`. Finally it runs `bench run-parallel-tests --app healthcare` against MariaDB 11.8. PRs that only touch js/css/md/html/csv are skipped. A nightly cron collects coverage and uploads it to Codecov.
- `docs_checker.yml`: `feat` PRs need a wiki docs link.
- `codeql.yml`, `labeller.yml`.

**Release (upstream earthians flow)**
- `initiate_release.yml`: every Tuesday it opens release PRs from `version-N-hotfix` into `version-N` (14/15/16).
- `on_release.yml`: a push to `version-14/15/16` runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major release). It bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates the GitHub release.
- `release_notes.yml`: regenerates the release notes without chore/ci/test/docs/style entries.
- `generate-pot-file.yml`: weekly POT refresh on `develop`. Crowdin opens `fix: sync translations from crowdin` PRs.

Several release workflows hardcode `earthians/biograph` and bot secrets, so they do not run meaningfully on this fork. The fork has no CI history on `biograph-fh`. Pushes that modify `.github/workflows/*` need a token with `workflow` scope.
