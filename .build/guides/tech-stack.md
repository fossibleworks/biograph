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
  - crowdin.yml
---

# Tech stack

- **Backend:** Python ≥3.10 (CI uses 3.14). It is a **Frappe Framework** app that depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). CI also installs the `payments` app.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM, `frappe.qb` (PyPika query builder) and `frappe.db.*`.
- **Packaging:** `flit_core` via `pyproject.toml`. The version lives in `healthcare/__init__.py`.
- **Python deps:** `responses`, `python-barcode`.
- **Desk JS:** Plain Frappe client scripts (`frappe.ui.form.on`, jQuery and Frappe globals). They are bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- **Patient Portal SPA:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 (with the frappe-ui preset), Vite 4 and feather/lucide icons. It is a Yarn workspace.
- **Node:** 24 in CI, with Yarn (`yarn.lock`).
- **Tooling:** ruff, eslint 10 (flat config), prettier, pre-commit, semgrep (Frappe rules), detect-secrets, pip-audit, commitlint and semantic-release.
- **i18n:** a gettext `.pot` file synced through Crowdin.
