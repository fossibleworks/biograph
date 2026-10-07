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
  - healthcare/hooks.py
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - yarn.lock
  - .github/workflows/ci.yml
  - crowdin.yml
---

**Backend:** Python ≥ 3.10. Ruff targets py310 and CI runs Python 3.14. The backend is a **Frappe Framework** app with a hard dependency on **ERPNext** (`required_apps = ["frappe/erpnext"]`) and is packaged with `flit_core`. Its own runtime deps are only `responses` and `python-barcode`. Everything else comes from the bench. The database is MariaDB (CI uses `mariadb:11.8`).

**Desk frontend:** plain JS form scripts per doctype (`<doctype>.js`), plus shared scripts in `healthcare/public/js`, bundled through `healthcare.bundle.js` by Frappe's build. They use the `frappe`, `erpnext` and jQuery globals.

**Patient portal:** **Vue 3** + **vue-router 4** + **frappe-ui** (^0.1.176), built with **Vite 4.4.9**. Styling is **Tailwind CSS 3.4.15** with the frappe-ui Tailwind preset and PostCSS/autoprefixer. Icons come from feather-icons and lucide (via the frappe-ui Vite plugin). The package manager is **Yarn** (root `yarn.lock`, workspaces `patient_portal`, `frappe-ui`).

**Tooling:** pre-commit, ruff (lint + format), ESLint 10 (flat config), Prettier, pip-audit, detect-secrets, Frappe semgrep rules, commitlint, semantic-release, Codecov, Crowdin (translations), and Mergify.
