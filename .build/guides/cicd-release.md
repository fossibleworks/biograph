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
  - .github/workflows/linters.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - .github/workflows/initiate_release.yml
  - .github/workflows/on_release.yml
  - .releaserc
  - .github/release.yml
  - .mergify.yml
  - codecov.yml
  - healthcare/patches.txt
---

**PR checks (GitHub Actions)**
- **`ci.yml` (Server Tests):**
  - Runs on PRs, skipping changes that only touch `.css/.js/.md/.html/.csv`, and nightly at 00:00 UTC.
  - Steps: Ubuntu, Python 3.14, Node 24, MariaDB 11.8 service → `compileall` and a merge-conflict-marker check → `.github/helper/install.sh`, which installs frappe-bench and clones frappe, payments and erpnext on the matching branch.
  - Fork branches such as `biograph-fh` and `goal/*` fall back to `version-16`.
  - Then `bench --site test_site run-parallel-tests --app healthcare`, with a 30-minute timeout.
  - Coverage is uploaded to Codecov only on non-PR runs.
- **`linters.yml` / `linters.v2.yml`:** pre-commit (ruff, ruff-format, eslint, prettier, pip-audit, detect-secrets, and others) plus Semgrep with `frappe/semgrep-rules` and `r/python.lang.correctness`.
- **`semantic-commits.yml`:** commitlint over the PR's commits.
- **`docs_checker.yml`:** `feat` PRs need a wiki docs link.
- **`labeller.yml`, `codeql.yml`:** labelling and CodeQL analysis.
- Dependabot is configured in `.github/dependabot.yml`.

**Merge:** Mergify merges automatically after at least 1 approval and green CI, and squashes when the `squash` label is set.

**Release (inherited from upstream)**
- `initiate_release.yml` runs weekly, on Tuesday at 09:30 UTC. It opens `chore: release v{14,15,16}` PRs from `version-N-hotfix` into `version-N` on `earthians/biograph`.
- `on_release.yml` runs on a push to `version-14/15/16`. It runs **semantic-release** (`.releaserc`) with these steps:
  - analyse commits with the angular preset; breaking changes do not trigger a major release
  - generate notes
  - bump the version string in `healthcare/__init__.py`
  - commit `chore(release): Bumped to Version x.y.z`
  - create a GitHub release
- `release_notes.yml` and `.github/release.yml` build the changelog. PRs labelled `skip-release-notes` are excluded.
- Translations: `generate-pot-file.yml` regenerates `main.pot` weekly, and Crowdin opens `fix: sync translations from crowdin` PRs.

**Fork caveats**
- Release workflows target `earthians` and need `EARTHIANS_BOT_TOKEN`. They are not active for the `biograph-fh` fork.
- The fork has no CI run history (see the sync ledger).
- Versions in the fork are sometimes bumped by hand, for example `chore: bump version to 16.0.8`.
- Changes to workflow files need a credential with `workflow` scope.

**Deployment:** install on Frappe benches or Frappe Cloud with `bench get-app` / `install-app healthcare`. Migrations run through `patches.txt` and `after_migrate` on `bench migrate`.
