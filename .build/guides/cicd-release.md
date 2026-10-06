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
  - .github/workflows/release_notes.yml
  - .releaserc
  - .mergify.yml
  - codecov.yml
---

**PR checks** (`.github/workflows/`)
- `ci.yml` (**Server Tests**) runs on PRs, except those touching only css/js/md/html/csv and except `version-*-beta` branches, and nightly at 00:00 UTC. Steps: Python 3.14 + Node 24, `compileall`, and a scan for merge-conflict markers. Then it sets up a bench (`.github/helper/install.sh`) with MariaDB 11.8 and runs `bench --site test_site run-parallel-tests --app healthcare`, with a 30-minute timeout. Coverage is collected only on non-PR runs and uploaded to Codecov.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, prettier, eslint, detect-secrets, pip-audit, …) plus Frappe Semgrep rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: `feat` PRs need a docs link or `no-docs`.
- `codeql.yml`: python and javascript, on `develop` plus weekly.
- `labeller.yml`: auto-labels such as `needs-tests`.

**Merging:** Mergify merges after at least 1 approval and green CI. The `squash` label switches to a squash merge, `dont-merge` blocks merging, and `backport <branch>` labels open backports.

**Release (inherited from upstream earthians):**
- `initiate_release.yml` opens weekly (Tuesday) `chore: release vN` PRs from `version-N-hotfix` → `version-N` for N = 14, 15, 16.
- `on_release.yml`: each push to `version-14/15/16` runs **semantic-release** (`.releaserc`: angular preset, breaking changes do not trigger a major bump). It rewrites the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z`, and creates a GitHub release.
- `release_notes.yml` regenerates the notes and strips chore/ci/test/docs/style entries. PRs labelled `skip-release-notes` are excluded (`.github/release.yml`).
- `generate-pot-file.yml` regenerates translations weekly. Dependabot is configured.

**Fork caveats:** several workflows hard-code `earthians/biograph`, `develop`, and earthians bot secrets. The fork's default branch is `biograph-fh`, and per the sync ledger `ci.yml` has never run on this fork. The sync credential cannot push changes under `.github/workflows/` (B2 #86 was skipped for that reason). Workflow edits must be applied by hand.
