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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
  - .github/dependabot.yml
---

**PR checks** (`.github/workflows`):
- `linters.yml` / `linters.v2.yml`: pre-commit on Python 3.14 and Node 24 (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks), plus Semgrep with Frappe rules and `r/python.lang.correctness`. v2 also runs on push and workflow_dispatch.
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: `feat` PRs need a docs link unless the body says `no-docs` or `backport`.
- `codeql.yml`: CodeQL security scanning.
- `labeller.yml` + `.github/labeler.yml`: automatic labels, e.g. `needs-tests`.
- Codecov is configured (patch 85%), but no server-test workflow exists in this fork, so there is no CI test baseline yet.
- Dependabot is configured in `.github/dependabot.yml`.

**Release:**
- `initiate_release.yml` runs weekly (Tue 09:30 UTC) and opens `chore: release v1x` PRs from `version-1x-hotfix` into `version-1x` for 14, 15 and 16. It targets `earthians/biograph`.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. Using `.releaserc` (angular preset; breaking changes do not trigger a major release), it bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and publishes a GitHub release.
- `release_notes.yml` and `.github/release.yml` build the changelog and leave out PRs labelled `skip-release-notes`.
- `generate-pot-file.yml` regenerates translations weekly on `develop`. Crowdin opens translation PRs.
- Deployment is by installing the app on a Frappe bench or Frappe Cloud (`bench get-app` / `install-app`, then `bench migrate` to apply `patches.txt`).

Several workflows still point at the `earthians/` org and use the `EARTHIANS_BOT_TOKEN` secret, which are upstream leftovers. Confirm the target before relying on them in the fossibleworks fork. Pushing workflow-file changes needs a credential with `workflow` scope (see sync-ledger item B2 #86).
