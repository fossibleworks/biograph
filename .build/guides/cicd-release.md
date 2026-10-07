---
title: CI/CD & release
category: cicd-release
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - .github/workflows/linters.v2.yml
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - .mergify.yml
  - codecov.yml
---

**PR checks (GitHub Actions)**
- `linters.v2.yml` (runs on PR, push and dispatch):
  - **precommit-linters** job: Python 3.14 and Node 24. Installs the ESLint dependencies and runs `pre-commit/action` (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks).
  - **semgrep** job: Frappe semgrep rules plus `r/python.lang.correctness`.
- `linters.yml`: the older PR-only version of the same pre-commit and semgrep checks.
- `semantic-commits.yml`: commitlint on every commit in the PR range.
- `docs_checker.yml`: requires a wiki docs link on `feat` PRs.
- `codeql.yml`: CodeQL security scanning. `labeller.yml`: auto-labels PRs using `.github/labeler.yml`.
- Codecov: 85% patch target (`codecov.yml`). **There is no unit-test (`ci.yml`) workflow in this fork**, so run tests locally on a bench.
- Mergify: auto-closes non-maintainer PRs to stable branches. It also auto-merges on CI success plus review unless the PR is labelled `dont-merge`.
- Dependabot (`.github/dependabot.yml`).

**Release (inherited from upstream earthians)**
- `initiate_release.yml`: every Tuesday 09:30 UTC it opens `chore: release v1x` PRs from `version-1x-hotfix` into `version-1x` (for 14, 15 and 16).
- `on_release.yml`: on push to `version-14/15/16` it runs **semantic-release** (`.releaserc`, angular preset; breaking changes do not trigger a major release). That bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` and `.github/release.yml` cover release notes.
- `generate-pot-file.yml`: every Sunday it regenerates `healthcare/locale/main.pot` on `develop`. Crowdin opens `fix: <lang> translations` PRs.

**Deploy:** installed into Frappe benches or Frappe Cloud through `bench get-app` and `install-app`, then `bench migrate` (runs `patches.txt` and `after_migrate`). The repo has no deploy pipeline of its own.

Note: several release workflows target `earthians/biograph` and need `EARTHIANS_BOT_TOKEN`, so they do not apply to the `biograph-fh` fork as written. Pushes that change `.github/workflows/*` need a credential with workflow scope.
