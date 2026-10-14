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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - package.json
  - patient_portal/package.json
  - .github/workflows/semantic-commits.yml
---

All of these run inside a Frappe bench (`~/frappe-bench`) that has frappe, erpnext and payments installed.

**Install / setup**
```sh
bench get-app https://github.com/Tacten/biograph   # or a local path
bench --site <site> install-app healthcare
bench --site <site> migrate                        # runs patches.txt + after_migrate
```
CI bootstrap script: `bash .github/helper/install.sh`. It runs bench init, gets payments and erpnext on the matching branch (falling back to `version-16` for fork branches), sets up `test_site`, and reinstalls it.

**Tests**
```sh
bench --site test_site run-parallel-tests --app healthcare            # what CI runs
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.fee_validity.test_fee_validity
```

**Lint / format** (mirrors CI)
```sh
pip install pre-commit && pre-commit install
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal frontend**
```sh
yarn install              # root postinstall installs patient_portal
yarn build                # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server (frappeProxy to bench)
```

**Commit-message check**: `npx commitlint --from <base> --to <head>`.
