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
  - .github/workflows/ci.yml
  - package.json
  - patient_portal/package.json
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
---

# Commands

This is a Frappe app, so it is run and tested inside a **bench**. There is no standalone test runner.

## Install / run
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # applies patches.txt + doctype JSON
```

## Tests (as CI runs them)
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module/doctype locally:
bench --site test_site run-tests --app healthcare --doctype "Lab Test"
```
CI bootstraps the bench with `.github/helper/install.sh` and `.github/helper/site_config.json`.

## Lint / format
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks

git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Frontend (Patient Portal)
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # → cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

## Commit-message check
```sh
npx commitlint --from <base> --to <head>
```
