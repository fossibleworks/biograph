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
  - .github/helper/install.sh
  - healthcare/hooks.py
  - crowdin.yml
---

**Backend**
- **Python ≥ 3.10** (ruff target `py310`). CI runs Python **3.14**.
- **Frappe Framework** with **ERPNext** (and the `payments` app in CI). Targets the `version-16` Frappe/ERPNext branches.
- Packaging: `flit_core`, declared in `pyproject.toml`. Extra runtime deps: `responses`, `python-barcode`.
- Database: **MariaDB** (CI uses `mariadb:11.8`). Redis comes with Frappe.
- Data access goes through the Frappe ORM, `frappe.qb` (PyPika query builder) and `frappe.db.sql`.

**Desk frontend (classic Frappe UI)**
- Plain JavaScript form scripts (`<doctype>.js`, `<doctype>_list.js`, `*_tree.js`) plus jQuery/Frappe globals.
- Bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).

**Patient Portal SPA (`patient_portal/`)**
- **Vue 3**, **vue-router 4**, **frappe-ui** (component library and data resources), **Tailwind CSS 3.4** using the frappe-ui preset, **Vite 4.4**.
- Built output goes into the `healthcare` app's public assets.

**Tooling**
- Node 24 in CI. **Yarn** workspaces (`yarn.lock`).
- ruff, ESLint 10, Prettier, pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release.
- i18n: gettext `.pot` with Crowdin.
