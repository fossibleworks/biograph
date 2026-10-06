---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - README.md
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
---

All server commands run inside a Frappe bench (`~/frappe-bench`) with ERPNext installed.

**Install**
- `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`
- To reproduce CI setup, follow `.github/helper/install.sh`.

**Test**
- All tests: `bench --site test_site run-parallel-tests --app healthcare` (CI form)
- One module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<dt>.test_<dt>` (standard Frappe)

**Lint and format**
- `pre-commit install` once, then `pre-commit run --all-files`. This runs ruff (with `--fix`), ruff-format, prettier, eslint, detect-secrets, pip-audit and basic file checks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`

**Frontend (Patient Portal)**
- `yarn install` at the root. Its postinstall runs install in `patient_portal`.
- `yarn build` at the root, which runs `cd patient_portal && yarn build`, which runs `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server.
- Desk assets: `bench build --app healthcare`.

**Migrations:** `bench --site <site> migrate` runs `patches.txt` and the `after_migrate` hook.
