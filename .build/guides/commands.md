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
  - .pre-commit-config.yaml
  - README.md
  - .github/workflows/ci.yml
  - .github/workflows/semantic-commits.yml
---

**Setup (bench):**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`

**Portal frontend:**
- `yarn install`: the root postinstall also installs `patient_portal`.
- `yarn build` (root) or `cd patient_portal && yarn build`: runs `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev`: Vite dev server proxied to Frappe.

**Lint / format:**
- `pre-commit install && pre-commit run --all-files`: runs trailing-whitespace, yaml/json/toml/ast checks, prettier, eslint, pip-audit, `ruff --fix`, `ruff-format` and detect-secrets.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Tests (inside a bench):**
- `bench --site test_site run-parallel-tests --app healthcare` (this is what CI runs)
- `bench --site <site> run-tests --app healthcare --doctype "<DocType>"`

**Commit check:** `npx commitlint --from <base> --to <head>`
