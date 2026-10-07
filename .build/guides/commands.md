---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - package.json
  - patient_portal/package.json
  - README.md
---

**Install (bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Tests** (inside a bench; CI does this exactly)
```sh
cd ~/frappe-bench && bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module/doctype locally:
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"
```
The CI bench is set up by `.github/helper/install.sh`.

**Lint / format** (same as the CI `linters` job)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files   # ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep (Frappe rules)**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn install           # postinstall installs patient_portal
yarn build             # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server with frappe proxy
```

**Quick sanity check** (from CI)
```sh
python -m compileall -f .
```
