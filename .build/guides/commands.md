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
  - .github/workflows/ci.yml
  - .github/workflows/linters.v2.yml
  - README.md
---

All commands run inside a Frappe bench with this app at `apps/healthcare`.

**Install:**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Run server tests** (same as CI):
```sh
bench --site test_site run-parallel-tests --app healthcare
```
To run one module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`.

**Lint and format:**
```sh
pip install pre-commit && pre-commit install
npm install
pre-commit run --all-files
```
The pre-commit hooks are trailing-whitespace/yaml/json/toml/ast checks, prettier, eslint, pip-audit, `ruff --fix`, `ruff-format`, and detect-secrets.

**Semgrep** (same as CI):
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient Portal:**
- `yarn install` at the repo root. The postinstall step also installs `patient_portal`.
- `yarn build` runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` starts the Vite dev server.

**Migrate after adding patches or changing schema:** `bench --site <site> migrate`.
