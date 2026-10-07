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
---

**Install (bench):**
- `bench get-app https://github.com/Tacten/biograph`
- `bench --site <site> install-app healthcare`

**Server tests (as in CI):**
- `bench --site test_site run-parallel-tests --app healthcare`
- For one module: `bench --site <site> run-tests --app healthcare --module <dotted.module>`

**Lint and format:**
- `pip install pre-commit && pre-commit install && npm install`
- `pre-commit run --all-files`. This runs ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets, and the yaml/json/toml/ast checks.

**Semgrep:**
- `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
- `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`

**Patient portal:**
- `yarn install` (postinstall installs `patient_portal`)
- `yarn build`, which runs `vite build --base=/assets/healthcare/patient_portal/`
- Dev server: `cd patient_portal && yarn dev`

**CI sanity checks:**
- `python -m compileall -f .`
- A grep for leftover `<<<<<<<` merge-conflict markers
