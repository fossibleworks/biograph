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
  - .github/helper/install.sh
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

- **Backend:** Python (>=3.10; CI runs 3.14). The app runs on the **Frappe Framework** and depends on **ERPNext** and **payments**, which CI installs via `bench get-app` on the matching `version-*` / `develop` branch, with `version-16` as the fallback for fork branches. Packaging uses `flit_core`. Runtime pip dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`, utf8mb4) plus Redis, as standard for Frappe bench.
- **Desk UI:** plain Frappe client scripts (`<doctype>.js`, `<doctype>_list.js`, `*_tree.js`). Shared code lives in `healthcare/public/js` and is bundled through `healthcare.bundle.js` (`app_include_js`). jQuery, moment and the `frappe` / `erpnext` globals are used.
- **Patient portal SPA:** **Vue 3** + **vue-router**, **frappe-ui** (components, `createResource`, Vite plugin), **Tailwind CSS 3.4** with the frappe-ui preset, **Vite 4.4**, socket.io client. It is a Yarn workspace (`patient_portal`).
- **Package managers:** Yarn (root `yarn.lock`, workspaces) for JS; pip/bench for Python.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), CodeQL, detect-secrets, pip-audit, commitlint, semantic-release, Crowdin (translations).
