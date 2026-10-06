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
  - patient_portal/tailwind.config.js
  - healthcare/hooks.py
  - .github/helper/install.sh
  - .github/workflows/ci.yml
---

- **Backend:** Python ≥3.10 (`requires-python`, ruff `target-version = py310`; CI runs Python 3.14). It is a **Frappe app** that depends on **ERPNext** and **payments**. It builds with `flit_core`, and its runtime deps are `responses` and `python-barcode`.
- **Data:** MariaDB/MySQL through the Frappe ORM (CI uses a mysql service). Schema is defined as DocType JSON.
- **Desk UI:** plain JavaScript form scripts per doctype, plus `healthcare/public/js/*` bundled through `healthcare.bundle.js` (`app_include_js`). The frappe, erpnext, and jQuery globals are available.
- **Patient Portal:** Vue 3, vue-router 4, **frappe-ui**, Tailwind CSS 3.4 (with the frappe-ui preset), Vite 4.4, and feather-icons. It is a yarn workspace (`patient_portal`).
- **Node:** v24 in CI, managed with yarn (`yarn.lock`).
- **Target versions:** Frappe/ERPNext `version-16`. The fork branches `biograph-fh` and `goal/*` test against `version-16`.
