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
  - .pre-commit-config.yaml
  - README.md
  - .github/workflows/ci.yml
  - .github/helper/install.sh
---

## Install (inside a Frappe bench that already has ERPNext)
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`

## Frontend (patient portal)
- `yarn install`: the root `postinstall` also runs `yarn install --check-files` inside `patient_portal`.
- `yarn build`, which runs `cd patient_portal && yarn build` (that is, `vite build --base=/assets/healthcare/patient_portal/`).
- `cd patient_portal && yarn dev`: the Vite dev server with the Frappe proxy.

## Lint and format
- One-time setup: `pip install pre-commit && pre-commit install && npm install`.
- `pre-commit run --all-files` runs:
  - trailing-whitespace, check-yaml/json/toml/ast, check-merge-conflict, debug-statements
  - prettier
  - eslint (`--quiet`)
  - pip-audit
  - `ruff --fix` and `ruff-format`
  - detect-secrets (baseline `.secrets.baseline`)
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

## Tests
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1` is what CI runs.
- To run a single module locally: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`. This is standard Frappe usage.
- CI sets up the bench with `.github/helper/install.sh`.
