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

# Tech stack

## Backend
- **Python ≥ 3.10.** `pyproject.toml` sets ruff `target-version = py310`. CI runs Python 3.14.
- **Frappe Framework + ERPNext.** ERPNext is a required app. CI tests against the frappe/erpnext `version-16` branches when the target branch is a fork branch.
- Packaging is **flit_core**. The version is dynamic and is read from `healthcare/__init__.py`.
- Extra Python deps: `responses`, `python-barcode`.
- Database: **MariaDB** (CI uses `mariadb:11.8`), with Redis.

## Frontend
- **Desk UI:** plain JavaScript form scripts that use Frappe globals (`frappe`, `cur_frm`, `__`, jQuery). They are bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- **Patient portal** (`patient_portal/`): **Vue 3**, vue-router, **frappe-ui**, **Tailwind CSS 3.4** with the frappe-ui preset, and **Vite 4.4.9** through the `frappe-ui/vite` plugin. It also uses feather/lucide icons.
- Package management is a **Yarn** workspace (`yarn.lock`). The root workspaces are `patient_portal` and `frappe-ui`.

## Tooling
ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, CodeQL, and Crowdin for translations.
