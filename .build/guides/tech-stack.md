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
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - healthcare/hooks.py
  - yarn.lock
---

- **Backend:** Python ≥3.10 (ruff target `py310`; CI runs Python 3.14). It is a **Frappe Framework app** that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaging uses `flit_core`. Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Queries go through the Frappe ORM, `frappe.qb` (PyPika query builder) and `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts per doctype (`<doctype>.js`), bundled via `healthcare/public/js/healthcare.bundle.js`. They use Frappe/jQuery globals.
- **Patient Portal SPA:** **Vue 3** + **vue-router** + **frappe-ui**. It is built with **Vite 4** and styled with **Tailwind CSS 3** (frappe-ui preset) and PostCSS/autoprefixer. Icons come from feather-icons and lucide (via the frappe-ui vite plugin).
- **Package managers:** Yarn workspaces (`yarn.lock` at the root; workspaces `patient_portal`, `frappe-ui`) and pip.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), CodeQL, detect-secrets, pip-audit, commitlint, semantic-release, Crowdin for translations.
- **Deployment target:** a Frappe bench (`bench get-app`, `bench --site <site> install-app healthcare`) or Frappe Cloud.
