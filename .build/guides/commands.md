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
  - .github/workflows/linters.v2.yml
  - .pre-commit-config.yaml
---

All server commands run inside a **Frappe bench** where `erpnext`, `payments` and this app are installed.

**Install / setup**
- `bench get-app https://github.com/Tacten/biograph` then `bench --site <site> install-app healthcare`
- After a schema change or a new patch: `bench --site <site> migrate`

**Tests** (same as CI)
- `bench --site test_site run-parallel-tests --app healthcare` (CI form)
- Single module: `bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint / format** (from the repo root)
- `pre-commit install` then `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic file hooks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules` then `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`

**Frontend (patient portal)**
- `yarn install` at the root (postinstall installs `patient_portal`)
- `yarn build` at the root, which runs `cd patient_portal && yarn build` (`vite build --base=/assets/healthcare/patient_portal/`)
- `cd patient_portal && yarn dev` starts the Vite dev server, which proxies to Frappe
- Desk JS assets: `bench build --app healthcare`
