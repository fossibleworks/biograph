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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - package.json
  - patient_portal/package.json
  - .github/helper/update_pot_file.sh
---

Everything runs inside a Frappe bench that has ERPNext installed. The app lives at `apps/healthcare`.

**Install**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Server tests (same as CI)**
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module locally:
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```

**Lint and format (pre-commit)**
```sh
pip install pre-commit
pre-commit install
npm install
pre-commit run --all-files
```
The pre-commit hooks are: ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks.

**Semgrep (Frappe rules)**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal**
- From the repo root: `yarn install` (its postinstall step installs `patient_portal`), then `yarn build`.
- Inside `patient_portal/`: `yarn dev` (Vite dev server) or `yarn build` (`vite build --base=/assets/healthcare/patient_portal/`).

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.

**CI sanity checks you can run locally:** `python -m compileall -f .` and a grep for leftover `<<<<<<<` conflict markers.
