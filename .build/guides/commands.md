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
  - .github/helper/install.sh
---

**Install (in a bench with ERPNext):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Run the tests (as CI does):**
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module locally
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
CI provisions a bench with `.github/helper/install.sh`.

**Lint and format:**
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep with Frappe rules:**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal frontend:**
```sh
yarn install          # postinstall installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
