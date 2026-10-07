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
  - crowdin.yml
---

- **Backend:** Python ≥3.10 (ruff targets py310; CI runs Python 3.14). Built as a **Frappe** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaged with `flit_core`. Runtime pip dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM (`frappe.get_doc`, `frappe.db.*`), with some raw `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts (`<doctype>.js`), jQuery, and Frappe globals (`frappe`, `__`, `cur_frm`). They are bundled through `healthcare/public/js/healthcare.bundle.js`.
- **Patient Portal:** a **Vue 3** SPA built with **Vite 4**, **frappe-ui**, **Tailwind CSS 3** (frappe-ui preset), vue-router, feather/lucide icons, and socket.io (`socket.js`).
- **JS tooling:** Yarn workspaces (`patient_portal`, `frappe-ui`), Node 24 in CI, ESLint 10 flat config, Prettier.
- **Tooling:** pre-commit, ruff (lint and format), semgrep with Frappe rules, CodeQL, detect-secrets, pip-audit, commitlint, semantic-release.
- **i18n:** a gettext `main.pot` file, synced through Crowdin.
