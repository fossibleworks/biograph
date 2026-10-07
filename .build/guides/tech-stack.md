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
  - patient_portal/vite.config.js
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - .releaserc
---

- **Backend:** Python ≥3.10 (`pyproject.toml`; ruff targets py310; CI runs Python 3.14). It is a **Frappe Framework** app on top of **ERPNext**, built with `flit_core`. Runtime Python deps are minimal (`responses`, `python-barcode`). Everything else comes from Frappe and ERPNext.
- **Data/ORM:** Frappe DocTypes (JSON metadata plus a Python controller plus an optional JS form script). Queries use `frappe.qb` (pypika query builder), `frappe.db.*` and `frappe.get_doc`. MariaDB is used through bench.
- **Desk UI:** Frappe desk JS. The bundle is `healthcare/public/js/healthcare.bundle.js`, and per-doctype form scripts are wired via `doctype_js` in `hooks.py`.
- **Patient Portal SPA:** Vue 3, vue-router 4, **frappe-ui**, Tailwind CSS 3.4 (frappe-ui preset), Vite 4.4.9 and socket.io-client. It lives in `patient_portal/`.
- **JS tooling:** Yarn workspaces (`yarn.lock`, root `package.json` workspaces `patient_portal` and `frappe-ui`). CI uses Node 24. ESLint 10 uses flat config (`eslint.config.mjs`). Prettier is also used.
- **Tooling:** bench, pre-commit, ruff, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release.
- **Supported Frappe/ERPNext lines:** version-14, version-15 and version-16 release branches. The fork's integration branch is `biograph-fh`.
