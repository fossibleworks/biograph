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
  - .github/release.yml
  - codecov.yml
---

**On every pull request**
- `ci.yml` (Server Tests): Python 3.14, Node 24 and MariaDB 11.8. It runs `compileall` and a merge-marker check, bootstraps a bench with `.github/helper/install.sh`, then runs `bench run-parallel-tests --app healthcare`. It skips PRs that only touch css/js/md/html/csv files and `version-*-beta` branches, and also runs nightly at 00:00 UTC. Coverage is uploaded to Codecov only on non-PR runs.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks) and Semgrep with the Frappe rules plus `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR commit range.
- `docs_checker.yml`: `feat` PRs need a docs link or `no-docs`.
- `codeql.yml` and `labeller.yml` (path labels from `.github/labeler.yml`). `dependabot.yml` handles dependency updates.

**Release (inherited from upstream earthians)**
- `initiate_release.yml` opens weekly (Tuesday) PRs from `version-N-hotfix` to `version-N` for N = 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`, using the angular preset. Breaking changes don't trigger a major release. It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release. Release notes come from `release_notes.yml` and `.github/release.yml`, which exclude the `skip-release-notes` label.
- Translations: `generate-pot-file.yml` regenerates `main.pot` weekly, and Crowdin opens `fix: sync translations from crowdin` PRs.
- Deployment is via `bench get-app` / `install-app` and Frappe Cloud. There is no in-repo deploy script.

**Fork caveats:** several workflows hardcode `earthians/biograph` and `EARTHIANS_BOT_TOKEN`. `ci.yml` has never run on `biograph-fh`. Credentials used for automation can't push changes under `.github/workflows/`, so workflow edits must be applied by hand.
