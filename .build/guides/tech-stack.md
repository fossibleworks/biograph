---
title: Tech Stack
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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - .releaserc
---

# Tech stack

## Backend
- **Python ≥ 3.10**: ruff targets `py310` and CI runs Python 3.14. Packaged with `flit_core`.
- **Frappe Framework** (metadata-driven: DocType JSON + Python controller + JS form script) with **ERPNext** as a required app (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app.
- **MariaDB** (CI uses `mariadb:11.8`). Queries go through `frappe.qb` (PyPika query builder), `frappe.get_all` and `frappe.db.*`. Some legacy code uses raw `frappe.db.sql`.
- Supported Frappe/ERPNext release lines: **v14, v15, v16** (`version-NN` branches).
- Extra Python deps: `responses`, `python-barcode`.

## Desk frontend
- Plain JavaScript Frappe form scripts (`frappe.ui.form.on(...)`), jQuery, and the bundle `healthcare/public/js/healthcare.bundle.js` loaded through `app_include_js`.
- Jinja is used for print formats and for `www/` pages.

## Patient portal SPA (`patient_portal/`)
- **Vue 3** and **vue-router 4**, built with **Vite 4.4.9** and `@vitejs/plugin-vue`.
- **frappe-ui** (component library and Tailwind preset), **Tailwind CSS 3.4.15**, PostCSS/autoprefixer, feather/lucide icons.
- Uses a Socket.io client (`src/socket.js`) for realtime updates.
- Node 24 in CI. **Yarn** workspaces (`yarn.lock`).

## Tooling
- ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, Mergify, Codecov, CodeQL, Crowdin.
