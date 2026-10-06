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

## Backend
- **Python ≥3.10**. Ruff targets `py310`, and CI runs Python **3.14**. The package is built with `flit_core`.
- **Frappe Framework** (metadata-driven DocTypes) plus **ERPNext**, which is a required app. CI also installs **payments**. All three are cloned at the branch that matches the base: `develop`/`version-*`, falling back to `version-16` for fork branches such as `biograph-fh` and `goal/*`.
- **MariaDB 11.8** (the CI service) and Redis.
- Extra Python dependencies: `responses`, `python-barcode`.

## Frontend
- **Desk UI**: Frappe form scripts in plain JS (`*.js` next to each doctype, plus `healthcare/public/js/*`, bundled through `healthcare.bundle.js`) and Jinja/HTML templates.
- **Patient Portal** (`patient_portal/`): **Vue 3**, **vue-router 4**, **frappe-ui** (^0.1.176), **Tailwind CSS 3.4** (frappe-ui preset), **Vite 4.4**, feather/lucide icons and a socket.io client.
- Package manager: **Yarn** workspaces (`patient_portal`, `frappe-ui`). `yarn.lock` is committed. Node **24** in CI.

## Tooling
Ruff (lint and format), ESLint 10 (flat config), Prettier (JS/TS/Vue/CSS), pre-commit, Frappe semgrep rules, pip-audit, detect-secrets, commitlint (conventional commits), semantic-release, Codecov, CodeQL, Crowdin (translations) and Mergify.
