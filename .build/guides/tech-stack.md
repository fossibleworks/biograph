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
  - .github/helper/install.sh
  - .github/workflows/ci.yml
  - yarn.lock
---

- **Backend:** Python 3.10+ (`requires-python >=3.10`; CI runs 3.14), packaged with `flit_core`. Built as a **Frappe app** that needs **ERPNext** (and `payments` in CI). The database is MariaDB (CI uses `mariadb:11.8`). Runtime extras: `python-barcode` and `responses`.
- **Branch targets:** the Frappe/ERPNext `version-16` line. Fork branches such as `biograph-fh` and `goal/*` are tested against `version-16`.
- **Desk frontend:** plain Frappe Desk JavaScript (doctype `.js` controllers, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js`). jQuery and the `frappe` globals are available.
- **Patient portal:** Vue 3 + vue-router 4, built with Vite 4.4.9 and `@vitejs/plugin-vue`. Uses the **frappe-ui** component library and TailwindCSS 3.4.15 (frappe-ui preset), plus feather and lucide icons.
- **Package managers:** yarn workspaces at the root (`patient_portal`, `frappe-ui`) with `yarn.lock`. Node 24 in CI.
- **Tooling:** ruff (lint and format), prettier, eslint 10 (flat config), pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint, semantic-release, CodeQL (python and javascript).
