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
  - .github/helper/install.sh
---

Run inside a Frappe bench that already has ERPNext installed:

- **Install app:** `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- **Migrate (runs patches):** `bench --site <site> migrate`
- **Run tests:** `bench --site <site> run-tests --app healthcare` (add `--doctype "Patient Appointment"` to run one doctype). CI sets up its bench with `.github/helper/install.sh`.
- **Build desk assets:** `bench build --app healthcare`
- **Patient portal:** `yarn install` at the repo root (its postinstall runs install in `patient_portal`), then `yarn build` (= `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`). For dev, run `cd patient_portal && yarn dev`.
- **Lint and format (all hooks):** `pre-commit install` and `pre-commit run --all-files`. This runs trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, `ruff --fix`, `ruff-format` and detect-secrets.
- **Semgrep:** `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- **Commit lint:** `npx commitlint --from <base> --to <head>`
