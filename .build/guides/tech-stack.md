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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

- **Backend:** Python ≥3.10 (`requires-python`; ruff targets py310, and CI runs Python 3.14). It is a **Frappe Framework** app that requires **ERPNext** (`required_apps = ["frappe/erpnext"]`) and is tested together with the `payments` app. Packaging uses `flit_core`. Runtime Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`). Data access goes through the Frappe ORM, `frappe.qb` (pypika query builder) and some `frappe.db.sql`.
- **Desk UI:** Frappe Desk form, list and tree scripts in plain JavaScript (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`). Shared code lives in `healthcare/public/js`, bundled as `healthcare.bundle.js`. There are also Jinja/HTML templates for pages and print formats.
- **Patient portal SPA:** **Vue 3** + **vue-router 4** + **frappe-ui** (0.1.x), built with **Vite 4.4.9** and styled with **Tailwind CSS 3.4.15** + PostCSS/autoprefixer. It uses socket.io-client for realtime updates and feather/lucide icons.
- **JS tooling:** Yarn workspaces (`yarn.lock`; root `package.json` workspaces `patient_portal`, `frappe-ui`). Node 24 in CI. ESLint 10 flat config and Prettier.
- **Tooling:** pre-commit, ruff (lint and format), detect-secrets, pip-audit, Semgrep with the Frappe rules, CodeQL, commitlint, semantic-release, Codecov, Mergify, and Crowdin for translations.
- **Deployment target:** Frappe bench (`bench get-app`, `bench --site … install-app healthcare`) and Frappe Cloud.
