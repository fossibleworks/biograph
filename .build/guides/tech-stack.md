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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - crowdin.yml
---

- **Backend:** Python ≥3.10 (CI runs 3.14). It is a **Frappe framework app** that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaging uses `flit_core` through `pyproject.toml`, and the version lives in `healthcare/__init__.py`. Runtime Python deps: `responses`, `python-barcode`.
- **Database:** MariaDB. CI uses `mariadb:11.8`, accessed through the Frappe ORM (`frappe.db`, `frappe.get_doc`).
- **Desk UI:** Frappe Desk form scripts in plain JavaScript (`<doctype>.js`, `_list.js`, `_tree.js`, `_calendar.js`), plus a bundle at `healthcare/public/js/healthcare.bundle.js` that loads through `app_include_js`.
- **Patient portal:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 (frappe-ui preset), feather/lucide icons, built with Vite 4.4.9. Yarn workspaces are used (`yarn.lock`).
- **Tooling:** Node 24 in CI, ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), CodeQL, detect-secrets, pip-audit.
- **Release tooling:** semantic-release and commitlint (conventional commits).
- **i18n:** gettext `.pot` at `healthcare/locale/main.pot`, synced through Crowdin.
