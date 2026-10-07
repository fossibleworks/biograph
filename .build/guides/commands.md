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
  - .github/workflows/semantic-commits.yml
---

# Commands

The app runs inside a **Frappe bench**. There is no standalone run command.

## Install / run
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # applies patches.txt + doctype JSON
```

## Patient portal (frontend)
```sh
yarn install                          # root; postinstall installs patient_portal
yarn build                            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev         # vite dev server (frappe proxy)
```

## Tests (as CI runs them)
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare
# single module locally:
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.lab_test.test_lab_test
```

## Lint / format
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files            # ruff (--fix) + ruff-format, eslint, prettier, detect-secrets, pip-audit, yaml/json/toml/ast checks
```

## Semgrep (as CI runs it)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Commit-message lint
`npx commitlint --from <base> --to <head>`
