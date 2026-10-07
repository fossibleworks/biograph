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
  - .github/workflows/linters.v2.yml
  - .pre-commit-config.yaml
  - .github/helper/update_pot_file.sh
---

**Setup (bench):**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`

**Tests:**
- All tests (as CI runs them): `bench --site test_site run-parallel-tests --app healthcare`
- Single module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint and format:**
- `pre-commit install` then `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and basic hygiene hooks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Frontend (patient portal):**
- `yarn install` at the root. The postinstall step installs `patient_portal`.
- `yarn build` at the root (runs `vite build --base=/assets/healthcare/patient_portal/`).
- `cd patient_portal && yarn dev` for the Vite dev server with the Frappe proxy.

**Migrations:** `bench --site <site> migrate` runs `healthcare/patches.txt`.

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. It runs weekly in CI.
