---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
---

The app runs inside a Frappe **bench**, not on its own.

**Install / run**
- `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`
- `bench --site <site> migrate` runs `patches.txt` and `after_migrate`.

**Frontend (Patient Portal)**
- `yarn install` at the root. Its postinstall runs `cd patient_portal && yarn install`.
- `yarn build` runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server, which proxies to Frappe.

**Tests**
- `bench --site test_site run-parallel-tests --app healthcare` (as in CI)
- `bench --site <site> run-tests --app healthcare [--doctype "Patient Appointment"]`

**Lint / format**
- `pre-commit install && pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets, and the yaml/json/toml/ast checks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`
