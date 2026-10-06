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
  - healthcare/hooks.py
  - eslint.config.mjs
---

**Backend**
- Python 3.10 or newer (`requires-python >=3.10`; ruff targets py310; CI runs Python 3.14).
- Built with `flit_core`.
- A **Frappe Framework** app that depends on **ERPNext** (imports `erpnext.*`). Uses Frappe DocTypes (JSON, Python controller and JS form script per DocType), `frappe.qb` (pypika query builder), `frappe.db`, whitelisted RPC methods, hooks, scheduler events and patches.
- Database: MariaDB (CI uses `mariadb:11.8`).
- Extra Python dependencies: `responses`, `python-barcode`.

**Desk frontend**
- Plain JavaScript Frappe form scripts (`<doctype>.js`, `<doctype>_list.js`, `_tree.js`).
- Shared desk code is bundled through `healthcare/public/js/healthcare.bundle.js`, registered as `app_include_js` in `hooks.py`.
- Uses jQuery, the `frappe` and `erpnext` globals, and `__()` for translation.

**Patient Portal SPA (`patient_portal/`)**
- Vue 3, vue-router 4, **frappe-ui**, Tailwind CSS 3.4 (with the frappe-ui preset), Vite 4.4 and `@vitejs/plugin-vue`.
- Uses feather and lucide icons.
- Yarn workspaces are set up from the root `package.json` (`yarn.lock`).

**Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, Frappe semgrep rules, CodeQL, pip-audit, detect-secrets, commitlint, semantic-release and Codecov.
