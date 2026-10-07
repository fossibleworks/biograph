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
  - yarn.lock
---

## Backend

- **Python**, on the **Frappe framework** with **ERPNext** as a required app (`required_apps = ["frappe/erpnext"]`). The `payments` app is installed in CI.
- Packaging uses `flit_core` via `pyproject.toml`. `requires-python >=3.10` and ruff targets `py310`, but CI runs **Python 3.14**.
- Frappe and ERPNext branches track `version-16` (CI falls back to version-16 for fork branches). Older `version-14` and `version-15` release lines also exist.
- Database is **MariaDB**, with Redis. Runtime deps include `python-barcode` and `responses`.

## Desk frontend

- Frappe desk JavaScript is plain JS against the `frappe` and `cur_frm` globals. It lives in `healthcare/public/js` and per-doctype `*.js` files, and is bundled via `healthcare.bundle.js`.

## Patient portal

- **Vue 3**, **vue-router 4**, **frappe-ui** (`createResource`), **Tailwind CSS 3.4** with the frappe-ui preset, and **Vite 4.4**.
- Yarn workspaces are used: the root `package.json` has workspaces `patient_portal` and `frappe-ui`, and `yarn.lock` is committed.

## Tooling

ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), pip-audit, detect-secrets, commitlint, semantic-release, Mergify, Codecov and CodeQL.
