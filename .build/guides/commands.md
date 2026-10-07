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

## Setup (bench)

```sh
bench get-app <repo-url>
bench --site <site> install-app healthcare
```

## Tests

Tests run through bench, inside a site that has erpnext and payments installed:

```sh
bench --site test_site run-tests --app healthcare            # all
bench --site test_site run-tests --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K   # what CI runs
```

`bench --site <site> migrate` runs the patches listed in `healthcare/patches.txt`.

## Lint and format

```sh
pip install pre-commit && pre-commit install
pre-commit run --all-files     # ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient portal

```sh
yarn install          # root; postinstall installs patient_portal
yarn build            # root -> cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server (frappe proxy)
```

## Commit linting

```sh
npx commitlint --from <base> --to <head>
```
