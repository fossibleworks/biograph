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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
---

**Install (Frappe bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
bench --site <site> migrate          # runs healthcare/patches.txt
```

**Run tests** (Frappe test runner, needs a bench site with ERPNext):
```sh
bench --site <site> run-tests --app healthcare
bench --site <site> run-tests --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```

**Patient portal frontend**
```sh
yarn install                 # root postinstall runs `cd patient_portal && yarn install --check-files`
yarn build                   # → cd patient_portal && yarn build (vite build --base=/assets/healthcare/patient_portal/)
cd patient_portal && yarn dev   # vite dev server proxied to Frappe
```

**Lint / format** (the same checks CI runs)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps
pre-commit run --all-files     # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Commit titles** are checked with `npx commitlint` (Conventional Commits; see `commitlint.config.js`).
