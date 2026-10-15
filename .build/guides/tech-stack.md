---
title: Tech Stack
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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - .github/helper/install.sh
---

# Tech stack

## Backend (most of the code)
- **Python >= 3.10**. Ruff targets `py310`, and CI runs Python 3.14.
- **Frappe framework** app named `healthcare`, with **ERPNext** as a required app (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app.
- Packaging: `flit_core` (`pyproject.toml`). The version is set in `healthcare/__init__.py`.
- Extra Python dependencies: `responses`, `python-barcode`.
- Database: **MariaDB**. CI uses `mariadb:11.8` with utf8mb4. Redis is installed by the bench setup.
- Data model: Frappe **DocTypes**. Each one is a JSON schema plus a Python controller plus a JS form script. Database access uses the `frappe.qb` query builder, `frappe.db.*` and some raw `frappe.db.sql`.

## Desk frontend
- Plain JavaScript Frappe form, list and calendar scripts kept next to each DocType.
- Shared desk JS in `healthcare/public/js`, bundled through `healthcare.bundle.js` (`app_include_js`).
- Uses the jQuery and Frappe globals declared in `eslint.config.mjs`.

## Patient Portal SPA (`patient_portal/`)
- **Vue 3** with `vue-router`, **frappe-ui** (^0.1.176), **Vite 4.4.9**, **Tailwind CSS 3.4.15** using the frappe-ui preset, PostCSS/autoprefixer and feather or lucide icons.
- The build writes to `healthcare/public/patient_portal/assets` and to the Jinja page `healthcare/www/patient_portal.html`.

## Tooling
- Yarn workspaces (root `package.json` plus `yarn.lock`).
- pre-commit with ruff, ruff-format, prettier, eslint 10, pip-audit and detect-secrets.
- Semgrep using the Frappe rules.
- commitlint, semantic-release, Mergify, Crowdin and Codecov.
