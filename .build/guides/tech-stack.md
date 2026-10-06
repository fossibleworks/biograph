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

- **Backend:** Python 3.10 or later (`requires-python >=3.10`; CI runs 3.14). It is a Frappe app that requires ERPNext. It is packaged with `flit_core` from `pyproject.toml`. Runtime dependencies are `python-barcode` and `responses`.
- **Database:** MariaDB (CI uses the `mariadb:11.8` service). Queries use the Frappe ORM (`frappe.db.*`) and `frappe.qb` (PyPika query builder).
- **Desk UI:** Frappe form scripts in plain JavaScript (jQuery/Frappe globals), one per doctype (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`), plus shared bundles in `healthcare/public/js` (`healthcare.bundle.js`).
- **Patient portal:** Vue 3 + vue-router, frappe-ui (~0.1.176), Tailwind CSS 3.4.15, built with Vite 4.4.9 and `@vitejs/plugin-vue`. Yarn workspaces are used (`yarn.lock`, workspaces `patient_portal` and `frappe-ui`).
- **Node:** 24 in CI.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release, Crowdin (translations, `main.pot`).
