---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - README.md
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .pre-commit-config.yaml
---

All server commands run inside a Frappe bench (`~/frappe-bench`) with the app installed. Each command below is followed by the file it comes from.

**Setup**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare` (README)
- CI bootstrap: `bash .github/helper/install.sh` (creates a bench, a MariaDB `test_site`, and installs payments, erpnext and healthcare)

**Tests**
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1` (CI)
- A single module locally: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<dt>.test_<dt>` (standard Frappe)

**Lint and format** (README → Development)
- `pip install pre-commit && pre-commit install && npm install`
- `pre-commit run --all-files`: ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets, plus yaml/json/toml/ast/merge-conflict/debug-statement checks
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && pip install semgrep && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Sanity check from CI: `python -m compileall -f .` and grep for `^<<<<<<< ` conflict markers

**Frontend (patient portal)**
- `yarn install` at the root (postinstall installs `patient_portal`)
- `yarn build` (→ `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`)
- `cd patient_portal && yarn dev` (Vite dev server)
- Desk assets: `bench build --app healthcare`

**Migrations:** `bench --site <site> migrate` runs `patches.txt` and the `after_migrate` hook.

**Commit check:** `npx commitlint --from <base> --to <head>`
