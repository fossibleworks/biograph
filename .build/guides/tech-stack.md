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
  - healthcare/hooks.py
  - yarn.lock
  - crowdin.yml
---

- **Backend:** Python ≥3.10 (CI runs 3.14) as a **Frappe framework app** that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaged with `flit_core`. Runtime extras: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Queries go through the Frappe ORM, `frappe.qb` (pypika query builder), and some raw `frappe.db.sql`.
- **Desk UI:** plain JavaScript Frappe form scripts (`<doctype>.js`, `_list.js`, `_calendar.js`) plus shared bundles in `healthcare/public/js` (`healthcare.bundle.js`). They use Frappe globals such as `frappe`, `erpnext`, jQuery and moment.
- **Patient Portal SPA:** **Vue 3** + vue-router, **frappe-ui**, **Tailwind CSS 3.4** with the frappe-ui preset, built by **Vite 4**. It uses yarn workspaces (`yarn.lock`), and Node 24 in CI.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, Codecov, CodeQL, Crowdin (translations).
