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
  - patient_portal/tailwind.config.js
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - healthcare/__init__.py
  - yarn.lock
---

## Backend

- **Python ≥3.10**. Ruff targets `py310`; CI runs Python 3.14.
- **Frappe framework** app named `healthcare`. It requires **ERPNext** (`required_apps = ["frappe/erpnext"]`) and is built against Frappe/ERPNext `version-16`.
- Packaging uses `flit_core` with a dynamic version from `healthcare/__init__.py` (currently `16.0.8`).
- Extra Python dependencies: `responses`, `python-barcode`.
- Database: **MariaDB** (CI uses `mariadb:11.8`) and Redis, via `bench`.

## Desk frontend

- Plain Frappe Desk JavaScript: doctype `.js` controllers, `*_list.js`, `*_tree.js`, `*_calendar.js`, and `healthcare/public/js/*`.
- Bundled through `app_include_js = "healthcare.bundle.js"`.
- Uses the jQuery/frappe globals declared in `eslint.config.mjs`.

## Patient portal

- `patient_portal/` is a **Vue 3** SPA built with **Vite 4.4.9**, **frappe-ui** (^0.1.176), **Tailwind CSS 3.4.15** with the frappe-ui preset, `vue-router` and `feather-icons`.
- Socket.io client is set up in `src/socket.js`.

## Tooling

- Yarn workspaces (`yarn.lock`)
- Node 24 in CI
- pre-commit with ruff, prettier, eslint 10, pip-audit and detect-secrets
- Semgrep (frappe rules), CodeQL, commitlint, semantic-release
- Crowdin for translations
