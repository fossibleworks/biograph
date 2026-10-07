---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - README.md
  - package.json
  - patient_portal/package.json
  - .github/workflows/linters.v2.yml
  - .pre-commit-config.yaml
---

This app runs inside a Frappe **bench**. Most commands assume a bench with ERPNext installed.

**Install**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs patches.txt + after_migrate
```

**Tests** (Frappe test runner)
```sh
bench --site <site> run-tests --app healthcare
bench --site <site> run-tests --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```

**Lint and format** (the same hooks CI runs)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files
```
This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets, and the yaml/json/toml/ast checks.

**Semgrep** (Frappe rules, also in CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal**
```sh
yarn install            # root; postinstall installs patient_portal
yarn build              # root -> cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server (frappe proxy)
```
