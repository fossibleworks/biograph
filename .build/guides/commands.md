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
  - .github/helper/install.sh
  - .github/workflows/semantic-commits.yml
---

# Commands

The app runs inside a **Frappe bench**. It is not run standalone.

## Install (bench)
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```
CI bootstraps a bench with `bash .github/helper/install.sh`.

## Tests
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare
# single doctype / module (standard Frappe):
bench --site test_site run-tests --app healthcare --doctype "Patient Appointment"
```

## Lint and format
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```
Semgrep (Frappe rules):
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient Portal
```sh
yarn install            # root postinstall runs yarn install in patient_portal
yarn build              # root: cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server with frappe proxy
```

## Commit titles
Commitlint checks commit titles: `npx commitlint --from <base> --to <head>`.
