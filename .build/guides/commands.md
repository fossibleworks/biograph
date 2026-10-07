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
---

**Install (bench):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Tests (server):**
```sh
bench --site test_site run-parallel-tests --app healthcare   # what CI runs
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>
```

**Lint and format:**
```sh
pip install pre-commit && pre-commit install && npm install
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep (Frappe rules):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal frontend:**
```sh
yarn install          # root postinstall installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Commit message check:** `npx commitlint --from <base> --to <head>`
