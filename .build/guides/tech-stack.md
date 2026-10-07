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
  - yarn.lock
  - healthcare/hooks.py
---

- **Backend:** Python 3.10+ (`requires-python >=3.10`; CI runs Python 3.14). The package is built with `flit_core`. It is a **Frappe Framework** app and needs **ERPNext** (`required_apps = ["frappe/erpnext"]`).
- **Database:** MariaDB (CI uses `mariadb:11.8`). Data access uses the Frappe ORM, `frappe.qb`, and raw `frappe.db.sql`.
- **Desk UI:** Frappe form and list scripts in plain JavaScript (`<doctype>.js`, `<doctype>_list.js`) plus the `healthcare/public/js/healthcare.bundle.js` bundle. ESLint globals include `frappe`, `erpnext`, `$`, `moment` and similar.
- **Patient Portal SPA:** Vue 3, vue-router 4, **frappe-ui**, Tailwind CSS 3.4 and Vite 4, organised as a Yarn workspace under `patient_portal/`.
- **Python dependencies:** `responses`, `python-barcode`.
- **Tooling:** ruff, prettier, eslint 10, pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint and semantic-release.
- **Node:** 24 in CI. Yarn is the package manager (`yarn.lock`).
