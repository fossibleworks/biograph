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
  - yarn.lock
---

- **Backend:** Python ≥3.10 (ruff targets py310; CI runs Python 3.14). It is a **Frappe Framework** app that depends on **ERPNext** and **payments**, and is tested against the `version-16` branches. The package is built with `flit_core`. Runtime pip dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB through the Frappe ORM (`frappe.db`, `frappe.qb` query builder, some raw `frappe.db.sql`). Redis is used for queues and cache.
- **Desk UI:** plain JavaScript form scripts for each doctype (`<doctype>.js`, `<doctype>_list.js`) that use the Frappe client globals (`frappe`, `cur_frm`, `__`). The shared bundle is `healthcare/public/js/healthcare.bundle.js`.
- **Patient Portal:** Vue 3, vue-router 4, **frappe-ui** (^0.1.176), TailwindCSS 3.4 (with the frappe-ui preset), Vite 4.4, and feather and lucide icons. The root `package.json` declares Yarn workspaces (`patient_portal`, `frappe-ui`).
- **Templates:** Jinja (`healthcare/templates`, `www/`) and print formats.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release.
