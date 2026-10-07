---
title: Tech stack
category: tech-stack
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - pyproject.toml
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - healthcare/hooks.py
  - crowdin.yml
---

- **Backend:** Python ≥3.10 (CI runs 3.14), packaged with `flit_core`, built as a **Frappe framework app** that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Data lives in **MariaDB** (CI uses `mariadb:11.8`). Runtime Python dependencies: `responses`, `python-barcode`.
- **Desk UI:** plain JavaScript Frappe form scripts and jQuery (`frappe`, `erpnext`, `$` globals). They are bundled through `healthcare/public/js/healthcare.bundle.js` and wired up with `doctype_js` in hooks.
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 with the frappe-ui preset, and Vite 4. It lives in `patient_portal/`.
- **Tooling:** Node 24 in CI, yarn workspaces (root `package.json` and `yarn.lock`), ruff, prettier, ESLint 10 (flat config), pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, and semantic-release.
- **i18n:** gettext `.pot`/`.po` under `healthcare/locale`, synced through Crowdin.
