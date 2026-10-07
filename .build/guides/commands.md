---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
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

## Install (inside a bench with ERPNext)

```sh
bench get-app <repo-url>
bench --site <site> install-app healthcare
```

## Tests

This is how CI runs them:

```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
```

Locally, `bench --site <site> run-tests --app healthcare [--module ...]` is the usual Frappe equivalent.

The CI environment is set up by `.github/helper/install.sh`. Fork branches (`biograph-fh`, `goal/*`) clone Frappe/ERPNext `version-16`.

## Lint and format

```sh
pip install pre-commit && pre-commit install && npm install
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Patient portal

```sh
yarn install          # root postinstall runs yarn install in patient_portal
yarn build            # root → cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server
```

The portal build is `vite build --base=/assets/healthcare/patient_portal/`.

## Commit check

```sh
npx commitlint --from <base> --to <head>
```
