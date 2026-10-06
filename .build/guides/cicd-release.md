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
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/codeql.yml
  - .github/dependabot.yml
---

**On pull requests**
- `ci.yml` (Server Tests). Skipped for PRs that only change css/js/md/html/csv. It sets up Ubuntu, Python 3.14, Node 24 and MariaDB 11.8, then runs `.github/helper/install.sh`. That script runs bench init, then frappe, payments and erpnext on the base branch, falling back to `version-16` for fork branches such as `biograph-fh` and `goal/*`. It installs healthcare on `test_site` and runs `bench run-parallel-tests --app healthcare`. Timeout is 30 minutes. It also runs nightly at 00:00 UTC with coverage uploaded to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, file checks) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint across the PR's commits.
- `docs_checker.yml`: `feat` PRs need a wiki docs link, `no-docs` or `backport`.
- `labeller.yml`: adds the `needs-tests` label.
- `codeql.yml`: Python and JS analysis on develop and weekly.

**Release (inherited from upstream earthians)**
- `initiate_release.yml`: every Tuesday, opens `version-N-hotfix` → `version-N` release PRs for 14, 15 and 16 on `earthians/biograph`.
- `on_release.yml`: when `version-14/15/16` is pushed, runs **semantic-release** (`.releaserc`, angular preset; breaking changes don't trigger majors). It bumps `healthcare/__init__.py` `__version__`, commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml`: regenerates and strips release notes.
- `generate-pot-file.yml`: weekly POT regeneration. Crowdin sync PRs are titled `fix: sync translations from crowdin`.
- Dependabot keeps GitHub Actions up to date weekly.

**Fork notes:** the fork integrates on `biograph-fh`, which had no CI history before the upstream sync. Several workflows hard-code `earthians/biograph` and earthians bot secrets, so release automation is not wired for `fossibleworks/biograph`. Editing workflow files needs a token with the `workflow` scope; the sync ledger records deferrals for this reason. Deployment is by `bench get-app` / `install-app` or Frappe Cloud. There is no deploy pipeline in the repo.
