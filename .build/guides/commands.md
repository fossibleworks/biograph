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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
  - .github/helper/install.sh
---

The app runs inside a Frappe bench (`frappe-bench`). Run all commands from the bench or the app directory as shown.

**Install**
- `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`
- CI bootstraps the bench with `bash .github/helper/install.sh`.

**Frontend (patient portal)**
- `yarn install` at the root. Its `postinstall` runs `cd patient_portal && yarn install --check-files`.
- `yarn build`, which runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.

**Tests**
- `bench --site test_site run-parallel-tests --app healthcare` (this is what CI runs)
- `bench --site <site> run-tests --app healthcare [--doctype "Patient Appointment"]` runs a subset locally.

**Lint and format**
- `pre-commit install` then `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`

**Migrations:** `bench --site <site> migrate` runs the entries in `healthcare/patches.txt`.
