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
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - commitlint.config.js
---

**Install (into a bench that has ERPNext)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs healthcare/patches.txt
```

**Tests** (they need a bench site; CI calls `.github/helper/install.sh`)
```sh
bench --site test_site run-parallel-tests --app healthcare            # what CI runs
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"   # single doctype
```

**Lint/format** (pre-commit runs ruff, ruff-format, prettier, eslint, detect-secrets, pip-audit, and yaml/json/toml/ast checks)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files
ruff check --fix . && ruff format .
```

**Semgrep (Frappe rules)**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal**
```sh
yarn install                 # root postinstall installs patient_portal
yarn build                   # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server proxied to Frappe
```

**Commit messages** must pass commitlint: `type(scope): subject`, where type is one of build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test.
