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
  - .github/helper/install.sh
  - yarn.lock
---

- **Backend:** Python ≥3.10. Ruff targets py310 and CI runs Python 3.14. This is a **Frappe Framework** app (`healthcare`) that requires **ERPNext** (plus `payments` in CI). The version-16 branch line is the target. The package builds with `flit_core`, and the version lives in `healthcare/__init__.py`.
- **Database:** MariaDB (CI uses `mariadb:11.8`), accessed through the Frappe ORM (`frappe.get_doc`, `frappe.db.*`, `frappe.qb`) and some raw `frappe.db.sql`.
- **Desk UI:** Frappe client scripts in plain JavaScript (`<doctype>.js`, `_list.js`, `_tree.js`, `_calendar.js`), bundled through `healthcare/public/js/healthcare.bundle.js`. Uses jQuery and Frappe globals.
- **Patient Portal:** **Vue 3** + **vue-router** + **frappe-ui** (`createResource`), built with **Vite 4** and styled with **Tailwind CSS 3.4** through the frappe-ui Tailwind preset. Icons are feather-icons and lucide.
- **Node tooling:** Yarn workspaces (`yarn.lock`), Node 24 in CI.
- **Python deps:** `responses`, `python-barcode`, and the dev requirements in `dev-requirements.txt`.
- **Background jobs:** Frappe RQ via `frappe.enqueue` and `scheduler_events` in hooks.
