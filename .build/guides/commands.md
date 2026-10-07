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
  - .github/helper/update_pot_file.sh
---

**Install (in a bench):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Server tests** (the same command CI uses):
```sh
bench --site test_site run-parallel-tests --app healthcare
# or for a single doctype/module
bench --site test_site run-tests --app healthcare --doctype "Patient Appointment"
```
CI sets up the bench with `.github/helper/install.sh`.

**Lint / format** (pre-commit runs ruff `--fix`, ruff-format, prettier, eslint, pip-audit and detect-secrets):
```sh
pip install pre-commit && pre-commit install && npm install
pre-commit run --all-files
```

**Semgrep** (Frappe rules, the same as CI):
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal:**
```sh
yarn install        # postinstall installs patient_portal
yarn build          # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Commit titles** are checked with `npx commitlint` (conventional types).

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
