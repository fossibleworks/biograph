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
  - .github/workflows/linters.v2.yml
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/docs_checker.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/workflows/codeql.yml
  - .github/workflows/generate-pot-file.yml
  - codecov.yml
---

**On every pull request**
- `ci.yml` (**Server Tests**): runs on PRs, but not when only `css/js/md/html/csv` files change and not on `version-*-beta` branches. It also runs nightly at 00:00 UTC. Python 3.14 + Node 24 + MariaDB 11.8. Steps: `compileall` and a merge-conflict-marker check, bench install via `.github/helper/install.sh`, then `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov on non-PR runs (patch target 85%).
- `linters.yml` / `linters.v2.yml` (**linters**, also on push): run pre-commit (ruff, ruff-format, eslint, prettier, pip-audit, detect-secrets, file checks) and Frappe **semgrep** rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a wiki docs link unless the body says `no-docs` or `backport`.
- `codeql.yml`: CodeQL security scanning. `labeller.yml` applies automatic labels.

**Release (inherited from upstream earthians)**
- `initiate_release.yml`: every Tuesday at 09:30 UTC, opens `version-1x-hotfix → version-1x` release PRs for 14, 15 and 16.
- `on_release.yml`: on push to `version-14/15/16`, runs **semantic-release** (`.releaserc`, angular preset, breaking changes do not trigger a major bump). It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and publishes a GitHub release. `release_notes.yml` handles release notes.
- `generate-pot-file.yml`: weekly on Sunday, regenerates translation strings.
- **Deployment** is by installing the app on Frappe benches or Frappe Cloud (`bench get-app` / `install-app`, then `bench migrate` runs `patches.txt` and `after_migrate`).

**Fork caveats:** several workflows still reference `earthians/biograph` and its bot secrets. The fork's `ci.yml` has no run history on `biograph-fh`. The push credential used by automation cannot modify `.github/workflows/*`, so workflow changes must be applied by hand.
