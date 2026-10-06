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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
---

**Setup (inside a bench with ERPNext):**
- `bench get-app <repo-url>`, then `bench --site <site> install-app healthcare`
- After schema or patch changes, run `bench --site <site> migrate`.

**Tests (server; needs a bench site):**
- CI runs `bench --site test_site run-parallel-tests --app healthcare`.
- For one DocType locally, use `bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"`, or pass `--module healthcare.healthcare.doctype.<name>.test_<name>`.
- To reproduce the CI environment, see `.github/helper/install.sh`.

**Lint and format:**
- `pip install pre-commit && pre-commit install && npm install`, then `pre-commit run --all-files`. This runs ruff (with `--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Patient portal frontend:**
- `yarn install` at the root also installs `patient_portal` through `postinstall`.
- `yarn build` at the root runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server, which proxies to Frappe.
- Desk JS is built by `bench build --app healthcare`.

**Commit messages:** commitlint checks them with conventional-commit types (see the workflow guide).
