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
  - .github/workflows/linters.v2.yml
  - .pre-commit-config.yaml
  - README.md
  - .github/helper/install.sh
---

# Commands

The app runs inside a Frappe **bench**. Run commands from the bench, or from `apps/healthcare` where noted.

## Install / setup
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`
- `bench --site <site> migrate`: runs the patches in `healthcare/patches.txt`.
- CI bootstrap script: `.github/helper/install.sh`

## Frontend
- `yarn install`: root workspaces. Postinstall runs `cd patient_portal && yarn install --check-files`.
- `yarn build`: builds the patient portal (`vite build --base=/assets/healthcare/patient_portal/`).
- `cd patient_portal && yarn dev`: Vite dev server.

## Tests
- `bench --site test_site run-parallel-tests --app healthcare`: what CI runs.
- `bench --site <site> run-tests --app healthcare [--doctype "Patient Appointment"]`: standard Frappe single-run form.

## Lint / format
- `pre-commit install && pre-commit run --all-files`: ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and basic hygiene hooks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`
