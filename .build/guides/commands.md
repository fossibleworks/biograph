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
---

**Setup (bench):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Lint/format (pre-commit runs ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets and basic hygiene hooks):**
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files
```

**Semgrep (Frappe rules, as CI runs them):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Tests (inside a bench):**
```sh
bench --site test_site run-parallel-tests --app healthcare
# or a single module/doctype
bench --site test_site run-tests --app healthcare --doctype "Patient Appointment"
```

**Patient portal frontend:**
```sh
yarn build              # root: cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server
```

**Commit message check:** `npx commitlint --from <base> --to <head>`.

Many legacy files appear in `.pre-commit-config.yaml`'s `exclude` list. To check whether a change adds lint findings, run `ruff check <file>` on those files directly, as the upstream-sync ledger does.
