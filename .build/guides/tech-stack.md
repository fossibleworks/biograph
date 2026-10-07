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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

# Tech stack

## Backend
- **Python ≥ 3.10**. Ruff targets `py310` and CI runs on Python 3.14. The package is built with `flit_core`.
- **Frappe Framework** with **ERPNext** (a required app) and **payments**. Supported release lines are version-14, 15 and 16. Fork branches test against `version-16`.
- **MariaDB** (CI uses `mariadb:11.8`) and Redis, both through Frappe bench.
- Data access goes through the Frappe ORM (`frappe.get_doc`, `frappe.db.get_value/get_all`), the query builder (`frappe.qb`, PyPika), and some raw `frappe.db.sql`.
- Python runtime deps: `responses`, `python-barcode`.

## Desk frontend
- Plain Frappe Desk JavaScript form scripts (`frappe.ui.form.on(...)`), bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- jQuery and Frappe globals (`frappe`, `__`, `cur_frm`, `locals`, ...) are declared as ESLint globals.

## Patient Portal SPA (`patient_portal/`)
- **Vue 3** + **vue-router 4** + **frappe-ui** + **Tailwind CSS 3.4** (frappe-ui preset) + **Vite 4**. Icons come from feather and lucide.
- Yarn workspaces (`yarn.lock`). Node 24 in CI.

## Tooling
- ruff (lint and format), prettier, ESLint 10 (flat config), pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, CodeQL, commitlint, semantic-release, Codecov, Crowdin, Mergify.
