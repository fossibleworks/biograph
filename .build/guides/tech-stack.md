---
title: Tech stack
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
  - .github/workflows/ci.yml
  - .releaserc
  - yarn.lock
---

- **Backend:** Python ≥3.10 (`target-version py310`; CI runs Python 3.14), as a **Frappe** app on top of **ERPNext**. Packaged with `flit_core`. Runtime pip dependencies: `responses`, `python-barcode`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM (`frappe.get_doc`, `frappe.get_all`, `frappe.db.*`).
- **Desk UI:** Frappe form, list and calendar JS in each doctype folder (`<doctype>.js`, `<doctype>_list.js`, `<doctype>_calendar.js`). Shared scripts live in `healthcare/public/js` and are bundled via `app_include_js = "healthcare.bundle.js"`.
- **Patient portal:** Vue 3 + vue-router + **frappe-ui** (`createResource`), Vite 4.4.9, Tailwind CSS 3.4.15 (frappe-ui preset), feather/lucide icons.
- **Package management:** Yarn workspaces (`yarn.lock`; workspaces `patient_portal`, `frappe-ui`). Node 24 in CI.
- **Tooling:** ruff 0.15.18, ESLint 10 (flat config), Prettier, pre-commit, Semgrep (Frappe rules), detect-secrets, pip-audit, CodeQL, commitlint, semantic-release.
- **Supported versions:** release branches `version-14`, `version-15` and `version-16`. Patches are organised under `v0_0`, `v15_0` and `v16_0`.
