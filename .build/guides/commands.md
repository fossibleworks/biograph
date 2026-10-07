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
  - README.md
  - .pre-commit-config.yaml
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - .github/helper/install.sh
---

**Setup (inside a Frappe bench):**
- `bench get-app <repo>` and then `bench --site <site> install-app healthcare`
- `yarn install` at the repo root. Its `postinstall` runs `cd patient_portal && yarn install --check-files`.

**Build:**
- `yarn build` (root) runs `cd patient_portal && yarn build`, which is `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server with the Frappe proxy.

**Lint / format:**
- `pip install pre-commit && pre-commit install && pre-commit run --all-files` runs trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, `ruff --fix`, `ruff-format`, and detect-secrets.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Test:**
- `bench --site test_site run-tests --app healthcare` for local runs. Add `--module`/`--doctype` to narrow the run.
- CI runs `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`.

**Migrations / i18n:**
- `bench --site <site> migrate` applies `healthcare/patches.txt`.
- `.github/helper/update_pot_file.sh` regenerates `healthcare/locale/main.pot`.
