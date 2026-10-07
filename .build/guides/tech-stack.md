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
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

**Backend**
- Python **>=3.10**. Ruff targets py310, and CI runs on Python **3.14**.
- The app is a **Frappe** app on top of **ERPNext**, plus the `payments` app.
- Packaging uses **flit_core**. The version is dynamic and read from `healthcare/__init__.py`.
- Runtime dependencies: `responses`, `python-barcode`.
- Database: **MariaDB**. CI uses `mariadb:11.8` with utf8mb4.
- Redis, through Frappe.
- `wkhtmltopdf` for PDF print formats.

**Desk UI**
- Plain Frappe desk JavaScript: form scripts per doctype, plus `healthcare/public/js/*.js` bundled through `healthcare.bundle.js`.
- Jinja templates and HTML for print formats and web pages.

**Patient Portal SPA** (`patient_portal/`)
- **Vue 3** with `vue-router`
- **frappe-ui** (`^0.1.176`) as the component library
- **Tailwind CSS 3.4** using the frappe-ui preset
- **Vite 4.4.9** with the `frappe-ui/vite` plugin
- `feather-icons` and Lucide icons
- socket.io for realtime

**Package management**
- **Yarn** workspaces (`patient_portal`, `frappe-ui`) with a committed `yarn.lock`.
- Node 24 in CI.

**Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release.
