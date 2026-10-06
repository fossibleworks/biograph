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
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - healthcare/hooks.py
---

- **Backend:** Python ≥3.10 (ruff targets py310; CI runs Python 3.14). Packaged as a **Frappe app** (`flit_core` build backend) that requires **ERPNext** and the `payments` app. The database is **MariaDB** (CI uses `mariadb:11.8`), with Redis through the Frappe bench.
- **Python dependencies:** `responses`, `python-barcode` (pyproject).
- **Desk UI:** plain JavaScript Frappe form scripts (`<doctype>.js` next to each doctype), bundled through `healthcare/public/js/healthcare.bundle.js`, using the jQuery/Frappe globals.
- **Patient portal SPA:** `patient_portal/` uses **Vue 3**, vue-router 4, **frappe-ui** (^0.1.176), **Vite 4.4.9**, **Tailwind CSS 3.4.15** with the frappe-ui preset, and feather/lucide icons.
- **Package management:** Yarn workspaces at the root (`yarn.lock`, workspaces `patient_portal`, `frappe-ui`). Node 24 in CI.
- **Tooling:** ruff (lint and format), prettier, eslint 10, pre-commit, semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, CodeQL.
- **Deployment target:** Frappe bench (`bench get-app`, `bench --site … install-app healthcare`), also offered on Frappe Cloud.
