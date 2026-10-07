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
  - healthcare/hooks.py
  - yarn.lock
  - .pre-commit-config.yaml
---

**Backend**
- Python >= 3.10 (ruff target `py310`). CI linting runs on Python 3.14.
- **Frappe Framework**, a metadata-driven full-stack framework. **ERPNext** is a required app (`required_apps = ["frappe/erpnext"]`).
- Packaged with `flit_core` (`pyproject.toml`). The version string lives in `healthcare/__init__.py`.
- Extra Python dependencies: `responses`, `python-barcode`.
- MariaDB/SQL through the Frappe ORM (`frappe.db`, `frappe.get_all`, `frappe.qb`).

**Desk frontend**
- Frappe desk JavaScript: doctype form scripts (`<doctype>.js`) and shared scripts in `healthcare/public/js`, bundled through `healthcare.bundle.js`.

**Patient Portal frontend** (`patient_portal/`)
- Vue 3 and vue-router 4, built with Vite 4.
- **frappe-ui** components, Tailwind CSS 3.4 (with the frappe-ui preset), PostCSS and autoprefixer, feather and lucide icons.
- Yarn workspaces. The root `package.json` declares the `patient_portal` and `frappe-ui` workspaces.

**Tooling**
- ruff for linting and formatting, Prettier, ESLint 10 (flat config), pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets.
- commitlint (conventional commits), semantic-release, Crowdin for translations, Codecov.
