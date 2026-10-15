---
title: Tech Stack
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
  - .github/helper/install.sh
  - yarn.lock
---

# Tech stack

## Backend
- **Python ≥ 3.10.** `pyproject.toml` builds with `flit_core`. CI runs Python 3.14.
- **Frappe Framework** (a metadata-driven, DocType-based web framework) plus **ERPNext** as a required app. **Payments** is installed in CI.
- **MariaDB 11.8** (in the CI service) and Redis.
- Extra Python dependencies: `responses`, `python-barcode`. External HTTP calls use `requests` (ABDM).
- The version lives in `healthcare/__init__.py` (`__version__`).

## Desk frontend
- Plain JavaScript form scripts (`frappe.ui.form.on`) next to each DocType. Shared desk JS lives in `healthcare/public/js/`, bundled through `healthcare.bundle.js` (`app_include_js`).
- Jinja HTML templates for print formats, `www/` pages and the `.html` micro-templates in `public/js`.

## Patient portal SPA (`patient_portal/`)
- **Vue 3** (`<script setup>`), **vue-router**, **frappe-ui**, feather/lucide icons.
- **Vite 4.4.9** with the `frappe-ui/vite` plugin, plus **Tailwind CSS 3.4.15**, PostCSS and autoprefixer.
- Package manager: **Yarn** workspaces (root `yarn.lock`), on Node 24 in CI.

## Tooling
ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, CodeQL, commitlint, semantic-release, Mergify, Crowdin (translations) and Codecov.
