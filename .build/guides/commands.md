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
  - .github/helper/update_pot_file.sh
---

Server code only runs inside a **Frappe bench**. The repo has no Makefile and no standalone Python test runner.

**Install / run**
```sh
bench get-app https://github.com/Tacten/biograph   # or a local path
bench --site <site> install-app healthcare
bench start
bench --site <site> migrate                       # runs patches.txt + after_migrate
```

**Tests** (the CI form; it needs a site with erpnext + payments + healthcare installed)
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module locally:
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
```
`.github/helper/install.sh` is the reference for building a test bench.

**Lint / format** (pre-commit is the source of truth)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml/ast checks
```

**Semgrep** (Frappe rules, as in CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal**
```sh
yarn install          # root postinstall also installs patient_portal
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. A scheduled workflow runs it every week.
