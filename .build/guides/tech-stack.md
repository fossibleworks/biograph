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
  - .github/helper/install.sh
  - yarn.lock
---

**Backend**
- Python >= 3.10 (ruff targets py310; CI runs Python 3.14), packaged with `flit_core`.
- **Frappe Framework** app `healthcare`, with **ERPNext** (required_apps) and the `payments` app. It follows Frappe and ERPNext `version-16`.
- MariaDB 11.8 (CI service) and Redis, run through `bench`.
- Python dependencies: `responses`, `python-barcode`.

**Desk frontend**
- Plain JavaScript for Frappe form scripts (`frappe.ui.form.on`, `frm.add_custom_button`, `__()`), bundled by esbuild through `healthcare/public/js/healthcare.bundle.js`. Jinja/HTML micro-templates live next to the JS.

**Patient portal**
- Vue 3, vue-router 4, **frappe-ui** (^0.1.176), Vite 4.4.9, Tailwind CSS 3.4.15 with the frappe-ui preset, and feather/lucide icons.
- Yarn workspaces: the root `package.json` declares `patient_portal` and `frappe-ui` as workspaces, and `yarn.lock` is committed.

**Tooling**
- ruff (lint and format), ESLint 10 (flat config), Prettier, and pre-commit.
- detect-secrets, pip-audit, Semgrep (Frappe rules), CodeQL.
- commitlint (conventional commits) and semantic-release.
