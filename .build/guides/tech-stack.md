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
  - yarn.lock
---

**Backend**
- Python 3.10 or newer (`requires-python >=3.10`, ruff target py310). CI runs on Python 3.14.
- **Frappe Framework** together with **ERPNext** (a required app). The code is metadata-driven: each DocType is a JSON definition plus a `.py` controller and a `.js` form script.
- Packaging uses `flit_core`. Runtime pip dependencies are `responses` and `python-barcode`.
- Database: MariaDB (CI uses `mariadb:11.8`).

**Desk frontend**
- Plain JavaScript form scripts that use the `frappe`, `erpnext` and jQuery globals.
- `healthcare.bundle.js` is included through `app_include_js`.

**Patient portal**
- `patient_portal/` is a Vue 3 + vue-router SPA built with **Vite 4.4.9**.
- Styling: **frappe-ui** components, Tailwind CSS 3.4.15 with the frappe-ui preset, PostCSS/autoprefixer, and feather-icons.
- Uses socket.io via `src/socket.js`.

**Tooling**
- Node 24 in CI. Yarn workspaces (`yarn.lock`, workspaces `patient_portal` and `frappe-ui`).
- ESLint 10 (flat config), Prettier, ruff, pre-commit, Semgrep (Frappe rules), CodeQL, pip-audit, detect-secrets.
- commitlint for conventional commits, semantic-release, Crowdin for translations.
