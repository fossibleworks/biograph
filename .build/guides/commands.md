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

All runtime commands run inside a **Frappe bench**. There is no standalone dev server for the Python app.

**Install**
- `bench get-app <repo-url>`
- `bench --site <site> install-app healthcare`

**Tests** (as in CI)
- `bench --site test_site run-parallel-tests --app healthcare`
- Single module locally: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Migrate / patches:** `bench --site <site> migrate`

**Lint/format** (run from the app dir)
- `pip install pre-commit && pre-commit install && npm install`
- `pre-commit run --all-files`
- This runs ruff with `--fix`, ruff-format, prettier, eslint, detect-secrets, pip-audit, and YAML/JSON/TOML/AST checks.

**Semgrep**
- `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
- `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Patient portal**
- `yarn install`: the root `postinstall` also installs `patient_portal`
- `yarn build` (root, runs `cd patient_portal && yarn build`)
- `cd patient_portal && yarn dev` (Vite dev server)

**Translations:** `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
