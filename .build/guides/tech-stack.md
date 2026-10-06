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
  - .github/workflows/ci.yml
  - healthcare/__init__.py
  - yarn.lock
---

- **Backend:** Python (>=3.10; ruff targets py310, CI runs 3.14) on the **Frappe Framework** and **ERPNext** (version-16 line, app version `16.0.8`). Packaged with `flit_core` through `pyproject.toml`. Runtime dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`) through the Frappe ORM, `frappe.qb` (pypika query builder) and `frappe.db.sql`. Redis is used for queues and cache.
- **Desk front-end:** plain JavaScript Frappe form scripts (`<doctype>.js`, `_list.js`, `_calendar.js`) plus `healthcare/public/js/*`, bundled through `healthcare.bundle.js`. Uses jQuery and Frappe globals.
- **Patient portal:** Vue 3, vue-router 4, **frappe-ui** (with its Tailwind preset), Tailwind CSS 3.4, Vite 4.4.9, feather/lucide icons. It is a yarn workspace (`package.json` workspaces: `patient_portal`, `frappe-ui`) with `yarn.lock`.
- **Node:** 24 in CI.
- **Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, Semgrep (frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, CodeQL, Crowdin for translations.
