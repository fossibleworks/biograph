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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - README.md
  - .github/workflows/semantic-commits.yml
---

## Setup (bench)
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```
CI builds this setup with `.github/helper/install.sh`. That script does a bench init, then `bench get-app payments` and `erpnext`, then `bench get-app healthcare $GITHUB_WORKSPACE`, then `bench setup requirements --dev`, then `install-app`.

## Tests
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare
# single module/doctype (standard Frappe):
bench --site test_site run-tests --app healthcare --doctype "Fee Validity"
```

## Lint / format
```sh
pip install pre-commit && pre-commit install
npm install   # eslint deps
pre-commit run --all-files   # ruff (--fix), ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient portal
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # root → cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server (frappe proxy)
```

## Commit lint
`npx commitlint --from <base> --to <head>`
