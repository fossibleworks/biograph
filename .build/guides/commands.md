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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - README.md
  - .github/helper/update_pot_file.sh
---

# Commands

This app runs inside a Frappe bench; it has no standalone run command.

## Install / run
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- `bench start`; `bench --site <site> migrate`, which runs `patches.txt` and then `after_migrate`

## Tests (server)
- CI: `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`
- Locally: `bench --site <site> run-tests --app healthcare [--module healthcare.healthcare.doctype.<dt>.test_<dt>]`
- CI environment setup is scripted in `.github/helper/install.sh`.

## Lint / format
- `pre-commit install`, then `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and the basic hygiene hooks.
- Install the eslint deps first with `npm install`, or as CI does, `npm install -D eslint@10.5.0 @eslint/js@10.0.1 @eslint/eslintrc@3.3.5 globals@17.4.0`.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

## Frontend (patient portal)
- From the root, `yarn install`; its postinstall installs `patient_portal`.
- `yarn build` runs `cd patient_portal && yarn build`, which is `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.

## Translations
- `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. A weekly workflow runs it.
