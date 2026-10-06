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
  - .github/workflows/linters.v2.yml
  - package.json
  - patient_portal/package.json
  - .github/workflows/semantic-commits.yml
---

**Install (in a Frappe bench with ERPNext):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs patches.txt
```

**Tests (as CI runs them):**
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module/doctype locally:
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"
```

**Lint and format (pre-commit runs everything):**
```sh
pip install pre-commit && pre-commit install
npm install        # eslint deps
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep (Frappe rules, as in CI):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal:**
```sh
yarn install             # root postinstall installs patient_portal deps
yarn build               # → cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server proxied to Frappe
```

**Commit-message check:** `npx commitlint --from <base> --to <head>`.
