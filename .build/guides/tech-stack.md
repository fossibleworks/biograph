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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - patient_portal/tailwind.config.js
  - .github/workflows/ci.yml
  - yarn.lock
---

- **Backend:** Python >= 3.10 (ruff targets `py310`; CI runs Python 3.14). It is a **Frappe Framework** app with a hard dependency on **ERPNext** (`required_apps = ["frappe/erpnext"]`). Packaging uses `flit_core`. Runtime Python dependencies are `responses` and `python-barcode`.
- **Database:** MariaDB. CI uses `mariadb:11.8`. Data is modelled as Frappe DocTypes (JSON metadata plus a Python controller plus an optional JS form script).
- **Desk frontend:** plain Frappe form scripts in JavaScript (`frappe.ui.form.on`, jQuery, `frappe.call`). They are bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- **Patient Portal SPA:** **Vue 3**, vue-router 4, **frappe-ui** (^0.1.176), **Tailwind CSS 3.4** with the frappe-ui preset, **Vite 4.4**, feather/lucide icons, and socket.io via `socket.js`.
- **Node tooling:** Node 24 in CI. The root `package.json` is a Yarn workspace (`patient_portal`, `frappe-ui`) with `yarn.lock`. Linting uses ESLint 10 flat config and Prettier.
- **Quality and security:** pre-commit, ruff (lint and format), ESLint, Prettier, pip-audit, detect-secrets, Frappe semgrep rules, CodeQL, commitlint and semantic-release.
- **Release branches:** the fork's default branch is `biograph-fh`. Upstream release branches are `version-14`, `version-15` and `version-16`.
