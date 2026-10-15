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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - package.json
  - patient_portal/package.json
  - .github/workflows/linters.v2.yml
  - .github/helper/update_pot_file.sh
---

All app commands run from inside a Frappe bench (`~/frappe-bench`), with the app at `apps/healthcare`.

**Install and run**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`
- `bench start`
- `bench --site <site> migrate` runs the patches in `healthcare/patches.txt` and the `after_migrate` hook.

**Tests**
- In CI: `bench --site test_site run-parallel-tests --app healthcare`
- Locally: `bench --site <site> run-tests --app healthcare`. Add `--doctype "Patient Appointment"` or `--module healthcare.healthcare.doctype.<name>.test_<name>` to narrow the run.
- CI sets the bench up with `.github/helper/install.sh`.

**Lint and format** (one-time setup is `pip install pre-commit && pre-commit install && npm install`)
- `pre-commit run --all-files` runs ruff (with `--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets, and basic yaml/json/toml/ast checks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit messages: `npx commitlint --from <base> --to <head>`

**Patient portal**
- `yarn install` (root; its postinstall installs `patient_portal`)
- `yarn build` (root) runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`
- `cd patient_portal && yarn dev` starts the Vite dev server, which proxies to Frappe.

**Translations**
- `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
