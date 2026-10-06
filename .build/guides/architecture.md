---
title: Architecture
category: architecture
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Biograph is a single Frappe app (the `healthcare` Python package) installed into a bench alongside frappe, erpnext and payments.

**Top-level layout**
- `healthcare/`: the Frappe app package.
  - `hooks.py`: the integration hub. It holds `doc_events` (including a wildcard `"*"` hook that maintains Patient Medical Record on submit and cancel), hooks into ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient), `scheduler_events` (appointment reminders and daily status updates), `doctype_js` overrides, Jinja methods, and the `on_login` role-based home page.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one directory per DocType. It holds `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (form script), optional `_list.js`, `_tree.js`, `_calendar.js` and `_dashboard.py`, and `test_<name>.py`.
    - `api/patient_portal.py`: whitelisted endpoints used by the portal SPA.
    - `utils.py`: shared helpers, including invoice and billing hooks and code value helpers.
    - `report/`, `page/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, `custom_doctype/` (overrides for ERPNext doctypes such as Payment Entry and Sales Invoice) and `setup/`.
  - `controllers/`: shared controllers (for example the service request controller and queries).
  - `regional/india/abdm/`: region-specific integration.
  - `patches/` with `patches.txt`: versioned data migrations (`v0_0`, `v15_0`, `v16_0`) listed under `[pre_model_sync]` and `[post_model_sync]`.
  - `public/js/`: Desk JS bundled by `healthcare.bundle.js`.
  - `public/frontend/`: built portal assets.
  - `www/`: portal page entry points (`patient_portal.html` and `patient-portal/`).
  - `tests/utils.py`: `HealthcareTestSuite` and the `BootStrapTestData` fixtures.
  - `locale/main.pot`: translatable strings.
- `patient_portal/`: the Vue 3 and frappe-ui SPA. It calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources and builds into `healthcare/public/...` with `www/patient_portal.html` as the index.
- `public/js/`: a small root-level JS asset.
- `wiki/`: design notes, usage docs and the upstream sync ledger.

**Dependency direction:** the portal SPA calls the whitelisted Python API. DocType controllers call ERPNext (Item, Sales Invoice, Customer, Company) and other healthcare doctypes. ERPNext events flow back into healthcare through `hooks.py` `doc_events`. Business logic and validation live server-side; the PR template says so explicitly.
