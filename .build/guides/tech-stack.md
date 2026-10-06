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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - yarn.lock
---

**Backend:**
- Python ≥3.10. ruff targets py310, and CI runs Python 3.14.
- **Frappe Framework** app `healthcare` with a hard dependency on **ERPNext**. CI also installs the `payments` app.
- Packaged with `flit_core` (`pyproject.toml`). The version string lives in `healthcare/__init__.py`.
- Database: **MariaDB** (CI uses `mariadb:11.8`), plus Redis.
- Extra Python dependencies: `responses`, `python-barcode`.

**Desk frontend:**
- Frappe Desk JavaScript: doctype `.js` controllers, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js`.
- Globals in use: jQuery, `frappe`, `erpnext`.

**Patient Portal (`patient_portal/`):**
- **Vue 3** with `vue-router`, **frappe-ui**, **Tailwind CSS 3.4** (frappe-ui preset), and **Vite 4.4.9**.
- Yarn workspaces (`yarn.lock`). The root `package.json` declares workspaces `patient_portal` and `frappe-ui`.

**Tooling:**
- Node 24 in CI
- ruff (lint and format)
- ESLint 10 (flat config) and Prettier
- pre-commit, semgrep (Frappe rules), CodeQL, pip-audit, detect-secrets
- commitlint and semantic-release

**Version lines:** Frappe/ERPNext `version-14`, `version-15`, and `version-16`. The fork tracks version-16.
