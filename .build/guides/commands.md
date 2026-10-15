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
  - README.md
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
---

The app runs inside a **Frappe bench**. Most commands run from the bench root, not from this repo.

## Install

```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

## Tests

CI runs the tests like this:

```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
```

Run the tests for a single DocType or module locally:

```sh
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"
```

## Lint and format

Run these from `apps/healthcare`:

```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files
```

The pre-commit hooks are ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks.

Semgrep:

```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

## Frontend (patient portal)

```sh
yarn install              # root postinstall runs yarn install in patient_portal
yarn build                # = cd patient_portal && yarn build (vite build --base=/assets/healthcare/patient_portal/)
cd patient_portal && yarn dev   # vite dev server
```

Build the Desk assets with `bench build --app healthcare`.

## Migrations

```sh
bench --site <site> migrate   # runs patches.txt and after_migrate
```
