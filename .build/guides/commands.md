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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - .github/helper/update_pot_file.sh
---

**Setup (inside a Frappe bench):**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`

**Tests (server):**
- `bench --site test_site run-parallel-tests --app healthcare` (this is what CI runs)
- For a single doctype: `bench --site <site> run-tests --app healthcare --doctype "<DocType>"`

CI bootstraps a bench with `.github/helper/install.sh`. It clones frappe, payments and erpnext on the base branch, falling back to `version-16` for fork branches such as `biograph-fh` and `goal/*`.

**Lint / format:**
- `pre-commit install && pre-commit run --all-files` runs ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and basic hygiene hooks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit-title check: `npx commitlint --from <base> --to <head>`

**Frontend (Patient Portal):**
- `yarn install`: root postinstall also installs `patient_portal`.
- `yarn build`: runs `cd patient_portal && yarn build`, which is `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev`: Vite dev server with the Frappe proxy.
- Desk assets: `bench build --app healthcare`.

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
