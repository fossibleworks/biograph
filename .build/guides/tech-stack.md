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
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - yarn.lock
---

**Backend:** Python ≥3.10, with ruff targeting py310. CI runs Python 3.14. This is a **Frappe Framework** app that depends on **ERPNext**. It is packaged with `flit_core`, and its runtime deps are `responses` and `python-barcode`. CI uses MariaDB 11.8 as the database.

**Desk frontend:** Frappe Desk JavaScript (jQuery and the `frappe.ui` globals). It is bundled through `healthcare/public/js/healthcare.bundle.js` and loaded via `app_include_js`. Some forms are extended with `doctype_js` in `hooks.py`.

**Patient portal:** Vue 3 (`<script setup>`), vue-router 4, and **frappe-ui** (`createResource`, `Tabs`, `Dialog`). It is built with Vite 4.4.9, Tailwind CSS 3.4.15 (frappe-ui preset), PostCSS/autoprefixer, and feather/lucide icons. Yarn workspaces are used (`patient_portal`, `frappe-ui`), with `yarn.lock` at the root. Node 24 runs in CI.

**Tooling:**
- ruff (lint and format)
- ESLint 10 (flat config) and Prettier
- pre-commit, pip-audit, detect-secrets
- Semgrep with the Frappe rules
- CodeQL
- commitlint with conventional commits
- semantic-release
