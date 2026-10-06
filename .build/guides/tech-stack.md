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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

**Backend:** Python ≥3.10 (CI runs 3.14) as a **Frappe Framework** app. `required_apps = ["frappe/erpnext"]`, so it needs **ERPNext**; CI also installs `payments`. The database is **MariaDB** (CI uses `mariadb:11.8`). Redis is used for the queue and cache. Packaging uses `flit_core` through `pyproject.toml`. Python dependencies include `responses` and `python-barcode`. The fork's target line is Frappe/ERPNext `version-16`.

**Desk frontend:** plain JavaScript files in `healthcare/public/js` and in each doctype's `<doctype>.js`. They use Frappe desk globals (`frappe`, `__`, `$`). They are bundled through `healthcare.bundle.js` (`app_include_js`).

**Patient portal:** **Vue 3** with `vue-router`, **frappe-ui** (^0.1.176) and **Tailwind CSS 3.4**, built with **Vite 4.4.9** and `feather-icons`. The JS package manager is Yarn workspaces (root `package.json` lists the `patient_portal` workspace; `yarn.lock` is committed). CI uses Node 24.

**Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Frappe semgrep rules, detect-secrets, pip-audit, commitlint and semantic-release. Translations are managed with Crowdin `.pot`/`.po` files.
