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
  - healthcare/hooks.py
---

- **Backend:** Python 3.10 or newer (`requires-python >=3.10`; CI uses 3.14). It runs on the **Frappe** framework with **ERPNext** as a required app. The package is built with flit_core. Extra Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses the `mariadb:11.8` service).
- **Desk UI:** Frappe desk JavaScript (form scripts per doctype, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js`). Jinja and HTML templates are used for print formats and web pages.
- **Patient portal:** Vue 3 SPA in `patient_portal/`, built with Vite 4.4.9, `frappe-ui`, Tailwind CSS 3.4.15 (using the frappe-ui preset), vue-router and feather/lucide icons.
- **Package management:** yarn workspaces (`yarn.lock`; the root `package.json` lists the `patient_portal` workspace). Node 24 is used in CI.
- **Tooling:** ruff (lint and format), prettier, eslint 10 (flat config), pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint and semantic-release.
