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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - yarn.lock
  - .github/workflows/ci.yml
  - .github/helper/install.sh
---

# Tech stack

## Backend
- **Python** Frappe app `healthcare`, packaged with `flit_core` (`pyproject.toml`).
- `requires-python >=3.10`. Ruff targets `py310`. CI runs Python **3.14**.
- **Frappe framework + ERPNext** (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app.
- Database: **MariaDB** (CI uses `mariadb:11.8`). Redis comes with Frappe bench.
- Extra Python deps are only `responses` and `python-barcode`. Everything else comes from Frappe/ERPNext.
- Desk UI: classic Frappe form scripts (`*.js` next to each doctype). App-wide JS is bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`) and uses jQuery/Frappe globals.
- Print and HTML templates use Jinja.

## Patient portal (frontend)
- **Vue 3** + **vue-router 4** + **frappe-ui** (`createResource`, `Card`, `ErrorMessage`, etc.).
- **Vite 4.4.9** with the `frappe-ui/vite` plugin (frappe proxy, lucide icons, jinja boot data).
- **Tailwind CSS 3.4.15** using the frappe-ui Tailwind preset, plus PostCSS/autoprefixer.
- Yarn workspaces: the root `package.json` workspaces are `patient_portal` and `frappe-ui`. The lockfile is `yarn.lock`.
- CI uses Node **24**.

## Tooling
- ruff (lint + format)
- ESLint 10 (flat config)
- Prettier
- pre-commit
- Semgrep with the Frappe rules
- pip-audit
- detect-secrets
- commitlint
- semantic-release
- Crowdin for translations
