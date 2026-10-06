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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/workflows/ci.yml
  - README.md
  - commitlint.config.js
---

**Setup (bench):**
```sh
bench get-app <repo-url>            # add app to a bench that already has ERPNext
bench --site <site> install-app healthcare
bench --site <site> migrate         # runs patches.txt + doctype JSON sync
```

**Lint and format** (the same checks CI runs):
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps for the eslint hook
pre-commit run --all-files   # trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, ruff --fix, ruff-format, detect-secrets
```
Semgrep (Frappe rules):
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```
Many legacy files are in the pre-commit `exclude` list. To lint those, run ruff on them directly: `ruff check <file>`.

**Tests** (inside a bench):
```sh
bench --site test_site run-tests --app healthcare [--doctype "Patient Appointment"]
bench --site test_site run-parallel-tests --app healthcare   # what CI runs
```

**Patient Portal frontend:**
```sh
yarn install          # postinstall installs patient_portal deps
yarn build            # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev   # vite dev server
```

**Commit messages** must pass commitlint (conventional commits):
`npx commitlint --from <base> --to <head>`
