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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - crowdin.yml
---

# Tech stack

## Backend
- **Python ≥ 3.10** (ruff target `py310`; CI runs Python 3.14). Packaged with **flit_core**, and the version lives in `healthcare/__init__.py`.
- **Frappe Framework** app with a hard dependency on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Supported release lines are version-14, version-15, and version-16.
- Database: **MariaDB** (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (PyPika query builder), and `frappe.db`.
- Extra Python dependencies: `responses`, `python-barcode`.

## Desk frontend
- Classic Frappe Desk JavaScript (form scripts `<doctype>.js`, `*_list.js`, `*_tree.js`). It is bundled through `healthcare/public/js/healthcare.bundle.js` and uses jQuery and the `frappe` / `erpnext` globals.

## Patient Portal SPA (`patient_portal/`)
- **Vue 3** + **vue-router 4**, **Vite 4.4.9**, **Tailwind CSS 3.4.15** with the **frappe-ui** preset and components, and feather/lucide icons.
- Managed with **Yarn** workspaces (`yarn.lock` at the root, workspaces `patient_portal` and `frappe-ui`).

## Tooling
- Node 24 in CI, ESLint 10 (flat config), Prettier, Ruff (lint + format), pre-commit, Semgrep (Frappe rules), CodeQL, pip-audit, detect-secrets, commitlint, and semantic-release.
- Translations: gettext `.pot`/`.po` files synced through Crowdin.
