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
---

- **Backend:** Python ≥3.10 (CI runs 3.14) Frappe app named `healthcare`. It requires **ERPNext** and the **payments** app, and targets Frappe/ERPNext `version-16`. It is packaged with `flit_core` through `pyproject.toml`. Runtime dependencies are `python-barcode` and `responses`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Redis is used for the Frappe queue and cache.
- **Desk UI:** Frappe Desk form scripts in plain JavaScript (jQuery and the `frappe` globals), bundled via `healthcare.bundle.js`.
- **Patient portal:** Vue 3, vue-router, `frappe-ui` (with the frappe-ui Tailwind preset and Vite plugin), Tailwind CSS 3.4, Vite 4, and feather/lucide icons.
- **Tooling:** Yarn workspaces with root `yarn.lock`, ESLint 10 (flat config), Prettier, Ruff, pre-commit, Semgrep (frappe rules), CodeQL, semantic-release, commitlint and Crowdin for translations.
