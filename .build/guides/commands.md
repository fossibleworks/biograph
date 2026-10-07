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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
---

**Install (in a bench with ERPNext):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Server tests** (as CI runs them):
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
The CI bench setup lives in `.github/helper/install.sh`.

**Lint and format:**
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml/ast checks
```

**Semgrep** (Frappe rules, also run in CI):
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal:**
```sh
yarn install          # root postinstall runs yarn install in patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Commit-message check:** `npx commitlint --from <base> --to <head>`.

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
