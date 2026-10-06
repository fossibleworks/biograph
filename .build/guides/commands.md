---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
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

**Install into a bench**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Run the server tests** (the command CI uses)
```sh
cd ~/frappe-bench
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# narrower runs during development (standard Frappe):
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
```
CI sets up the bench with `.github/helper/install.sh`. Fork branches (`biograph-fh`, `goal/*`) are tested against frappe, erpnext and payments `version-16`.

**Lint and format**
```sh
pip install pre-commit && pre-commit install
npm install            # or yarn; installs eslint + portal deps via postinstall
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml checks
```

**Semgrep** (the same rules as CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn build                 # root script: cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server
# build = vite build --base=/assets/healthcare/patient_portal/
```

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. CI runs it weekly.
