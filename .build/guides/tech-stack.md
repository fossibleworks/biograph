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
  - patient_portal/tailwind.config.js
  - healthcare/tests/utils.py
  - healthcare/hooks.py
  - .github/workflows/linters.v2.yml
  - crowdin.yml
---

- **Backend:** Python ≥ 3.10 (ruff targets py310; CI uses Python 3.14). It is a **Frappe Framework** app that depends on **ERPNext** (imports `erpnext.*`, and tests extend `ERPNextTestSuite`). It is packaged with `flit_core` from `pyproject.toml`. Runtime pip dependencies are `responses` and `python-barcode`.
- **Data/model layer:** Frappe DocTypes, each defined as JSON plus a Python controller plus an optional JS form script, under `healthcare/healthcare/doctype/<name>/`. The database is reached through the Frappe ORM (`frappe.get_all`, `frappe.db.get_value`, `frappe.qb`, sometimes `frappe.db.sql`).
- **Desk UI:** Frappe desk JavaScript (form scripts, `healthcare/public/js/*`, bundled through `healthcare.bundle.js` / `app_include_js`), with globals `frappe`, `erpnext`, `$` and `__`.
- **Patient Portal SPA:** Vue 3 with vue-router, **frappe-ui** (^0.1.176), Tailwind CSS 3.4 using the frappe-ui preset, Vite 4.4.9 with the `frappe-ui/vite` plugin, and feather/lucide icons. It is a Yarn workspace (`patient_portal`).
- **Tooling:** Node 24 in CI, Yarn (`yarn.lock`), ESLint 10 (flat config), Prettier, Ruff 0.15.18, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets.
- **i18n:** gettext `.pot`/`.po` files under `healthcare/locale`, synced through Crowdin.
- **Supported Frappe/ERPNext lines:** versions 14, 15 and 16, released on the `version-1x` branches. Patches exist for v15_0 and v16_0.
