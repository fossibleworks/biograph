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

- **Backend:** Python ≥3.10 (CI uses 3.14). The app is a **Frappe** app depending on **ERPNext** and **payments**. Packaging uses `flit_core`. Runtime Python dependencies are in `pyproject.toml` (`responses`, `python-barcode`).
- **Database:** MariaDB (CI uses `mariadb:11.8`, utf8mb4) and Redis, both through Frappe bench.
- **Desk UI:** plain Frappe desk JavaScript: doctype `.js` form scripts, `healthcare/public/js/*`, and a bundle at `healthcare.bundle.js`. Uses jQuery and the `frappe`/`erpnext` globals.
- **Patient Portal SPA:** Vue 3, vue-router and **frappe-ui**, styled with Tailwind 3.4 (frappe-ui preset) and built with Vite 4. It lives in `patient_portal/` (yarn workspace) and builds into `healthcare/public/patient_portal/assets`, served from `healthcare/www/patient_portal.html`.
- **Node:** Node 24 in CI. The root uses yarn workspaces (`yarn.lock`).
- **Tooling:** ruff (lint + format), prettier, ESLint 10 flat config, pre-commit, Frappe semgrep rules, pip-audit, detect-secrets, commitlint, semantic-release, CodeQL.
