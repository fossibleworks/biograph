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
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/release_notes.yml
  - .github/workflows/codeql.yml
  - README.md
---

**On pull requests (GitHub Actions):**
- `ci.yml` (Server Tests) runs on PRs that touch more than css/js/md/html/csv, and nightly at 00:00 UTC. It runs on Python 3.14, Node 24 and MariaDB 11.8. Steps: compile all Python, fail on merge-conflict markers, set up a bench with `.github/helper/install.sh`, then `bench run-parallel-tests --app healthcare`. Coverage goes to Codecov only on non-PR runs.
- `linters.yml` and `linters.v2.yml` run pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast/merge-conflict checks) plus semgrep with the Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml` runs commitlint on the PR commit range.
- `docs_checker.yml` requires a docs link (or `no-docs`) on `feat` PRs.
- `codeql.yml` (security scan) and `labeller.yml` (path labels via `labeler.yml`). Dependabot is configured in `.github/dependabot.yml`.

**Release (inherited from upstream earthians and wired to the `version-14/15/16` branches):**
- `initiate_release.yml` opens weekly `chore: release vNN` PRs every Tuesday, merging `version-NN-hotfix` into `version-NN`.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset. Breaking changes do not trigger a major bump. It bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates release notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations, and Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork caveats:** several workflows hardcode `earthians/biograph` and earthians bot secrets. The `biograph-fh` fork has no `ci.yml` run history. The push credential cannot modify `.github/workflows/*` (workflow scope), so workflow-file changes must be applied by hand.

**Deployment:** the app is installed into a Frappe bench (`bench get-app`, `bench --site <site> install-app healthcare`, then `bench migrate` to run `patches.txt`). It is also offered on Frappe Cloud.
