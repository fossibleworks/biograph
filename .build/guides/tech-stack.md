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
  - healthcare/hooks.py
  - yarn.lock
---

- **Backend:** Python ≥3.10 (CI runs 3.14) on the **Frappe framework**, with **ERPNext** as a required app. Packaged with `flit_core` (`pyproject.toml`). Runtime deps: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Queries use `frappe.qb` (query builder) and `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts per DocType, using Frappe globals (`frappe`, `erpnext`, `$`, `moment`), bundled through `healthcare/public/js/healthcare.bundle.js`.
- **Patient Portal:** Vue 3 + vue-router + **frappe-ui**, built with Vite 4 and styled with Tailwind CSS 3 (frappe-ui preset) and PostCSS. Socket via `engine.io-client`.
- **JS tooling:** Node 24 in CI. Yarn workspaces (`yarn.lock`, workspaces `patient_portal`, `frappe-ui`). ESLint 10 (flat config) and Prettier.
- **Python tooling:** ruff (lint + format), pip-audit, detect-secrets, and Frappe semgrep rules.
- **Deployment:** Frappe `bench` (`bench get-app`, `bench --site … install-app healthcare`), or Frappe Cloud.
