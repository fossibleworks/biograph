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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - yarn.lock
---

- **Backend:** Python ≥3.10 (CI runs 3.14) as a **Frappe** app that requires **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaged with `flit_core`, and the version is read dynamically from `healthcare/__init__.py`. Extra Python dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB. CI uses `mariadb:11.8`.
- **Desk UI:** Frappe desk client scripts in plain JavaScript (doctype `*.js`, `*_list.js`, `*_tree.js`, `*_calendar.js`) and Jinja/HTML templates. The desk bundle is `healthcare.bundle.js`.
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui** (^0.1.176), Vite 4.4.9, TailwindCSS 3.4.15 (frappe-ui preset), PostCSS/autoprefixer, feather/lucide icons.
- **Node tooling:** Yarn workspaces (`patient_portal`, `frappe-ui`) with `yarn.lock`. Node 24 in CI.
- **Tooling:** ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, CodeQL, commitlint, semantic-release.
- **Deployment target:** a Frappe bench (`bench get-app` / `bench --site <site> install-app healthcare`) or Frappe Cloud.
