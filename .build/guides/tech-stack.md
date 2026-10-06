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
  - .github/helper/install.sh
  - healthcare/hooks.py
---

- **Backend:** Python 3.10 or newer (`requires-python >=3.10`; ruff targets py310). CI runs Python 3.14. It is a **Frappe app** that requires **ERPNext** (and installs **payments** in CI). Packaging uses `flit_core`.
- **Database:** MariaDB 11.8 in CI. Redis is used by the bench.
- **Desk UI:** plain Frappe form scripts in JavaScript (`healthcare/public/js/*.js`, `doctype/*/*.js`), bundled through `healthcare.bundle.js` (`app_include_js`). They use jQuery and the `frappe`/`erpnext` globals.
- **Patient Portal:** **Vue 3**, vue-router 4, **frappe-ui**, **Tailwind CSS 3.4** with the frappe-ui preset, and **Vite 4**. It is a yarn workspace (`patient_portal`, `frappe-ui`).
- **Node:** 24 in CI. Yarn is the root package manager (`yarn.lock`).
- **Python deps:** `responses`, `python-barcode`. Most dependencies come from frappe and erpnext.
- **Tooling:** ruff (lint and format), prettier, eslint 10 (flat config), pre-commit, pip-audit, detect-secrets, Frappe semgrep rules, commitlint, semantic-release.
