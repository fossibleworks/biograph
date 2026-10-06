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
  - yarn.lock
---

- **Backend:** Python ≥3.10 (CI uses 3.14) on the **Frappe framework**, with **ERPNext** and **payments** installed as sibling apps in the same bench. The package is built with `flit_core`. Runtime dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), plus Redis via bench. Queries use the Frappe ORM (`frappe.get_doc`, `frappe.db.*`) and `frappe.qb`, a PyPika-based query builder. Raw `frappe.db.sql` also appears, mostly in tests.
- **Desk UI:** Frappe form scripts in plain JavaScript. There is one `<doctype>.js` per doctype, and shared scripts live in `healthcare/public/js`, bundled through `healthcare.bundle.js`.
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 and Vite 4.4. Its package manager is Yarn: the root `package.json` declares workspaces, and `yarn.lock` is committed.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint and semantic-release.
- **Target platform:** Frappe/ERPNext `version-16` branches (`version-14` and `version-15` are also release branches). The CI install script tests fork branches against `version-16`.
