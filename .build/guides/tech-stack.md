---
title: Tech Stack
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
  - healthcare/__init__.py
---

- **Backend:** Python ≥3.10 (CI runs 3.14), as a **Frappe framework** app that depends on **ERPNext** and **payments**. It is packaged with `flit_core` (`pyproject.toml`). The version is kept in `healthcare/__init__.py` (`16.0.8`). Runtime deps are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`, utf8mb4). Redis is used for the bench.
- **Desk UI:** Frappe desk JavaScript: per-doctype `<doctype>.js`, `_list.js` and `_tree.js` files, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js`. It uses jQuery and Frappe globals (`frappe`, `erpnext`, `__`).
- **Patient Portal SPA:** Vue 3, vue-router 4, **frappe-ui** (^0.1.176), Tailwind CSS 3.4.15 with the frappe-ui preset, built with Vite 4.4.9 and `@vitejs/plugin-vue`. Yarn workspaces (`yarn.lock`) are used.
- **Tooling:** ruff (lint and format), ESLint 10 flat config, Prettier, pre-commit, Semgrep with the Frappe rules, pip-audit, detect-secrets, commitlint, semantic-release, Codecov, Crowdin (translations), Mergify.
- **Target branches upstream:** Frappe/ERPNext `version-16` (the fork's CI tests against version-16).
