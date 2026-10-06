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
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.yml
  - .github/helper/update_pot_file.sh
---

All commands assume a Frappe bench. The app installs into `~/frappe-bench/apps/healthcare`.

**Setup**
- `bench get-app https://github.com/Tacten/biograph`, then `bench --site <site> install-app healthcare`
- CI bootstrap: `bash .github/helper/install.sh`. It runs `bench init`, gets payments and erpnext on the matching branch (fork branches use `version-16`), runs `bench setup requirements --dev`, and installs the app on `test_site`.
- `bench --site <site> migrate`: runs `patches.txt` and `after_migrate`.

**Tests**
- `bench --site test_site run-parallel-tests --app healthcare` (what CI runs)
- One module: `bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment`
- `python -m compileall -f .` and a grep for `^<<<<<<< ` (CI's syntax and conflict check)

**Lint/format**
- `pip install pre-commit && pre-commit install && npm install && pre-commit run --all-files` (ruff, ruff-format, prettier, eslint, pip-audit, detect-secrets, pre-commit-hooks)
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git frappe-semgrep-rules && pip install semgrep && semgrep ci --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Frontend (patient portal)**
- `yarn install` at the root. The postinstall step installs `patient_portal`.
- `yarn build`, which runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`
- `cd patient_portal && yarn dev` (Vite dev server, proxying to Frappe)
- Desk assets: `bench build --app healthcare`

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
