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
  - healthcare/__init__.py
  - .releaserc
---

- **Backend:** Python ≥3.10, with ruff targeting py310. CI runs Python 3.14. The app is built on the **Frappe Framework** and **ERPNext** and is packaged with `flit_core`. Runtime pip dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Data access uses Frappe ORM, `frappe.qb` (pypika query builder) and some raw `frappe.db.sql`.
- **Desk UI:** plain JavaScript form scripts per DocType (`<doctype>.js`, `<doctype>_list.js`), using jQuery and Frappe globals. Desk JS is bundled through `healthcare.bundle.js` (`app_include_js`).
- **Patient portal:** Vue 3, vue-router, the **frappe-ui** component library, Tailwind CSS 3.4 with the frappe-ui preset, and Vite 4. It is a Yarn workspace (`patient_portal`).
- **Node:** Node 24 in CI. The root `package.json` declares Yarn workspaces and ESLint 10.
- **Tooling:** pre-commit, ruff (lint and format), ESLint, Prettier, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, Codecov, CodeQL, Crowdin for translations, and Mergify.
- **Version lines:** the app is released for Frappe/ERPNext v14, v15 and v16 (`version-14/15/16` branches). The current version is `16.0.8`.
