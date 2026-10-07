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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - crowdin.yml
  - yarn.lock
---

- **Backend:** Python ≥3.10. Ruff targets py310, and CI runs Python 3.14. It is a **Frappe Framework** app with `required_apps = ["frappe/erpnext"]` and is packaged with `flit_core` (`pyproject.toml`). Runtime dependencies are pinned in pyproject (`responses`, `python-barcode`).
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM (`frappe.get_doc`, `frappe.db.*`) and sometimes raw `frappe.db.sql`.
- **Desk UI:** plain Frappe client scripts (`<doctype>.js` next to each doctype, and `healthcare/public/js/*.js`), bundled as `healthcare.bundle.js`. Globals such as `frappe`, `erpnext`, `$` and `moment` are used directly.
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui** components, Tailwind CSS 3.4 (frappe-ui preset), and Vite 4. The build output goes to `healthcare/public/frontend`.
- **Package management:** Yarn workspaces (`yarn.lock`; workspaces `patient_portal`, `frappe-ui`). Node 24 in CI.
- **Tooling:** pre-commit, ruff (lint and format), ESLint 10 (flat config), Prettier, pip-audit, detect-secrets, Semgrep (Frappe rules), CodeQL, commitlint, semantic-release.
- **i18n:** gettext POT at `healthcare/locale/main.pot`, synced with Crowdin.
- **Supported versions:** release branches `version-14`, `version-15`, `version-16`. The fork tests against Frappe/ERPNext `version-16`.
