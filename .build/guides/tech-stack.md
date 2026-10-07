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
  - yarn.lock
---

- **Backend:** Python 3.10 or newer (`requires-python >=3.10`, ruff `target-version = py310`). CI runs Python 3.14. It is a **Frappe framework** app that depends on **ERPNext** and the `payments` app. The package is built with **flit_core**. Runtime Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB. CI uses `mariadb:11.8`.
- **Desk UI:** classic Frappe client scripts (jQuery-style `frappe.ui.form.on`, `frappe.call`). The `healthcare.bundle.js` bundle is loaded through `app_include_js`. Some doctypes get extra JS through `doctype_js` in `hooks.py`.
- **Patient Portal SPA (`patient_portal/`):** **Vue 3**, **vue-router 4**, **frappe-ui** (^0.1.176), **Vite 4.4.9**, **TailwindCSS 3.4.15** with the frappe-ui preset, PostCSS/autoprefixer, feather and lucide icons. It is an ES module package.
- **Node tooling:** the root `package.json` is a Yarn workspace (`patient_portal`, `frappe-ui`) with a `yarn.lock`. CI uses Node 24. Linting uses ESLint 10 (flat config) and Prettier.
- **Python tooling:** ruff 0.15.18 (lint and format), pre-commit, pip-audit, detect-secrets, and Frappe semgrep rules.
