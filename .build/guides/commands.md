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
  - .github/workflows/ci.yml
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
  - .github/helper/install.sh
---

**Setup (bench):**
- `bench get-app <repo>` then `bench --site <site> install-app healthcare`
- JS deps: `yarn install`. The root `postinstall` also runs `cd patient_portal && yarn install --check-files`.

**Build:**
- `yarn build` at the root runs `cd patient_portal && yarn build` (`vite build --base=/assets/healthcare/patient_portal/`).
- Portal dev server: `cd patient_portal && yarn dev`.
- Desk assets are built through bench (`bench build --app healthcare`).

**Test:**
- `bench --site <site> run-tests --app healthcare` (optionally with `--doctype` or `--module`).
- CI uses `bench --site test_site run-parallel-tests --app healthcare --total-builds N --build-number K`.

**Lint/format:**
- One-time setup: `pip install pre-commit && pre-commit install && npm install`.
- Run: `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier, eslint, pip-audit, detect-secrets and the standard hygiene hooks.
- Semgrep: `git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules && semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness`.
- Commit titles: `npx commitlint --from <base> --to <head>`.

**Migrations:** `bench --site <site> migrate` runs `patches.txt` and the `after_migrate` hook.
