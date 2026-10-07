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
  - healthcare/hooks.py
  - yarn.lock
---

- **Backend:** Python ≥3.10 (CI uses 3.14), packaged with `flit_core`. It is a **Frappe Framework** app that requires **ERPNext** (and `payments` in CI). The database is **MariaDB** (CI uses `mariadb:11.8`). Redis is used for queue and cache.
- **Desk UI:** plain Frappe desk JavaScript: doctype `.js` controllers, `*_list.js`, `*_tree.js`, and the bundle `healthcare/public/js/healthcare.bundle.js`. It uses jQuery/Frappe globals (`frappe`, `__`, `$`, `moment`).
- **Patient Portal SPA:** **Vue 3** + **vue-router 4** + **frappe-ui**, built with **Vite 4** and styled with **Tailwind CSS 3.4** (frappe-ui preset). Icons come from feather-icons and lucide via the frappe-ui Vite plugin.
- **JS tooling:** Yarn workspaces (`yarn.lock`, workspaces `patient_portal`, `frappe-ui`) and Node 24 in CI.
- **Python deps:** `responses`, `python-barcode`. Dev requirements are in `dev-requirements.txt`.
- **Quality tooling:** ruff (lint + format), ESLint 10 flat config, Prettier, pre-commit, Semgrep (Frappe rules), CodeQL, detect-secrets, pip-audit, commitlint, semantic-release.
