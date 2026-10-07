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
  - eslint.config.mjs
---

**Backend**
- **Python ≥ 3.10** (ruff targets `py310`; CI runs Python **3.14**). The package is built with `flit_core`.
- **Frappe Framework** app named `healthcare`, with **ERPNext** as a required app (`required_apps = ["frappe/erpnext"]`). This is a metadata-driven DocType model: each DocType has a JSON schema plus a `.py` controller and a `.js` form script.
- **MariaDB** (CI uses `mariadb:11.8`) through the Frappe ORM (`frappe.get_doc`, `frappe.db.*`, `frappe.qb`), with some raw `frappe.db.sql`.
- Extra Python deps: `responses`, `python-barcode`.

**Desk frontend**
- Plain JavaScript Frappe form scripts under `healthcare/healthcare/doctype/*/*.js` and `healthcare/public/js/`, bundled via `healthcare.bundle.js` (`app_include_js`). These use Frappe globals: `frappe`, `__`, jQuery `$`, `moment`.

**Patient Portal SPA** (`patient_portal/`)
- **Vue 3** with `vue-router` 4
- **frappe-ui** (^0.1.176) for components, resources, and its Tailwind preset
- **Vite 4.4.9** with `@vitejs/plugin-vue` and the `frappe-ui/vite` plugin
- **Tailwind CSS 3.4.15**, PostCSS, autoprefixer
- feather-icons / lucide icons; socket.io for realtime

**Tooling**
- Yarn workspaces (`yarn.lock`, workspaces `patient_portal` and `frappe-ui`). Node 24 in CI.
- ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, CodeQL
- commitlint (conventional commits) and semantic-release
