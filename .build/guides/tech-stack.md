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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

**Backend**
- **Python ≥ 3.10** (ruff targets `py310`; CI runs Python 3.14), packaged with `flit_core`
- **Frappe Framework**: a metadata-driven full-stack framework (DocTypes, whitelisted APIs, query builder `frappe.qb`)
- **ERPNext**, a hard dependency (`required_apps = ["frappe/erpnext"]`), plus the `payments` app in CI
- **MariaDB** (CI uses `mariadb:11.8`), Redis
- Runtime Python deps: `responses`, `python-barcode`
- Managed with **bench** (`bench get-app`, `bench install-app`, `bench run-parallel-tests`)

**Desk frontend**
- Plain JavaScript Frappe form scripts (`<doctype>.js`, `_list.js`, `_tree.js`), shared code in `healthcare/public/js`, bundled through `healthcare.bundle.js`. Uses jQuery and Frappe globals.

**Patient Portal frontend** (`patient_portal/`)
- **Vue 3** + **vue-router 4**, **frappe-ui** (^0.1.176), **Vite 4.4.9**, **Tailwind CSS 3.4.15** with the frappe-ui preset, PostCSS/autoprefixer, feather/lucide icons, socket.io client
- Yarn workspaces (`yarn.lock` at root)

**Tooling:** Node 24 in CI, ESLint 10 (flat config), Prettier, Ruff (lint + format), pre-commit, Semgrep (Frappe rules), CodeQL, detect-secrets, pip-audit, commitlint, semantic-release.
