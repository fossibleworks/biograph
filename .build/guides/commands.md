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
  - .pre-commit-config.yaml
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
---

**Setup (inside a Frappe bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Lint and format** (the same hooks CI runs)
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep** (Frappe rules, as CI runs them)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Tests** (they need a bench site with erpnext and payments installed)
```sh
bench --site test_site run-parallel-tests --app healthcare   # CI
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```

**Patient portal**
```sh
yarn install        # root postinstall installs patient_portal
yarn build          # root: cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server with frappe proxy
```

**Commit titles** are checked with commitlint:
```sh
npx commitlint --from <base> --to <head>
```
