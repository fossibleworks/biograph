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
  - yarn.lock
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - healthcare/hooks.py
---

**Backend**
- Python 3.10 or newer (`requires-python >=3.10`, ruff `target-version py310`). CI runs Python **3.14**.
- **Frappe Framework** with **ERPNext** as a required app. The fork's CI tests against Frappe/ERPNext `version-16`.
- Database: **MariaDB**. CI uses the `mariadb:11.8` image. Redis is installed by the CI install script.
- Packaging: `flit_core`. Runtime dependencies are pinned in `pyproject.toml`: `responses`, `python-barcode`.
- Server logic lives in DocType controllers (`frappe.model.document.Document`), whitelisted methods, `frappe.qb` query builder, and doc_events and scheduler hooks in `hooks.py`.

**Desk frontend**
- Plain Frappe desk JavaScript: form scripts `<doctype>.js`, `*_list.js` and `*_tree.js`, bundled through `healthcare/public/js/healthcare.bundle.js`. Uses jQuery and Frappe globals.

**Patient Portal SPA** (`patient_portal/`)
- **Vue 3**, vue-router 4, **frappe-ui**, **Vite 4.4.9**, **Tailwind CSS 3.4.15** (frappe-ui preset), PostCSS/autoprefixer, feather and lucide icons.
- Yarn workspaces at the root (`yarn.lock`). `postinstall` installs the portal's dependencies.

**Tooling**
- Node 24 in CI
- ruff, ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, CodeQL
- commitlint (conventional commits), semantic-release, Crowdin for translations
