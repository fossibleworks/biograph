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

- **Backend:** Python 3.10 or later (`requires-python >=3.10`, ruff `target-version = py310`). CI runs on **Python 3.14**. Packaged with `flit_core`.
- **Framework:** **Frappe** with the required app **ERPNext**. CI tests against the `version-16` branches of frappe, erpnext and payments. The code follows Frappe's metadata-driven model: DocType JSON, a Python controller and a JS form script.
- **Database:** MariaDB (CI uses `mariadb:11.8`) and Redis, via `bench`.
- **Desk frontend:** plain JS form scripts that use the `frappe`, `erpnext` and `$` globals. They are bundled through `healthcare/public/js/healthcare.bundle.js` (`app_include_js`).
- **Patient Portal:** **Vue 3**, vue-router 4, **frappe-ui** (^0.1.176), Vite 4.4.9 and Tailwind CSS 3.4.15. It lives in the `patient_portal/` yarn workspace.
- **Node:** Node 24 in CI. Yarn workspaces (`yarn.lock`) at the repo root.
- **Python dependencies:** `responses`, `python-barcode`. Everything else comes from frappe and erpnext.
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, Semgrep with the Frappe rules, detect-secrets, pip-audit, commitlint, semantic-release, Codecov, Mergify and Crowdin.
