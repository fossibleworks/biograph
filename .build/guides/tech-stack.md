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
  - .github/helper/install.sh
  - healthcare/hooks.py
  - yarn.lock
---

# Tech stack

## Backend
- **Python ≥ 3.10.** Ruff targets `py310`, and CI runs Python 3.14.
- **Frappe Framework** with **ERPNext** (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app.
- The package is built with `flit_core`. Runtime deps are pinned in `pyproject.toml` (`responses`, `python-barcode`).
- **MariaDB** is the database. CI uses `mariadb:11.8` with a utf8mb4 charset.
- Server code uses Frappe idioms: DocType controllers (`Document` subclasses), `frappe.qb` (pypika query builder), `frappe.db.*`, `@frappe.whitelist()` APIs, doc_events and scheduler hooks, and `frappe.enqueue` for background jobs.
- CI tests against the Frappe/ERPNext `version-16` branch. Fork branches fall back to `version-16`.

## Desk UI
- Plain JavaScript form scripts (`frappe.ui.form.on(...)`), `*_list.js` and `*_tree.js` files, and a `healthcare.bundle.js` included through `app_include_js`. jQuery and Frappe globals are used.
- Jinja HTML templates for print formats and widgets (for example `healthcare/public/js/*.html`).

## Patient Portal SPA
- **Vue 3** with `vue-router`.
- **frappe-ui** for components, the Tailwind preset and the Vite plugin.
- **Vite 4.4.9** and **Tailwind CSS 3.4.15**, with PostCSS and autoprefixer.
- Yarn workspaces (`patient_portal`, `frappe-ui`). The lockfile is the root `yarn.lock`.

## Tooling
- Linting and formatting: ruff (lint and format), ESLint 10 (flat config), and Prettier for JS/TS/Vue/CSS.
- Checks: pre-commit, Semgrep with Frappe rules, pip-audit, and detect-secrets.
- Commits: commitlint (conventional commits). Releases: semantic-release.
- Translations: Crowdin, through `healthcare/locale/main.pot`.
