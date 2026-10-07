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
  - README.md
  - .pre-commit-config.yaml
  - .github/workflows/ci.yml
  - .github/workflows/linters.yml
  - .github/helper/install.sh
---

**Setup (inside a Frappe bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**JavaScript**
- `yarn install`: root workspace install. A postinstall step runs `cd patient_portal && yarn install --check-files`.
- `yarn build`: builds the Patient Portal (`vite build --base=/assets/healthcare/patient_portal/`).
- `cd patient_portal && yarn dev`: Vite dev server, which proxies to Frappe.

**Lint and format** (the same checks CI runs)
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Tests** (need a bench with erpnext and payments; CI uses the site `test_site`)
```sh
bench --site test_site run-parallel-tests --app healthcare
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
CI also runs `python -m compileall -f .` and greps for merge-conflict markers.
