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
  - patient_portal/vite.config.js
  - .github/workflows/ci.yml
  - yarn.lock
---

# Tech stack

## Backend
- **Python ≥ 3.10.** Ruff targets `py310`. CI runs Python **3.14**.
- **Frappe Framework** app named `healthcare`. `required_apps = ["frappe/erpnext"]`, so **ERPNext** is required.
- Packaging: `flit_core` (pyproject). The version string lives in `healthcare/__init__.py`.
- Runtime deps: `responses`, `python-barcode`.
- Database: **MariaDB** (CI uses `mariadb:11.8`). Redis/RQ is used through `frappe.enqueue` and scheduler events.

## Desk frontend (inside the app)
- Plain JS form scripts (`<doctype>.js`, `<doctype>_list.js`, `_tree.js`) running on Frappe Desk globals (`frappe`, `erpnext`, `$`, `moment`).
- A bundle entry at `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).

## Patient Portal SPA
- **Vue 3** + **vue-router 4** + **frappe-ui** + **Tailwind CSS 3.4** (frappe-ui preset), built with **Vite 4**.
- Uses feather/lucide icons.
- Yarn workspaces: the root `package.json` has the workspaces `patient_portal` and `frappe-ui`, and the lockfile is `yarn.lock`.
- Node 24 in CI.

## Tooling
- ruff (lint and format), ESLint 10 (flat config), Prettier (via pre-commit), semgrep (Frappe rules), pip-audit, detect-secrets
- commitlint, semantic-release, Mergify, CodeQL, Codecov, Crowdin (translations)
