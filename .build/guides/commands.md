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
  - .github/workflows/linters.yml
  - .pre-commit-config.yaml
  - .github/helper/install.sh
---

# Commands

The app runs inside a Frappe **bench**, not on its own.

## Setup
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench setup requirements --dev
```

## Tests (server)
```sh
bench --site <site> run-tests --app healthcare                # all tests
bench --site <site> run-tests --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
bench --site test_site run-parallel-tests --app healthcare     # what CI runs
```

## Lint and format
```sh
pip install pre-commit && pre-commit install
pre-commit run --all-files    # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks

# Semgrep (also runs in CI)
git clone --depth 1 https://github.com/frappe/semgrep-rules.git frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Frontend
```sh
yarn install                         # root postinstall also installs patient_portal
yarn build                           # = cd patient_portal && yarn build
cd patient_portal && yarn dev        # vite dev server, proxies to frappe
bench build --app healthcare         # build Desk assets (healthcare.bundle.js)
```

## Migrations
```sh
bench --site <site> migrate          # runs patches.txt and after_migrate
```
