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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .mergify.yml
  - .releaserc
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - codecov.yml
---

**PR checks (GitHub Actions):**
- `ci.yml` (Server Tests). Runs on PRs that are not CSS/JS/MD/HTML-only, and nightly at 00:00 UTC. It sets up Python 3.14, Node 24 and MariaDB 11.8. It runs `compileall` and a merge-conflict-marker scan, then `.github/helper/install.sh`, which bench-inits frappe, erpnext, payments and healthcare. Fork branches such as `biograph-fh` and `goal/*` are built against `version-16`. Finally it runs `bench run-parallel-tests --app healthcare`. Coverage is uploaded to Codecov on non-PR runs only.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, pip-audit, detect-secrets) and Frappe semgrep rules.
- `semantic-commits.yml`: commitlint across the PR's commits.
- `docs_checker.yml`: `feat` PRs need a wiki link or `no-docs`.
- `codeql.yml`: Python and JS analysis on `develop`, plus a weekly run.
- `labeller.yml`: adds `needs-tests` when relevant.

**Merge:** Mergify auto-merges after one approval and green CI. The `squash` label switches it to squash merge. The `backport <branch>` labels backport to develop or version-1x-hotfix. PRs to stable `version-14/15/16` from non-maintainers are auto-closed.

**Release (upstream model):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` PRs (Tuesdays).
- Pushes to `version-14/15/16` run **semantic-release** (`.releaserc`, angular preset; breaking changes don't auto-release). It bumps `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and creates a GitHub release.
- `release_notes.yml` strips chore/ci/test/docs/style entries from the notes.
- `generate-pot-file.yml` refreshes translations weekly.

Several of these workflows still point at `earthians/biograph` and its secrets. On this fork (`biograph-fh`), CI has no prior run history. Changes to workflow files need a token with `workflow` scope.
