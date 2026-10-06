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
  - .github/workflows/linters.yml
  - dev-requirements.txt
  - README.md
---

All commands run inside a Frappe **bench**. There is no standalone run target.

- **Install the app:** `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`.
- **Run tests (CI form):** `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`. Locally: `bench --site <site> run-tests --app healthcare [--doctype "Patient Appointment"]`. The site needs `allow_tests`; see `.github/helper/site_config.json`.
- **Migrate after schema or patch changes:** `bench --site <site> migrate`.
- **Lint/format:** `pre-commit run --all-files`. This runs ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks. Install the hooks with `pip install -r dev-requirements.txt && pre-commit install`.
- **Semgrep (as CI):** `semgrep ci --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness`, after cloning `frappe/semgrep-rules`.
- **Portal frontend:**
  - Root `yarn install` (its postinstall installs `patient_portal`).
  - `yarn build` runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
  - `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.
- **Translations POT:** `.github/helper/update_pot_file.sh`, run weekly in CI.
