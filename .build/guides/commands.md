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
  - .github/helper/install.sh
  - .github/workflows/semantic-commits.yml
---

# Commands

The app runs inside a **Frappe bench**. There is no standalone run command.

## Setup
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```
CI bootstraps a bench from scratch with `.github/helper/install.sh`.

## Tests (server)
```sh
bench --site test_site run-parallel-tests --app healthcare            # CI form
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<x>.test_<x>
```
The site needs `allow_tests` enabled (see `.github/helper/site_config.json`).

## Lint and format
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps for the eslint hook
pre-commit run --all-files   # ruff (--fix), ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks

git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient Portal
```sh
yarn install           # root postinstall installs patient_portal deps
yarn build             # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server with Frappe proxy
```

## Commit message check
```sh
npx commitlint --from <base> --to <head>
```
