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
---

**Backend**
- Python >= 3.10 (`requires-python`; ruff targets `py310`). CI runs Python 3.14.
- **Frappe Framework** with **ERPNext** (required app) and the `payments` app. CI and fork branches test against Frappe/ERPNext `version-16`.
- MariaDB 11.8 in CI and Redis, run through **bench**.
- Packaged with `flit_core`. Runtime extras: `responses`, `python-barcode`.
- Queries use the Frappe ORM (`frappe.db.get_all`, `frappe.get_doc`) and the **frappe.qb** query builder (PyPika).

**Desk frontend**
- Plain JavaScript Frappe form scripts (`frappe.ui.form.on`), jQuery and Jinja HTML templates.
- Bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).

**Patient Portal SPA** (`patient_portal/`)
- Vue 3, vue-router 4, **frappe-ui** (^0.1.176) and feather/lucide icons.
- Vite 4.4.9, TailwindCSS 3.4.15 (frappe-ui preset), PostCSS and autoprefixer.
- Yarn workspaces (`yarn.lock`) at the root, with the workspace `patient_portal`.

**Tooling**
- ruff (lint and format), ESLint 10 (flat config), Prettier (mirrors-prettier v3.1.0) and pre-commit.
- Semgrep (Frappe rules), detect-secrets, pip-audit and CodeQL.
- commitlint (conventional commits), semantic-release, Crowdin (translations) and Codecov.
