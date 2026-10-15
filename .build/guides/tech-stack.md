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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

- **Backend:** Python ≥3.10 (`requires-python`). CI runs Python 3.14. The app is built on the **Frappe Framework** and depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`) and the `payments` app. It targets Frappe v14–v16, and the release branches are `version-14/15/16`.
- **Database:** MariaDB. CI uses `mariadb:11.8`. Queries use `frappe.qb` (pypika query builder), `frappe.db.get_value/exists`, and raw `frappe.db.sql`.
- **Python deps:** `responses`, `python-barcode`. Packaging uses `flit_core`.
- **Desk UI:** plain JavaScript form scripts that use Frappe globals (`frappe`, `cur_frm`, `__`, jQuery). They are bundled through `healthcare/public/js/healthcare.bundle.js` (esbuild via `bench build`).
- **Patient Portal SPA:** **Vue 3** + vue-router + **frappe-ui** + **Tailwind CSS 3.4**, built with **Vite 4**. The package manager is **Yarn** (workspaces: `patient_portal`, `frappe-ui`).
- **Tooling:** ruff (lint + format), prettier, ESLint 10 (flat config), pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release, CodeQL, Codecov, Crowdin (translations), Mergify.
- **Server tooling:** `bench` (frappe-bench) for running, building, testing and migrating.
