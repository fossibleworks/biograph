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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/release_notes.yml
  - .releaserc
  - .mergify.yml
  - .github/helper/install.sh
---

**On pull requests:**
- `ci.yml`, *Server Tests*:
  - Skipped for PRs touching only css/js/md/html/csv. Also runs nightly at 00:00 UTC.
  - Sets up Python 3.14 + Node 24 + MariaDB 11.8.
  - Checks the code compiles (`compileall`) and greps for merge-conflict markers.
  - Builds a bench via `.github/helper/install.sh` with frappe, payments and erpnext on the base branch (fork branches fall back to `version-16`), installs `healthcare`, and runs `bench run-parallel-tests`.
  - Coverage goes to Codecov on non-PR runs only.
- `linters.yml` / `linters.v2.yml`: pre-commit (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, hygiene) plus Semgrep with Frappe rules and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR range.
- `docs_checker.yml`: feat PRs need a wiki link or `no-docs`.
- `labeller.yml`: auto-labels PRs.
- `codeql.yml`: Python and JS analysis on `develop` and weekly.

**Merge:** Mergify merges after ≥1 approval and CI. The `squash` label squashes; the `backport develop` label backports.

**Release (upstream-style, earthians):**
- `initiate_release.yml` opens weekly `version-N-hotfix → version-N` release PRs for N = 14, 15, 16 every Tuesday.
- `on_release.yml` runs **semantic-release** on pushes to `version-14/15/16`. Per `.releaserc`, it uses the angular preset, breaking changes do not trigger a major bump, it rewrites the version in `healthcare/__init__.py`, and it commits `chore(release): Bumped to Version x.y.z`.
- `release_notes.yml` regenerates GitHub release notes and strips chore/ci/test/docs/style entries.
- `generate-pot-file.yml` refreshes translations weekly.

**Fork caveats:**
- Several workflows hard-code `earthians/biograph` and earthians bot tokens.
- The fork's default branch `biograph-fh` has no CI run history.
- The push credential used by automation cannot modify `.github/workflows/*`. The upstream #86 change was skipped for this reason, so workflow-file changes must be applied by hand.

Deployment is via Frappe Cloud / bench (`bench get-app` + `install-app` + `migrate`, which runs `patches.txt` and `after_migrate`).
