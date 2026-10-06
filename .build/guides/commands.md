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
  - .github/workflows/linters.v2.yml
---

All server commands run inside a Frappe bench (`~/frappe-bench`) with this app installed as `healthcare`.

**Setup**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
yarn install          # root; postinstall runs `yarn install --check-files` in patient_portal
```

**Build**
```sh
yarn build                       # root -> cd patient_portal && yarn build
cd patient_portal && yarn dev    # vite dev server for the portal
bench build --app healthcare     # desk JS bundle
```

**Test** (as CI runs them)
```sh
bench --site test_site run-parallel-tests --app healthcare
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.lab_test.test_lab_test
```

**Lint and format**
```sh
pip install pre-commit && pre-commit install
pre-commit run --all-files       # ruff --fix, ruff-format, prettier, eslint, detect-secrets, pip-audit, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```
`.pre-commit-config.yaml` excludes many legacy files from pre-commit. For files in that list, run `ruff check <file>` directly and make sure the finding count does not go up. The sync ledger does this.

**Migrations:** `bench --site <site> migrate` runs the patches in `healthcare/patches.txt`.
