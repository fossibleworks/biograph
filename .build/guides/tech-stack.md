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
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
  - crowdin.yml
---

**Backend**
- Python 3.10 or newer (pyproject `requires-python`; ruff target py310). CI runs Python 3.14.
- Frappe Framework plus ERPNext (`required_apps = ["frappe/erpnext"]`). The `payments` app is installed in CI.
- Database: MariaDB. CI uses `mariadb:11.8` with utf8mb4. Redis is also used.
- Packaging uses `flit_core`. Runtime Python dependencies are `responses` and `python-barcode`.
- Queries are written with `frappe.qb` (pypika query builder), `frappe.get_all` / `frappe.db.*`, and some raw `frappe.db.sql`.

**Desk frontend**
- Plain JavaScript form scripts per DocType (`<doctype>.js`, `<doctype>_list.js`, `_tree.js`, `_calendar.js`).
- Shared scripts in `healthcare/public/js`, bundled as `healthcare.bundle.js`.
- These scripts use the Frappe globals `frappe`, `__`, `$` and `moment`.

**Patient portal** (`patient_portal/`)
- Vue 3 and vue-router 4, Vite 4.4.9 with `frappe-ui/vite`.
- Tailwind 3.4.15 with the frappe-ui preset, plus feather/lucide icons.
- Yarn workspaces are set up in the root `package.json`, with `yarn.lock` at the root.

**Tooling**
- ruff for linting and formatting, prettier, ESLint 10 flat config, pre-commit.
- Semgrep with the Frappe rules, CodeQL, pip-audit, detect-secrets.
- commitlint (conventional commits), semantic-release, Mergify, Crowdin for translations, Codecov.
