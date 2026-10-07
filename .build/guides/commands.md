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
  - .github/workflows/linters.v2.yml
  - package.json
  - patient_portal/package.json
  - .github/workflows/semantic-commits.yml
---

Server commands run inside a **Frappe bench** where ERPNext is installed.

**Install**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Tests** (the same command CI runs)
```sh
cd ~/frappe-bench
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# or a single module/doctype:
bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"
```

**Lint and format** (pre-commit runs trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, ruff `--fix`, ruff-format and detect-secrets)
```sh
pip install pre-commit
pre-commit install
npm install
pre-commit run --all-files
# files in pre-commit's exclude list: run ruff directly
ruff check <file> && ruff format <file>
```

**Semgrep** (Frappe rules, as in CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal frontend**
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # Vite dev server with frappe proxy
```

**Desk assets:** `bench build --app healthcare`.

**Commit messages** are checked with `npx commitlint --from <base> --to <head>`.
