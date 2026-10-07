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
  - .github/workflows/ci.yml
  - yarn.lock
---

- **Backend:** Python ≥3.10. Ruff targets py310; CI runs Python 3.14. This is a **Frappe Framework** app (package `healthcare`, built with `flit_core`) that depends on **ERPNext** and the `payments` app. Runtime dependencies are `responses` and `python-barcode`.
- **Database/infra:** MariaDB (utf8mb4) and Redis, run through `bench`. PDF printing uses wkhtmltopdf.
- **Desk UI:** plain JavaScript Frappe form scripts (`frappe.ui.form.on`), one `<doctype>.js` per DocType. They are bundled through `healthcare/public/js/healthcare.bundle.js`. Jinja HTML templates are used for print formats and web views.
- **Patient Portal:** Vue 3, vue-router, **frappe-ui**, Tailwind CSS 3.4 (frappe-ui preset), Vite 4, and feather/lucide icons. It lives in a yarn workspace (`patient_portal`).
- **Tooling:** Node 24 in CI, yarn workspaces, ESLint 10 (flat config), Prettier, Ruff (lint and format), pre-commit, Semgrep with Frappe rules, detect-secrets, pip-audit, CodeQL, commitlint, and semantic-release.
