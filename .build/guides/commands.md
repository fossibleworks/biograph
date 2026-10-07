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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
---

All server commands run inside a Frappe bench that has erpnext and healthcare installed.

**Install**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Tests** (what CI runs)
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module/doctype
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
```

**Lint and format**
```sh
pre-commit install && pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal**
```sh
yarn install                 # root; postinstall installs patient_portal
yarn build                   # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Migrations:** `bench --site <site> migrate`. This runs `patches.txt` and the `after_migrate` hook.

**CI sanity checks:** `python -m compileall -f .` and a grep for `^<<<<<<< ` merge markers.
