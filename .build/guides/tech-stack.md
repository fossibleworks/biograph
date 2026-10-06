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
  - healthcare/hooks.py
  - .pre-commit-config.yaml
  - crowdin.yml
---

# Tech stack

## Backend
- **Python ≥ 3.10** (ruff targets `py310`; CI runs Python 3.14).
- **Frappe Framework** app named `healthcare`, with **ERPNext** as a required app. Packaged with `flit_core`.
- Extra runtime deps: `responses`, `python-barcode`.
- Database: **MariaDB** (CI uses `mariadb:11.8`).
- Background jobs use Frappe's `frappe.enqueue` (RQ). Cron-like jobs use `scheduler_events` in `hooks.py`.

## Desk frontend
- Plain JavaScript form scripts per doctype (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`) and shared bundles in `healthcare/public/js` (`healthcare.bundle.js` via `app_include_js`).
- jQuery and Frappe globals (`frappe`, `erpnext`, `__`).

## Patient Portal SPA (`patient_portal/`)
- **Vue 3**, **vue-router 4**, **frappe-ui**, **Tailwind CSS 3.4** (with the frappe-ui preset), **Vite 4.4.9**, feather icons and lucide icons.
- Yarn workspaces. The root `package.json` declares workspaces `patient_portal` and `frappe-ui`.

## Tooling
- ruff 0.15.18 (lint and format), Prettier, ESLint 10 (flat config), pre-commit, pip-audit, detect-secrets, Frappe semgrep rules, CodeQL, commitlint (conventional commits), semantic-release, Codecov, Mergify, Crowdin (translations).
