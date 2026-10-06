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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
---

All server commands run inside a Frappe bench that has erpnext and payments installed. There is no Makefile.

**Install / setup**
- `bench get-app <repo-url>` and then `bench --site <site> install-app healthcare`
- `bench setup requirements --dev`

**Run / build**
- `bench start`
- `yarn install` at the root (postinstall installs `patient_portal`)
- `yarn build`: builds the portal (`cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`)
- `cd patient_portal && yarn dev`: Vite dev server with the Frappe proxy
- `bench build --app healthcare`: builds the desk assets
- `bench --site <site> migrate`: runs the patches in `healthcare/patches.txt`

**Test**
- `bench --site test_site run-tests --app healthcare` (optionally `--module healthcare.healthcare.doctype.<name>.test_<name>`)
- In CI: `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1`

**Lint / format**
- `pre-commit install` and then `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, check-yaml/json/toml/ast, debug-statements, detect-secrets (baseline `.secrets.baseline`) and pip-audit.
- `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`
