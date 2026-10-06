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
  - .github/helper/install.sh
---

**Setup (inside a bench with ERPNext):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Front-end (patient portal):**
```sh
yarn install          # root postinstall runs: cd patient_portal && yarn install --check-files
yarn build            # cd patient_portal && yarn build -> vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server
```

**Lint and format (the same as CI):**
```sh
pip install pre-commit && pre-commit install
npm install           # for the eslint hook
pre-commit run --all-files   # ruff --fix, ruff-format, eslint, prettier, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep (Frappe rules):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Tests (from the bench root):**
```sh
bench --site test_site run-parallel-tests --app healthcare   # what CI runs
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
CI also runs `python -m compileall -f .` and fails the build on leftover `<<<<<<<` conflict markers.
