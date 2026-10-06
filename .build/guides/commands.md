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
  - .github/helper/update_pot_file.sh
---

**Install (requires a Frappe bench with ERPNext)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Run tests** (matches CI)
```sh
cd ~/frappe-bench
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module/doctype:
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"
```
CI sets up the bench with `.github/helper/install.sh`.

**Lint and format**
```sh
pip install pre-commit && pre-commit install
npm install            # root; postinstall also installs patient_portal deps
pre-commit run --all-files   # ruff --fix, ruff-format, eslint, prettier, pip-audit, detect-secrets, yaml/json/toml/ast checks

# Frappe semgrep rules (same as CI)
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal frontend**
```sh
yarn build                 # root → cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server (frappeProxy)
```

**Commit-message check:** `npx commitlint --from <base> --to <head>`.

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
