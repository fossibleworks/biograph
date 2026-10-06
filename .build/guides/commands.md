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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/helper/install.sh
---

**Install (in a bench with ERPNext)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs patches.txt
```

**Frontend (patient portal)**
```sh
yarn install            # root postinstall also installs patient_portal
yarn build              # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server with frappe proxy
```

**Lint and format (the same checks CI runs)**
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks

git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Tests (Frappe test runner, inside a bench)**
```sh
bench --site <site> set-config allow_tests true
bench --site <site> run-tests --app healthcare
bench --site <site> run-tests --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
`.github/helper/install.sh` builds a CI bench (frappe, erpnext and payments on `version-16`), but no test workflow is currently checked in.
