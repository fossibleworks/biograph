---
title: Tech Stack
category: tech-stack
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - pyproject.toml
  - package.json
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - healthcare/__init__.py
---

# Tech stack

- **Backend:** Python ≥3.10 (CI runs on 3.14), using the **Frappe framework** with **ERPNext** as a required app. Packaging uses `flit_core` (`pyproject.toml`), and the version is kept in `healthcare/__init__.py` (`__version__ = "16.0.8"`).
  - Python dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB (CI runs `mariadb:11.8`). Redis is used for Frappe cache and queues.
- **Desk UI:** Frappe Desk client scripts written in plain JS: `frappe.ui.form.on`, `frappe.call`, and `__()` for i18n.
  - These are bundled through `healthcare/public/js/healthcare.bundle.js`, which `app_include_js` loads.
- **Patient Portal SPA:** Vue 3, vue-router 4 and **frappe-ui**, built with Vite 4 and styled with Tailwind CSS 3 (frappe-ui preset). Icons come from feather-icons and lucide.
  - It is a Yarn workspace (`patient_portal`).
  - The built output goes to `healthcare/public/patient_portal/assets`, and the HTML entry is `healthcare/www/patient_portal.html`.
- **Tooling:** Node 24 in CI, Yarn (`yarn.lock`), pre-commit, ruff, ESLint 10 (flat config), Prettier, Semgrep (frappe rules), detect-secrets, pip-audit, commitlint, and semantic-release.
- **Frappe branches targeted:** `develop` and `version-14/15/16`. Fork branches such as `biograph-fh` and `goal/*` are tested against Frappe `version-16`.
