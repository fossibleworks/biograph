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
  - .github/workflows/linters.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .github/helper/install.sh
---

**On pull requests**
- `ci.yml` (**Server Tests**):
  - Compiles all Python and greps for leftover merge-conflict markers.
  - Builds a bench with `.github/helper/install.sh` (MariaDB 11.8, Python 3.14, Node 24).
  - Runs `bench run-parallel-tests --app healthcare`.
  - Skipped when a PR touches only css/js/md/html/csv. Also runs nightly at 00:00 UTC, which uploads coverage to Codecov.
- `linters.yml` and `linters.v2.yml` (both named *Linters*): pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets…) plus semgrep with Frappe rules and `r/python.lang.correctness`. v2 also runs on push.
- `semantic-commits.yml`: commitlint over the PR's commits.
- `docs_checker.yml`: `feat` PRs need a /wiki docs link or `no-docs`.
- `labeller.yml`: auto-labels PRs.
- `codeql.yml`: on PRs and pushes to `develop`, and weekly.

**Release (inherited from upstream earthians)**
- `initiate_release.yml`: every Tuesday, opens `version-N-hotfix → version-N` PRs for 14/15/16 against **earthians/biograph**.
- `on_release.yml`: on push to `version-14/15/16`, runs **semantic-release** (`.releaserc`). The angular preset ignores breaking-change major bumps. It bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml`: regenerates notes on release, excluding `skip-release-notes` labels (`.github/release.yml`).
- `generate-pot-file.yml`: weekly POT regeneration on `develop`.

**Fork caveats**
- Several workflows hard-code `earthians/biograph` and depend on earthians secrets (`EARTHIANS_BOT_TOKEN`, `RELEASE_TOKEN`).
- `install.sh` maps fork branches (`biograph-fh`, `goal/*`) to `version-16` dependencies.
- Per the sync ledger, `ci.yml` has never run on `biograph-fh`.
- Pushing changes to `.github/workflows/*` needs a credential with the `workflow` scope.

There is no deploy pipeline in-repo. Deployment is by `bench get-app` / Frappe Cloud.
