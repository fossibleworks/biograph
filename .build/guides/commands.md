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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - README.md
  - .github/helper/install.sh
---

You need a Frappe bench with ERPNext installed. There is no local npm test script.

**Install**
- `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`
- CI bootstraps with `bash .github/helper/install.sh`

**Test (server)**
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1` (as in CI)
- For a single module: `bench --site <site> run-tests --app healthcare --module <dotted.module>` (standard Frappe)

**Lint / format**
- `pre-commit install && pre-commit run --all-files` (runs ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and basic hooks)
- `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles are checked by `npx commitlint --from <base> --to <head>`

**Frontend (patient portal)**
- `yarn install` (root `postinstall` also installs `patient_portal`)
- `yarn build` at the root, which runs `cd patient_portal && yarn build` (`vite build --base=/assets/healthcare/patient_portal/`)
- `cd patient_portal && yarn dev` for the Vite dev server (proxies to Frappe)

**Migrations**
- `bench --site <site> migrate` (runs `patches.txt` and `after_migrate`)
