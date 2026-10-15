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
  - .github/helper/update_pot_file.sh
---

This app runs inside a **frappe-bench**. Server commands run from the bench root against a site.

## Install / setup

```sh
bench get-app https://github.com/Tacten/biograph   # or: bench get-app healthcare <path>
bench --site <site> install-app healthcare
bench --site <site> migrate                        # runs patches.txt + after_migrate
```

## Tests (server)

```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1   # what CI runs
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"           # single doctype
```

The site needs `allow_tests` turned on (see `.github/helper/site_config.json`).

## Frontend (Patient Portal)

```sh
yarn install            # root; postinstall runs yarn install in patient_portal
yarn build              # root -> cd patient_portal && yarn build
cd patient_portal && yarn dev   # Vite dev server proxied to bench
bench build --app healthcare    # desk bundles (healthcare.bundle.js)
```

## Lint / format

```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps for the eslint hook
pre-commit run --all-files    # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks

git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Translations

The weekly workflow regenerates `healthcare/locale/main.pot` using `.github/helper/update_pot_file.sh`.
