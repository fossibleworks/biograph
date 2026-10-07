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
  - README.md
  - .pre-commit-config.yaml
  - .github/workflows/ci.yml
  - .github/workflows/semantic-commits.yml
---

There is no Makefile. Commands come from `package.json`, the README and CI.

**Install (inside a bench):**
- `bench get-app <repo-url>`
- `bench --site <site> install-app healthcare`

**Frontend (Patient Portal):**
- `yarn install`: installs the workspace. The root postinstall also runs `cd patient_portal && yarn install --check-files`.
- `yarn build` at the root, or `cd patient_portal && yarn build`. This runs `vite build --base=/assets/healthcare/patient_portal/`.
- `cd patient_portal && yarn dev`: Vite dev server proxied to Frappe.

**Lint and format:**
- `pip install pre-commit && pre-commit install && npm install && pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, Prettier, ESLint, pip-audit, detect-secrets and the basic file checks.
- Semgrep:
  - `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules`
  - `semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit titles: `npx commitlint --from <base> --to <head>`

**Tests:**
- `bench --site test_site run-parallel-tests --app healthcare` (what CI runs)
- For one module: `bench --site <site> run-tests --app healthcare --module <dotted.module>` (standard Frappe)

**Sanity check (CI):** `python -m compileall -f .`, plus a grep for leftover `<<<<<<<` conflict markers.
