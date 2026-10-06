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
---

- **Backend:** Python ≥3.10 (ruff targets py310; CI runs Python 3.14). It is a **Frappe Framework** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`) and is packaged with `flit_core`. Runtime pip dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (query builder) and `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts with Frappe client APIs (`frappe.ui.form`, `frappe.call`, `__()`), bundled through `healthcare/public/js/healthcare.bundle.js`. Doctype JS and JSON live next to each controller.
- **Patient portal SPA:** Vue 3 with `<script setup>`, vue-router, **frappe-ui** (components, Tailwind preset, Vite plugin), Tailwind CSS 3.4, Vite 4.4, feather/lucide icons, and socket.io for realtime resource refetch.
- **Package management:** Yarn workspaces (`patient_portal`, `frappe-ui`), `yarn.lock` at the root, and Node 24 in CI.
- **Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, semgrep (Frappe rules), CodeQL, pip-audit, detect-secrets, commitlint, semantic-release.
