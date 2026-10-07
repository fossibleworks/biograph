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
  - .github/workflows/ci.yml
  - .pre-commit-config.yaml
  - package.json
  - patient_portal/package.json
  - .github/workflows/semantic-commits.yml
---

**Install (into a Frappe bench that already has ERPNext):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Run the tests the way CI does:**
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
```
For one doctype: `bench --site <site> run-tests --app healthcare --doctype "Patient Appointment"`. Frappe test runner convention; not in CI.

**Lint and format:**
```sh
pip install pre-commit && pre-commit install
npm install   # eslint deps
pre-commit run --all-files
```
The hooks are ruff `--fix`, ruff-format, prettier, eslint, pip-audit, detect-secrets and basic file checks. Pre-commit skips a long top-level `exclude` list of legacy files. To lint those paths, run ruff on them directly, for example `ruff check <path>`.

**Semgrep (same as CI):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Commit-message check:**
```sh
npx commitlint --from <base> --to <head>
```

**Patient Portal:**
```sh
yarn install            # root postinstall also installs patient_portal
yarn build              # root → cd patient_portal && yarn build
cd patient_portal && yarn dev   # vite dev server (frappe proxy)
```

**Syntax and merge-marker check (from CI):** `python -m compileall -f .` and grep for `^<<<<<<< `.
