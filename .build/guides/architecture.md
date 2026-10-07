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
  - healthcare/controllers/service_request_controller.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/src/patient_portal.js
  - healthcare/patches.txt
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This is one Frappe app (`healthcare`) that installs into a bench next to `frappe`, `erpnext` and `payments`.

**Top-level layout**
- `healthcare/`: the Python package (the app root).
  - `hooks.py`: the integration contract with Frappe and ERPNext. It declares `doc_events` (Sales Invoice, Payment Entry, Company, Patient, and wildcard `*` submit/cancel hooks that build Patient Medical Records), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `scheduler_events` (appointment reminders, daily status updates), jinja methods, portal permissions, `standard_queries`, and install/migrate hooks.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType containing `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (desk form script), optional `_list.js`/`_dashboard.py`, and `test_<name>.py`.
    - `custom_doctype/`: overrides and hooks for ERPNext doctypes (sales_invoice, payment_entry).
    - `api/patient_portal.py`: whitelisted endpoints used by the Vue portal.
    - `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*`, `number_card/`, `module_onboarding/`: standard Frappe artefacts.
    - `utils.py`: shared billing and service helpers (large, about 1.9k lines).
    - `setup/`: setup and seed logic, for example patient duplicate check rules.
  - `controllers/`: shared base controllers (`service_request_controller.py`, `queries.py`).
  - `regional/india/`: ABDM integration.
  - `patches/` + `patches.txt`: data migrations under `v0_0`, `v15_0`, `v16_0`, split into `[pre_model_sync]` and `[post_model_sync]`.
  - `public/js`: desk JS bundle. `public/frontend`: built portal assets.
  - `www/`: portal page routes (`patient_portal.py/html`, `patient-portal`).
  - `tests/utils.py`: `HealthcareTestSuite` and the `BootStrapTestData` fixtures.
- `patient_portal/`: the Vue 3 SPA source. It calls the backend through frappe-ui `frappeRequest` (whitelisted methods) and a socket.io client (`socket.js`).
- `public/js`: a small set of extra root-level JS.
- `wiki/`: design docs, usage docs and the upstream sync ledger.

**Dependency direction:** `healthcare` depends on `frappe` and `erpnext` (for example `erpnext.tests.utils`, accounts and stock doctypes) and plugs into ERPNext through hooks. ERPNext never imports healthcare. Doctypes call each other directly by importing functions from sibling controller modules. Business logic and validation live server-side, in DocType controllers and whitelisted functions. JS handles UI flow only.
