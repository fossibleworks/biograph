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
  - .github/helper/update_pot_file.sh
---

All app commands run inside a Frappe bench (`~/frappe-bench`) with ERPNext and payments installed.

**Setup**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # applies healthcare/patches.txt + doctype JSON
```

**Tests**
```sh
bench --site test_site run-tests --app healthcare [--doctype "Patient Appointment"]
bench --site test_site run-parallel-tests --app healthcare   # what CI runs
```

**Lint / format** (pre-commit runs ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, and the basic hooks)
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files
```

**Semgrep** (Frappe rules, same as CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn install            # postinstall installs patient_portal deps
yarn build              # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. A scheduled workflow runs it.
