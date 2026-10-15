---
title: Tech Stack
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
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - healthcare/hooks.py
---

# Tech Stack

## Backend
- **Python ≥ 3.10**, declared in `pyproject.toml`. CI runs Python 3.14. The package is built with `flit_core`.
- **Frappe Framework** and **ERPNext** (`required_apps = ["frappe/erpnext"]`). The `payments` app is installed in CI and used for the portal payment gateway.
- **MariaDB**: CI uses `mariadb:11.8`, with Redis.
- Python dependencies: `responses`, `python-barcode`.
- The app version lives in `healthcare/__init__.py` (`__version__`). The current major line is 16.

## Desk frontend
- Plain JavaScript form scripts, using Frappe globals (`frappe`, `cur_frm`, `__`, and so on), one per DocType: `<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`, `<doctype>_calendar.js`.
- Shared desk JS is bundled from `healthcare/public/js/healthcare.bundle.js` through Frappe's esbuild asset pipeline (`app_include_js`).
- Jinja `.html` templates are used for print formats and desk widgets.

## Patient Portal SPA
- **Vue 3**, **vue-router**, **frappe-ui** (Button, Dialog, Card, createResource and so on) and **feather-icons**.
- **Vite 4** with the `frappe-ui/vite` plugin. **Tailwind CSS 3.4** with the `frappe-ui/tailwind` preset, plus PostCSS and Autoprefixer.
- Lives in the `patient_portal/` yarn workspace. The root `package.json` declares the workspaces `patient_portal` and `frappe-ui`.

## Tooling
- Yarn (`yarn.lock`). Node 24 in CI.
- Ruff for Python lint and format, ESLint 10 (flat config) and Prettier for JS, and pre-commit.
- Semgrep with the Frappe rules, CodeQL, detect-secrets and pip-audit.
- semantic-release and commitlint (conventional commits). Mergify. Crowdin for translations.
