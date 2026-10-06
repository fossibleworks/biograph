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
  - .github/helper/install.sh
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - README.md
---

The app runs inside a **Frappe bench**. CI reproduces that setup with `.github/helper/install.sh`.

**Install / run**
- `bench get-app <repo-url>` then `bench --site <site> install-app healthcare`
- `bench start` starts the dev server. `bench --site <site> migrate` runs patches and schema sync.

**Tests** (server, needs a bench site):
- `bench --site test_site run-parallel-tests --app healthcare` (what CI runs)
- Single module: `bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.<name>.test_<name>`

**Lint / format** (the same hooks CI runs):
- `pre-commit run --all-files`. This runs ruff (`--fix`), ruff-format, prettier (desk JS), eslint, pip-audit, detect-secrets and the standard hygiene hooks.
- Semgrep, as CI runs it: `semgrep ci --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness`
- Commit messages: `npx commitlint --from <base> --to <head>`

**Frontend (Patient Portal)**
- `yarn install`. The root postinstall installs `patient_portal` too.
- `yarn build` (root) is the same as `cd patient_portal && vite build --base=/assets/healthcare/patient_portal/`
- `cd patient_portal && yarn dev` starts the Vite dev server with a Frappe proxy.

**Sanity checks CI runs:** `python -m compileall -f .` and a grep for leftover `<<<<<<< ` conflict markers.
