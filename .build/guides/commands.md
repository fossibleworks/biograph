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
  - .pre-commit-config.yaml
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
---

All commands run inside a Frappe bench (`frappe-bench/apps/healthcare`).

**Install**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- `bench --site <site> migrate` runs the patches in `healthcare/patches.txt` and `after_migrate`.

**Lint / format** (the same checks CI runs)
- `pip install pre-commit && pre-commit install && npm install`
- `pre-commit run --all-files` runs trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, `ruff --fix`, `ruff-format` and detect-secrets.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Tests**
- `bench --site test_site run-tests --app healthcare` (optionally `--doctype "Patient Appointment"`)
- CI runs `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`.

**Frontend (patient portal)**
- `yarn install` at the root (postinstall installs `patient_portal`)
- `yarn build` at the root, or `cd patient_portal && yarn build`, runs `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.
- Desk JS is built by `bench build --app healthcare`.
