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
  - .github/helper/install.sh
---

**Install** (inside a Frappe bench that has ERPNext)
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs patches.txt + after_migrate
```

**Tests** (server-side, run in a bench; the same command CI uses)
```sh
bench --site test_site run-parallel-tests --app healthcare
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
```
The test site needs `allow_tests`. CI provisions it with `.github/helper/install.sh` and `.github/helper/site_config.json`.

**Lint and format**
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml checks
```

**Semgrep** (same rules CI uses)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn install           # root postinstall also installs patient_portal
yarn build             # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server with the Frappe proxy
```

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. CI runs it weekly.
