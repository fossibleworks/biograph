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
- Python `>=3.10`. Ruff targets `py310`, and CI runs Python **3.14**.
- **Frappe Framework** with **ERPNext**. The `payments` app is installed in CI. Each Frappe/ERPNext branch is matched to the repo branch, and fork branches fall back to `version-16`.
- Database: **MariaDB** (CI uses `mariadb:11.8`). Redis comes with bench.
- Packaging: `flit_core` (`pyproject.toml`). Runtime dependencies: `responses`, `python-barcode`.

**Frontend**
- Desk UI: plain JavaScript form scripts per doctype (`<doctype>.js`), plus `healthcare/public/js/*` bundled through `healthcare.bundle.js` (`app_include_js`).
- Patient Portal: **Vue 3**, **vue-router**, **frappe-ui** (^0.1.176), **Vite 4.4.9**, **TailwindCSS 3.4.15** with the frappe-ui preset, and feather-icons.
- Node 24 in CI. Yarn workspaces (`patient_portal`, `frappe-ui`) with `yarn.lock`.

**Tooling:** ruff (lint + format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, Codecov, CodeQL, Mergify, Crowdin (translations).
