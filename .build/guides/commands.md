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
  - .github/workflows/ci.yml
  - .pre-commit-config.yaml
  - .github/workflows/linters.yml
  - package.json
  - patient_portal/package.json
---

**Install (bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Server tests.** These need a bench site; CI uses `test_site`.
```sh
bench --site test_site run-parallel-tests --app healthcare
# single module/doctype
bench --site test_site run-tests --app healthcare --doctype "Patient Appointment"
```

**Lint and format.** Pre-commit is the single entry point, and CI runs the same thing.
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files
```
The hooks run trailing-whitespace, check-yaml/json/toml/ast, check-merge-conflict, debug-statements, prettier, eslint, pip-audit, `ruff` (lint), `ruff-format` and `detect-secrets`.

**Semgrep (Frappe rules)**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal (Vue)**
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server proxying to frappe
```

**Sanity check that CI also runs:** `python -m compileall -f .` plus a grep for leftover merge-conflict markers.
