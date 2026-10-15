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
---

- **Backend:** Python ≥3.10 (CI runs 3.14), packaged with `flit_core`, running as a **Frappe** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`) and `payments`. Its own Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (pypika) and `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts (`<doctype>.js`) and bundles under `healthcare/public/js` (`healthcare.bundle.js`), using Frappe globals (`frappe`, `__`, `$`, `moment`).
- **Patient Portal SPA:** Vue 3 + vue-router 4, built with **Vite 4.4.9**, **frappe-ui** (components, Tailwind preset, Vite plugin), **Tailwind CSS 3.4.15**, PostCSS/autoprefixer and feather/lucide icons.
- **JS tooling:** Yarn workspaces (root `yarn.lock`), Node 24 in CI, ESLint 10 (flat config) and Prettier.
- **Python tooling:** ruff (lint and format), pre-commit, Semgrep (Frappe rules), pip-audit and detect-secrets.
