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
  - healthcare/hooks.py
  - crowdin.yml
---

- **Backend:** Python 3.10 or later (`requires-python >=3.10`, ruff target `py310`; CI runs on Python 3.14). It is a **Frappe Framework** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaging uses `flit_core`. The extra Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (pypika query builder) and `frappe.db`.
- **Desk UI:** plain JavaScript Frappe form scripts (`<doctype>.js`, `_list.js`, `_tree.js`, `_calendar.js`) plus `healthcare/public/js/*`, bundled through `healthcare.bundle.js`.
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 with the frappe-ui preset, and Vite 4 (built with the `frappe-ui/vite` plugin). It lives in a Yarn workspace under `patient_portal/`.
- **Node:** version 24 in CI. The package manager is Yarn: `yarn.lock` at the root, workspaces `patient_portal` and `frappe-ui`.
- **Tooling:** ruff for linting and formatting, ESLint 10 (flat config), Prettier, pre-commit, Semgrep with the Frappe rules, CodeQL, detect-secrets, pip-audit, commitlint, and semantic-release.
- **i18n:** gettext `.pot` and `.po` files under `healthcare/locale`, synced through Crowdin.
