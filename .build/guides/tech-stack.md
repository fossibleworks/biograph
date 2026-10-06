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
  - crowdin.yml
---

**Backend**
- Python, `requires-python >=3.10`; ruff targets py310 and CI runs Python 3.14.
- Frappe Framework app named `healthcare`, with `required_apps = ["frappe/erpnext"]`. Payments is also installed in CI.
- Packaged with flit (`flit_core`). Extra dependencies are `responses` and `python-barcode`.
- Database: MariaDB (CI uses `mariadb:11.8`) and Redis, both managed through `bench`.
- Version is tracked in `healthcare/__init__.py` and bumped by semantic-release.

**Desk UI**
- Classic Frappe form scripts: `frappe.ui.form.on(...)`, jQuery, and `frappe.*` globals.
- They live next to each doctype (`<doctype>.js`, `<doctype>_list.js`, `_tree.js`) and in `healthcare/public/js`.
- The desk bundle is `healthcare.bundle.js`, loaded via `app_include_js`.

**Patient Portal** (`patient_portal/`)
- Vue 3, vue-router, Vite 4, and **frappe-ui** (Tailwind preset, components, `frappeRequest` resource fetcher).
- Tailwind CSS 3.4, PostCSS, feather/lucide icons, and socket.io for realtime.

**Tooling**
- Yarn workspaces at the root (`yarn.lock`).
- Python: ruff (lint and format).
- JavaScript: ESLint 10 (flat config) and Prettier.
- Security: pre-commit, pip-audit, detect-secrets, Semgrep (Frappe rules) and CodeQL.
- Commits: commitlint.
- Translations: gettext `healthcare/locale/main.pot`, managed through Crowdin.
