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
  - yarn.lock
  - crowdin.yml
---

## Backend

- **Python ≥3.10** (ruff targets py310; CI runs on Python 3.14). The package is built with `flit_core` (`pyproject.toml`), and the version is dynamic from `healthcare/__init__.py`.
- **Frappe Framework** (metadata-driven DocTypes, `@frappe.whitelist()` RPC, hooks) plus **ERPNext**. The `payments` app is installed in CI.
- The database is **MariaDB** (CI uses `mariadb:11.8`). Redis is used for queue/cache via bench.
- Extra Python dependencies are `responses`, `python-barcode`, and `requests` (used for ABDM calls).

## Desk frontend

- Plain JavaScript loaded by Frappe: form scripts `<doctype>.js`, `*_list.js`, `*_calendar.js`, and `healthcare/public/js/*` bundled through `healthcare.bundle.js`. It uses the jQuery/Frappe globals (`frappe`, `__`, `cur_frm`, …).

## Patient Portal SPA

- `patient_portal/` uses **Vue 3**, **vue-router**, **frappe-ui** (components plus `createResource`), **Vite 4.4.9**, **Tailwind CSS 3.4.15** (with the frappe-ui preset), PostCSS/autoprefixer, and feather/lucide icons.
- The root `package.json` is a Yarn workspace (`patient_portal`, `frappe-ui`), and `yarn.lock` is committed.

## Tooling

- Linting and checks: ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, detect-secrets, pip-audit, Semgrep (frappe rules), CodeQL.
- Releases and commits: semantic-release and commitlint (conventional commits).
- Other services: Crowdin for translations (`healthcare/locale/main.pot`) and Codecov for coverage.
