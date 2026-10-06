---
title: Tech stack
category: tech-stack
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - pyproject.toml
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - healthcare/hooks.py
---

- **Backend:** Python 3.10 or newer (`requires-python`; ruff targets py310; CI runs Python 3.14). It is a **Frappe Framework** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`) and the `payments` app. It is packaged with `flit_core` from `pyproject.toml`, and the version lives in `healthcare/__init__.py`.
- **Database:** MariaDB, version 11.8 in CI. Code uses the Frappe ORM, `frappe.qb` (PyPika query builder) and some raw `frappe.db.sql`.
- **Desk UI:** plain JavaScript with Frappe client APIs (`frappe.ui.form.on`, `frappe.call`, `__()` for translations). These files are bundled through `healthcare/public/js/healthcare.bundle.js`.
- **Patient portal:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 (with the frappe-ui preset) and Vite 4. It is a Yarn workspace (`patient_portal`) and uses feather/lucide icons.
- **Tooling:** Node 24 in CI. Yarn workspaces (`yarn.lock`), ESLint 10 (flat config), Prettier, Ruff, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, commitlint and semantic-release.
- **Python deps beyond Frappe/ERPNext:** `responses`, `python-barcode`.
- **Supported Frappe/ERPNext lines:** version-14, 15 and 16. The fork tests against version-16.
