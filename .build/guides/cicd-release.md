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
  - .github/workflows/on_release.yml
  - .github/workflows/initiate_release.yml
  - .releaserc
  - .mergify.yml
  - .github/workflows/codeql.yml
---

**On pull requests**
- `ci.yml` (**Server Tests**): skipped for PRs that only change css, js, md, html or csv. Steps: Python 3.14 and Node 24, `compileall`, a merge-conflict marker check, then `.github/helper/install.sh`, which sets up a bench with frappe, payments and erpnext. Fork branches (`biograph-fh`, `goal/*`) fall back to `version-16` for those apps. Then `bench run-parallel-tests --app healthcare` runs on MariaDB 11.8, with a 30-minute timeout. The workflow also runs daily at 00:00 UTC, and only non-PR runs upload coverage to Codecov.
- `linters.yml` / `linters.v2.yml`: the pre-commit action (ruff, prettier, eslint, pip-audit, detect-secrets and hygiene hooks), plus Semgrep with `frappe/semgrep-rules` and `r/python.lang.correctness`.
- `semantic-commits.yml`: commitlint over the PR's commit range.
- `docs_checker.yml`: a `feat` PR needs a docs link or `no-docs`. Note that `.github/helper/documentation.py` queries the `earthians/biograph` repo API.
- `labeller.yml`: labels PRs automatically. `codeql.yml`: CodeQL security scanning.

**Merging (Mergify):** auto-merge after CI success with at least 1 approval (squash if labelled `squash`, blocked by `dont-merge`). PRs to the stable `version-14/15/16` branches from non-maintainers are auto-closed. The `backport develop` label triggers a backport.

**Release:** `initiate_release.yml` opens weekly release PRs (Tuesday 09:30 UTC). `on_release.yml` runs `npx semantic-release` on pushes to `version-14`, `version-15` and `version-16`. Releases use the angular preset, and breaking changes do not trigger a major bump. The release bumps the version in `healthcare/__init__.py`, commits `chore(release): Bumped to Version x.y.z` and publishes a GitHub release. `release_notes.yml` regenerates the notes. `generate-pot-file.yml` refreshes translations every Sunday.

**Caveats:** workflow files need the `workflow` token scope to change, which is why upstream #86 was deferred. The fork has no historical CI baseline on `biograph-fh`.
