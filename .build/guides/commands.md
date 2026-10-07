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
  - README.md
  - .github/helper/update_pot_file.sh
---

The app runs inside a **Frappe bench**. It is not runnable on its own.

**Install and setup**
- `bench get-app <repo-url>`, then `bench --site <site> install-app healthcare`
- `bench --site <site> migrate` runs the patches in `healthcare/patches.txt` and `after_migrate`.

**Tests**, as CI runs them:
- `bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1`
- For a single module locally: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint and format**
- `pre-commit install` and `pre-commit run --all-files` run ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and the YAML/JSON/TOML/AST checks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules` and then `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Frontend**
- At the root, `yarn install`. Its postinstall step installs `patient_portal`.
- `yarn build` runs `cd patient_portal && yarn build`, which is `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` runs the Vite dev server.
- Desk assets: `bench build --app healthcare`.

**Translations**
- `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. A scheduled workflow runs it.
