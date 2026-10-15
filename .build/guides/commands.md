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

# Commands

The app runs inside a **Frappe bench**. It cannot run standalone.

## Install into a bench
```sh
bench get-app <repo-url>
bench --site <site> install-app healthcare
bench --site <site> migrate          # applies patches.txt + DocType JSON
```

## Tests (server)
```sh
bench --site test_site run-tests --app healthcare                 # all
bench --site test_site run-tests --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1   # what CI runs
```
CI builds the bench with `.github/helper/install.sh`: Frappe and ERPNext on the matching branch, plus the payments app.

## Lint / format
```sh
pip install pre-commit && pre-commit install
npm install                       # eslint deps for the eslint hook
pre-commit run --all-files        # ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient portal
```sh
yarn install                      # root postinstall installs patient_portal
yarn build                        # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev     # Vite dev server (frappeProxy to bench)
```
