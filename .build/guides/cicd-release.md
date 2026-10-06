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
  - .github/workflows/docs_checker.yml
  - .github/workflows/codeql.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

**PR checks** (GitHub Actions)
- **`ci.yml` – Server Tests:** runs on PRs except when only `.css/.js/.md/.html/.csv` files change, and nightly at 00:00 UTC. It uses Ubuntu, Python 3.14, Node 24 and a MariaDB 11.8 service. It first runs `compileall` and a merge-conflict-marker grep, then `.github/helper/install.sh` (bench, frappe, payments, erpnext and healthcare; fork branches use `version-16`), then `bench run-parallel-tests --app healthcare`. It has a 30-minute timeout and cancels superseded runs. Coverage is uploaded to Codecov only on non-PR runs.
- **`linters.yml` / `linters.v2.yml`:** run pre-commit (ruff, ruff-format, eslint, prettier, detect-secrets, pip-audit, yaml/json/toml/ast checks) and Frappe semgrep rules plus `r/python.lang.correctness`.
- **`semantic-commits.yml`:** runs commitlint on the PR's commit range.
- **`docs_checker.yml`:** requires a docs link on `feat` PRs.
- **`codeql.yml`:** CodeQL security analysis. **`labeller.yml`** with `.github/labeler.yml` handles auto-labelling.
- Dependabot is configured in `.github/dependabot.yml`.

**Merging:** Mergify merges after at least one approval and passing checks, with optional squash and backport labels.

**Release (inherited from upstream):**
- `initiate_release.yml` opens weekly (Tuesday 09:30 UTC) `chore: release vXX` PRs from `version-XX-hotfix` to `version-XX`, for versions 14, 15 and 16.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. It uses Angular commit analysis, and breaking changes do not trigger a major release. It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release. `release_notes.yml` and `.github/release.yml` shape the notes.
- `generate-pot-file.yml` regenerates `main.pot` weekly. Crowdin opens translation PRs.

**Fork notes:** these workflows still reference `earthians` owners and secrets (`EARTHIANS_BOT_TOKEN`). The fork has no CI run history on `biograph-fh` yet. Workflow-file changes need a token with the `workflow` scope, so they are sometimes deferred and applied by hand. Fork version bumps are done as explicit `chore: bump version to 16.0.x` commits.
