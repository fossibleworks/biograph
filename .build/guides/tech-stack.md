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
  - yarn.lock
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - crowdin.yml
---

- **Backend:** Python 3.10+ (`requires-python >=3.10`; CI uses 3.14). It is a **Frappe Framework** app that depends on **ERPNext** and **payments**. Built with flit (`flit_core`). Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`, utf8mb4). Queries use `frappe.db.*`, `frappe.qb` and raw `frappe.db.sql`.
- **Desk UI:** plain Frappe form, list and tree scripts in JavaScript (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`), plus shared desk JS in `healthcare/public/js`, bundled through `healthcare.bundle.js`. Server-rendered Jinja templates and print formats.
- **Patient Portal:** Vue 3, vue-router 4, **frappe-ui** (^0.1.176), Vite 4.4.9, Tailwind CSS 3.4.15 with the frappe-ui preset, and feather/lucide icons. Managed as a yarn workspace (`yarn.lock`).
- **Tooling:** ruff 0.15.18 (lint and format), Prettier, ESLint 10 (flat config), pre-commit, Semgrep with the Frappe rules, pip-audit, detect-secrets, commitlint, semantic-release, CodeQL, Codecov, Mergify, and Crowdin for translations.
- **Supported Frappe lines:** version-14, version-15 and version-16. The fork tracks upstream `version-16`.
