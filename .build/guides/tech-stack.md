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
  - yarn.lock
---

- **Backend:** Python ≥3.10 (`pyproject.toml`; CI runs Python 3.14). The app runs on the **Frappe Framework**, with **ERPNext** and **payments** as required apps. It is packaged with `flit_core`. Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`) and Redis, both managed through Frappe `bench`.
- **Desk UI:** plain Frappe Desk JavaScript (form scripts, `frappe.ui.form`, jQuery globals). It is bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`). Doctype form scripts sit next to each doctype's `.py` and `.json` files.
- **Patient portal:** **Vue 3** with `<script setup>`, **frappe-ui** (^0.1.176), vue-router, **Vite 4.4.9**, **Tailwind CSS 3.4.15** using the frappe-ui preset, and feather/lucide icons.
- **Package managers:** Yarn workspaces at the root (`yarn.lock`, workspaces `patient_portal` and `frappe-ui`), and pip/bench for Python.
- **Tooling:** ruff, prettier, eslint 10 (flat config), pip-audit, detect-secrets and semgrep (Frappe rules), plus commitlint and semantic-release.
- **Supported Frappe/ERPNext lines:** release branches cover versions 14, 15 and 16. The fork develops against **version-16**.
