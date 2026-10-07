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
  - healthcare/__init__.py
---

# Tech stack

- **Backend:** Python >= 3.10 (ruff targets py310; CI runs 3.14) on the **Frappe framework** with **ERPNext** (a required app) and `payments`. The package builds with `flit_core`. Runtime deps in `pyproject.toml`: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), plus Redis through bench.
- **Desk UI:** Frappe desk JavaScript. Per-doctype `<doctype>.js` and `_list.js` files, and shared code in `healthcare/public/js`, bundled through `healthcare.bundle.js` (`app_include_js`).
- **Patient portal:** Vue 3 + vue-router + **frappe-ui**, built with Vite 4 and styled with Tailwind 3 (frappe-ui preset). Yarn workspaces are set in the root `package.json` (`patient_portal`, `frappe-ui`).
- **Tooling:** ruff (lint and format), prettier, eslint 10 (flat config), pre-commit, detect-secrets, pip-audit, semgrep with Frappe rules, CodeQL, commitlint, and semantic-release.
- **Node:** CI uses Node 24.
- **Version targets:** Frappe/ERPNext `version-16` (the version-14/15/16 lines are released). `healthcare/__init__.py` holds `__version__` (currently 16.0.8).
