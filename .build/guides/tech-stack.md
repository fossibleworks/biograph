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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - crowdin.yml
  - yarn.lock
---

**Backend**
- **Python ≥3.10** (ruff targets `py310`; CI runs Python 3.14), packaged with `flit_core` from `pyproject.toml`.
- **Frappe Framework** (metadata-driven doctypes, `frappe.qb` query builder, whitelisted RPC methods) plus **ERPNext** as a required app. The app is installed into a `bench` (`bench get-app`, `bench --site <site> install-app healthcare`).
- Database: **MariaDB** (CI uses `mariadb:11.8`).
- Extra Python dependencies: `responses`, `python-barcode`.

**Desk frontend**
- Plain Frappe Desk JavaScript: per-doctype `*.js` form scripts, `*_list.js`, `*_tree.js`, and `healthcare/public/js/*.js`, bundled as `healthcare.bundle.js`. Uses the jQuery and `frappe` globals.

**Patient Portal SPA** (`patient_portal/`)
- **Vue 3** + **vue-router 4**, **frappe-ui** (components, Tailwind preset, Vite plugin), **Tailwind CSS 3.4**, **Vite 4.4**, feather/lucide icons, socket.io client (`socket.js`).
- Yarn workspaces (`yarn.lock`, root `package.json` workspaces `patient_portal`, `frappe-ui`).

**Tooling**
- ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, detect-secrets, pip-audit, Frappe semgrep rules, commitlint, semantic-release, CodeQL.
- Node 24 in CI.
- i18n: gettext `healthcare/locale/main.pot`, synced through Crowdin.
