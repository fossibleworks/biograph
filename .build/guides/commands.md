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
  - .github/workflows/semantic-commits.yml
---

All commands assume a Frappe bench with frappe and erpnext installed.

**Install**
- `bench get-app <repo-url>` and then `bench --site <site> install-app healthcare`
- CI bootstraps with `bash .github/helper/install.sh`.

**Tests** (server side, need a site with the app installed)
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1` (as in CI)
- For one module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint and format** (the same hooks CI runs)
- `pip install pre-commit && pre-commit install && npm install`, then `pre-commit run --all-files`. This runs ruff `--fix`, ruff-format, prettier (js/ts/vue/css/scss), eslint, check-yaml/json/toml/ast, debug-statements, pip-audit and detect-secrets (with `.secrets.baseline`).
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`, then `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`.
- Commit messages are checked with `npx commitlint --from <base> --to <head>`.

**Front end**
- Root `yarn install` runs `postinstall` → `cd patient_portal && yarn install`.
- `yarn build` at the root runs `cd patient_portal && yarn build`, which is `vite build --base=/assets/healthcare/patient_portal/`.
- For portal development: `cd patient_portal && yarn dev`.
- Desk assets: `bench build --app healthcare`.

**Migrations:** `bench --site <site> migrate` runs the patches in `patches.txt` and `after_migrate`.
