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
  - .github/workflows/linters.v2.yml
  - .github/workflows/ci.yml
  - README.md
---

Run these from a Frappe bench that has erpnext and this app installed (`bench get-app ...`, `bench --site <site> install-app healthcare`).

**Lint and format (same as CI):**
- `pre-commit install` then `pre-commit run --all-files`. This runs ruff, ruff-format, prettier, eslint, pre-commit-hooks, pip-audit and detect-secrets.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit messages: `npx commitlint --from <base> --to <head>`.

**Tests:**
- All tests: `bench --site test_site run-parallel-tests --app healthcare` (what CI runs).
- One module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`.
- CI also runs `python -m compileall -f .` and checks for merge-conflict markers.

**Frontend:**
- `yarn install` (root; postinstall installs `patient_portal`).
- `yarn build`, which runs `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev` for the Vite dev server (proxies to Frappe).

**Migrations:** `bench --site <site> migrate` runs `patches.txt`.
