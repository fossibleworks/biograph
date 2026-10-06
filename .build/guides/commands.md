---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - README.md
  - commitlint.config.js
---

Run these from a Frappe bench that has `frappe`, `payments`, `erpnext` and this app installed. CI shows the full setup in `.github/helper/install.sh`.

**Install / setup**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench setup requirements --dev
```

**Tests (server)**
```sh
bench --site test_site run-parallel-tests --app healthcare            # what CI runs
bench --site <site> run-tests --app healthcare --doctype "Fee Validity" # single doctype
```

**Lint / format**
```sh
pip install pre-commit && pre-commit install && npm install
pre-commit run --all-files     # ruff (--fix) + ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal (Vue)**
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Migrations**: `bench --site <site> migrate`. This runs patches from `healthcare/patches.txt` and `after_migrate`.

**Commit messages**: commitlint checks them in CI. Conventional types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test.
