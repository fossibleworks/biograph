---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
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

**Setup (inside a Frappe bench)**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- `bench setup requirements --dev`

**Tests** (as run in CI)
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1`
- Single module locally: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint and format**
- `pre-commit install` then `pre-commit run --all-files`. This runs ruff (`--fix`) and ruff-format, prettier (JS/Vue/CSS, excluding `patient_portal/`), eslint, check-yaml/json/toml/ast, debug-statements, pip-audit and detect-secrets.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`

**Frontend (patient portal)**
- `yarn install` at the root (postinstall installs `patient_portal`)
- `yarn build` at the root, which runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`
- `cd patient_portal && yarn dev` for the Vite dev server (proxies to Frappe)
- `bench build --app healthcare` for the Desk bundle

**Migrations:** `bench --site <site> migrate` runs the entries in `healthcare/patches.txt`.
