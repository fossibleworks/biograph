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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/helper/update_pot_file.sh
---

All app commands run from a Frappe bench that has erpnext, payments and healthcare installed.

**Setup**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`
- `bench --site <site> migrate` runs the patches in `patches.txt`.

**Tests**
- `bench --site test_site run-tests --app healthcare` runs the server tests.
- Add `--module healthcare.healthcare.doctype.<name>.test_<name>` to run a single module.
- CI runs `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`.
- Test sites need `allow_tests`; see `.github/helper/site_config.json`.

**Lint and format**
- `pre-commit install`, then `pre-commit run --all-files`. This runs:
  - ruff (with `--fix`) and ruff-format;
  - prettier on JS, Vue and CSS, and eslint `--quiet`;
  - pip-audit, detect-secrets with `.secrets.baseline`;
  - YAML, JSON and TOML checks, AST checks and debug-statement checks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Patient Portal**
- `yarn install` at the repo root. Its postinstall installs `patient_portal`.
- `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.
- `yarn build` at the root runs `vite build --base=/assets/healthcare/patient_portal/`.
- For desk assets, use `bench build --app healthcare`.

**Translations**
- `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`. It runs weekly in CI.
