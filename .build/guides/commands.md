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
  - .github/helper/install.sh
---

**Setup (inside a bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```
CI builds the bench with `.github/helper/install.sh`.

**Tests**
```sh
bench --site test_site run-parallel-tests --app healthcare   # what CI runs
bench --site <site> run-tests --app healthcare [--doctype "Patient Appointment"]
```

**Lint / format** (the same hooks CI runs)
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files    # ruff --fix, ruff-format, eslint, prettier, pip-audit, detect-secrets, yaml/json/toml checks
```

**Semgrep** (Frappe rules, run in CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Commit messages** are checked with `npx commitlint` against the conventional types in `commitlint.config.js`.
