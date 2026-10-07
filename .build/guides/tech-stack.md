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
  - .github/workflows/ci.yml
  - healthcare/hooks.py
  - crowdin.yml
---

- **Backend:** Python ≥3.10 (CI runs 3.14) on the **Frappe Framework** with **ERPNext** as a required app. The package is built with `flit_core`. Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (PyPika query builder) and some raw `frappe.db.sql`.
- **Desk UI:** Frappe Desk form scripts in plain JavaScript (`<doctype>.js`, `_list.js`, `_calendar.js`), bundled from `healthcare/public/js/healthcare.bundle.js`. Desk pages and forms are driven by doctype JSON metadata.
- **Patient Portal SPA:** Vue 3 (`<script setup>`), vue-router, **frappe-ui**, Tailwind CSS 3.4 (with the frappe-ui preset) and Vite 4. It lives in `patient_portal/` and uses Yarn workspaces.
- **Node:** 24 in CI. Yarn is the package manager (`yarn.lock`).
- **Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, Semgrep with the Frappe rules, detect-secrets, pip-audit, CodeQL, commitlint and semantic-release.
- **i18n:** a gettext POT/PO file at `healthcare/locale/main.pot`, synced through Crowdin.
