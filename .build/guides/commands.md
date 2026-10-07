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
  - README.md
  - .github/workflows/ci.yml
  - .pre-commit-config.yaml
---

**Install (bench):**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`

**Patient portal:**
- `yarn install` at the root (postinstall runs `cd patient_portal && yarn install --check-files`)
- `yarn build` at the root, or `cd patient_portal && yarn build` (`vite build --base=/assets/healthcare/patient_portal/`)
- `cd patient_portal && yarn dev`: Vite dev server

**Lint and format:**
- `pre-commit install` and `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets, and basic checks.
- `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness` (clone `frappe/semgrep-rules` first)
- `npx commitlint --from <base> --to <head>`

**Tests:**
- `bench --site test_site run-parallel-tests --app healthcare` (what CI runs)
- `bench --site <site> run-tests --app healthcare [--doctype "<DocType>"]` for local runs

**Migrations:** `bench --site <site> migrate` runs `patches.txt`.
