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
  - healthcare/hooks.py
  - yarn.lock
---

**Backend**
- Python **>=3.10** (`pyproject.toml`; ruff targets `py310`). CI runs Python **3.14**.
- **Frappe Framework + ERPNext**. Payments is also installed in CI. The app is built against the matching `version-16` / `develop` branches of frappe, erpnext and payments.
- Database: **MariaDB** (CI uses the `mariadb:11.8` service with utf8mb4). Redis is used through bench.
- Packaging: `flit_core`. Runtime Python dependencies are `responses`, `python-barcode` and `requests` (the ABDM integration uses requests).
- PDF printing relies on wkhtmltopdf, which CI installs.

**Desk frontend**
- Plain JavaScript form scripts per doctype (`<doctype>.js`, `_list.js`, `_tree.js`, `_calendar.js`), plus shared code in `healthcare/public/js`, bundled through `healthcare.bundle.js` (`app_include_js`).
- These scripts use the Frappe client globals (`frappe`, `erpnext`, `__`, jQuery `$`, `moment`).

**Patient Portal SPA** (`patient_portal/`)
- **Vue 3** + **vue-router 4**, **Vite 4.4.9**, **frappe-ui** (^0.1.176), **Tailwind CSS 3.4.15** with the frappe-ui preset, PostCSS/autoprefixer, feather-icons and lucide icons.
- The root `package.json` is a Yarn workspace (`patient_portal`, `frappe-ui`) with a `yarn.lock`.

**Tooling:** Node 24 in CI, ruff 0.15.18, ESLint 10.5 (flat config), Prettier 3.1 (mirror), pre-commit, semgrep with Frappe rules, CodeQL, detect-secrets, pip-audit, commitlint, semantic-release, Crowdin for translations, Codecov.
