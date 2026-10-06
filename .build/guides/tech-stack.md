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
  - healthcare/hooks.py
---

- **Backend:** Python ≥3.10 (CI uses 3.14) as a **Frappe** app (`healthcare`) that requires **ERPNext** and `payments`. Packaging uses `flit_core` through `pyproject.toml`. Runtime deps are `responses` and `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`, utf8mb4). Redis comes from the Frappe bench.
- **Desk UI:** Frappe desk JavaScript (form scripts per doctype, `healthcare/public/js/*.js`, bundled through `healthcare.bundle.js`) and jQuery/Frappe globals.
- **Patient Portal SPA:** **Vue 3** + **vue-router**, **frappe-ui**, **Tailwind CSS 3.4** (frappe-ui preset), built with **Vite 4**. Realtime updates use socket.io.
- **Node:** Node 24 in CI. Yarn workspaces (`patient_portal`, `frappe-ui`) with `yarn.lock`.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Frappe semgrep rules, detect-secrets, pip-audit, CodeQL, commitlint, semantic-release.
- **Supported Frappe/ERPNext lines:** `version-14`, `version-15` and `version-16`. Fork branches test against `version-16`.
