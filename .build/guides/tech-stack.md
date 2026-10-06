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
  - .github/helper/install.sh
  - .github/workflows/linters.v2.yml
  - healthcare/healthcare/api/patient_portal.py
---

- **Backend:** Python 3.10 or newer (ruff targets `py310`; CI runs Python 3.14). The app is built on the **Frappe Framework** and depends on **ERPNext**; the CI installer targets the frappe/erpnext `version-16` branches. It is packaged with **flit_core**. Its own runtime dependencies are `responses` and `python-barcode`.
- **Data:** MariaDB through the Frappe ORM and `frappe.qb` (pypika query builder), with Redis for cache and queues. Doctypes are defined as JSON metadata.
- **Desk UI:** plain JavaScript form scripts using the `frappe.ui.form` / jQuery globals, bundled via `healthcare/public/js/healthcare.bundle.js`. There are also Jinja `.html` templates.
- **Patient Portal SPA:** **Vue 3** with vue-router, **frappe-ui** (^0.1.176), **Tailwind CSS 3.4** with the frappe-ui preset, built with **Vite 4.4**. It uses feather/lucide icons and a socket.io client (`socket.js`).
- **JS tooling:** Yarn workspaces (`yarn.lock`; workspaces are `patient_portal` and `frappe-ui`). ESLint 10 (flat config), Prettier 3. CI uses Node 24.
- **Quality and security tooling:** pre-commit, ruff (lint and format), ESLint, Prettier, Semgrep (Frappe rules plus `r/python.lang.correctness`), pip-audit, detect-secrets, CodeQL.
- **Release:** semantic-release with commitlint (conventional commits).
