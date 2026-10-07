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

- **Backend:** Python 3.10 or newer (`requires-python >=3.10`, ruff `target-version py310`). CI runs Python **3.14**. The app runs on the **Frappe framework**, with **ERPNext** required. Development targets the Frappe/ERPNext `version-16` line; CI clones `version-16` for fork branches.
- **Packaging:** `flit_core` via `pyproject.toml`. The version lives in `healthcare/__init__.py` (currently `16.0.8`). Runtime Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), plus Redis.
- **Desk UI:** plain Frappe form scripts (`frappe.ui.form.on`) and jQuery-era globals. Shared desk JS is bundled from `healthcare/public/js/healthcare.bundle.js`.
- **Patient Portal:** **Vue 3**, vue-router 4 and **frappe-ui** (`^0.1.176`), built with **Vite 4.4.9** and styled with **Tailwind 3.4.15** using the frappe-ui preset. It is a Yarn workspace (`patient_portal`, `frappe-ui`) and uses `yarn.lock`.
- **Node:** CI uses Node 24.
- **Tooling:** pre-commit with ruff 0.15.18 (lint and format), prettier 3.1, ESLint 10.5 flat config, pip-audit, detect-secrets, Frappe semgrep rules, commitlint (conventional commits) and semantic-release.
