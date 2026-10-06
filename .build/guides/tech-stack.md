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
  - yarn.lock
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

- **Backend:** Python ≥3.10 (ruff targets py310; CI runs Python 3.14). It is a **Frappe Framework** app and depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaging uses `flit_core`. Runtime deps include `python-barcode` and `responses`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` and `frappe.db.sql`.
- **Desk UI:** Frappe Desk form scripts in plain JavaScript: `<doctype>.js`, `_list.js`, `_calendar.js`, `_tree.js`, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js`. HTML snippets are rendered as Jinja/Frappe templates.
- **Patient Portal SPA:** Vue 3 + vue-router + **frappe-ui**, Vite 4.4.9, Tailwind CSS 3.4.15 (frappe-ui preset), PostCSS/autoprefixer, feather and lucide icons, socket.io (engine.io-client) for realtime.
- **JS tooling:** Yarn workspaces (`patient_portal`, `frappe-ui`) with `yarn.lock`, Node 24 in CI, ESLint 10 (flat config), Prettier.
- **Tooling:** pre-commit, ruff (lint + format), detect-secrets, pip-audit, Frappe semgrep rules, CodeQL, commitlint, semantic-release, Crowdin for translations, Mergify, Codecov.
- **Install/run:** standard `bench` (`bench get-app`, `bench --site <site> install-app healthcare`).
