---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - README.md
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - package.json
  - patient_portal/package.json
  - healthcare/patches.txt
---

# Commands

The app runs inside a Frappe bench. There is no standalone run command.

## Install
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

## Server tests (as CI runs them)
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single doctype, standard Frappe form:
bench --site test_site run-tests --app healthcare --doctype "Patient Appointment"
```
CI sets up the bench with `.github/helper/install.sh`.

## Lint / format
```sh
pip install pre-commit && pre-commit install
npm install   # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml checks
```

Semgrep, as in CI:
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient portal
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

## Migrations
Add a patch module under `healthcare/patches/vXX_0/` and list it in `healthcare/patches.txt`. Then run `bench --site <site> migrate`.
