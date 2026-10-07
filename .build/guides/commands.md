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
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
  - .github/helper/update_pot_file.sh
---

**Setup (bench):**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- CI install script: `bash .github/helper/install.sh`

**Tests:**
- `bench --site test_site run-parallel-tests --app healthcare` (what CI runs)
- Single module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint/format:**
- `pre-commit install` then `pre-commit run --all-files` (ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks)
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Sanity checks from CI: `python -m compileall -f .` and a grep for merge-conflict markers

**Frontend (patient portal):**
- Root: `yarn install` (postinstall installs `patient_portal`), `yarn build`
- `cd patient_portal && yarn dev` (Vite dev server) / `yarn build` (`vite build --base=/assets/healthcare/patient_portal/`)

**Translations:** `bash .github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
