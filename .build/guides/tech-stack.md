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
  - healthcare/hooks.py
  - .github/helper/install.sh
  - crowdin.yml
  - yarn.lock
---

- **Backend:** Python >= 3.10 (ruff targets py310; CI uses Python 3.14). It is a **Frappe Framework** app and depends on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaged with `flit_core`. Runtime pip dependencies: `responses` and `python-barcode`.
- **Database:** MariaDB through the Frappe ORM and query builder (`frappe.qb`). Redis is used for the queue and cache.
- **Desk UI:** plain JavaScript form scripts per doctype (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_tree.js`) and a `healthcare.bundle.js` included via `app_include_js`. Uses Frappe globals (`frappe`, `erpnext`, jQuery, moment).
- **Patient portal:** Vue 3, vue-router 4, **frappe-ui**, Tailwind CSS 3.4 (frappe-ui preset) and Vite 4.4.9. It is a yarn workspace (`patient_portal`, `frappe-ui`).
- **Server-side templates:** Jinja (`healthcare/templates`, `www/`, print formats).
- **Tooling:** pre-commit with ruff and ruff-format, prettier, ESLint 10 (flat config), pip-audit, detect-secrets and Frappe semgrep rules. Commit messages are checked by commitlint. Releases use semantic-release.
- **i18n:** a gettext POT file (`healthcare/locale/main.pot`) synced to Crowdin.
