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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

- **Backend:** Python (>=3.10, ruff targets py310; CI runs Python 3.14). The app is a **Frappe** app and needs **ERPNext** (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app. Packaging uses `flit_core`. Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.db.*` and `frappe.qb`. Redis is used for Frappe queues and cache.
- **Desk UI:** classic Frappe desk JavaScript (form scripts `<doctype>.js`, list views, `healthcare.bundle.js`) with jQuery/Frappe globals.
- **Patient Portal SPA:** Vue 3 + vue-router, **frappe-ui**, Tailwind CSS 3.4 (frappe-ui preset), built with Vite 4 (`frappe-ui/vite` plugin). Uses Yarn workspaces (`yarn.lock`).
- **Tooling:** ruff (lint and format), Prettier, ESLint 10 (flat config), pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release, and Crowdin for translations.
- **Node:** CI uses Node 24.
