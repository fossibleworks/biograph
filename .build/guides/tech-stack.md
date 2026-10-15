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
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

- **Backend:** Python 3.10 or later (`requires-python >=3.10`; CI runs 3.14) on the **Frappe Framework** with **ERPNext** as a required app. Packaged with `flit_core`. The data model is Frappe DocTypes: a JSON schema, a Python controller and a JS form script per doctype.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Queries use `frappe.qb` (pypika), `frappe.get_all`/`get_list` and raw `frappe.db.sql`.
- **Desk frontend:** plain JavaScript form and list scripts using Frappe globals (`frappe`, `cur_frm`, `__`, jQuery). They are bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- **Patient Portal:** Vue 3 + vue-router + **frappe-ui**, built with Vite 4 and styled with Tailwind CSS 3 (frappe-ui preset). Uses `feather-icons` and Lucide icons through the frappe-ui Vite plugin, and socket.io for realtime.
- **Package management:** Yarn workspaces at the root (`patient_portal`). `yarn.lock` is committed.
- **Python dependencies:** `responses`, `python-barcode`. Everything else comes from the Frappe/ERPNext bench.
- **Tooling:** ruff (lint and format), prettier, eslint 10 (flat config), pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release.
