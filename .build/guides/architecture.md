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
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/tests/utils.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Architecture

This is a single Frappe app (`healthcare`) installed into a bench next to `frappe`, `erpnext` and `payments`.

## Top-level layout
- `healthcare/`: the Python package (app root).
  - `hooks.py`: the app's wiring. It sets `doc_events` (e.g. `*` on_submit/on_cancel creates or deletes Patient Medical Records; Sales Invoice, Payment Entry, Company and Patient hooks), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `scheduler_events` (appointment reminders, daily status and validity updates), `doctype_js` and `app_include_js`.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType holding `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (form script), optional `<name>_list.js`/`_calendar.js`, and `test_<name>.py`.
    - `api/patient_portal.py`: `@frappe.whitelist()` endpoints for the portal.
    - `custom_doctype/`: overrides and hooks for ERPNext doctypes (Sales Invoice, Payment Entry).
    - Other directories: `report/`, `page/`, `dashboard_chart*/`, `number_card/`, `print_format/`, `workspace/`, `web_form/`, `setup/`.
    - `utils.py`: shared billing and invoice helpers that hooks call.
  - `controllers/`: shared controller logic (`service_request_controller.py`) and link-field `queries.py`.
  - `regional/india/abdm`: country-specific integration.
  - `patches/` + `patches.txt`: data migrations, split into `[pre_model_sync]` and `[post_model_sync]` and versioned `v0_0`, `v15_0`, `v16_0`.
  - `public/js`: desk JS bundle. `public/frontend`: built portal assets.
  - `www/`: website routes (`patient_portal.html`, `patient-portal/`).
  - `tests/utils.py`: `HealthcareTestSuite` + `BootStrapTestData`.
  - `locale/main.pot`: translations.
- `patient_portal/`: Vue 3 SPA source. It calls the whitelisted Python API through frappe-ui `createResource`. Vite builds it into `healthcare/public/...`, and it is served via `healthcare/www/patient_portal.html`.
- `wiki/`: design and usage docs and the upstream-sync ledger.
- `.github/`: CI workflows and helper scripts.

## Dependency direction
- The patient portal calls only `healthcare.healthcare.api.patient_portal`.
- Doctype controllers import from `healthcare.healthcare.utils`, `healthcare.controllers` and ERPNext modules.
- ERPNext documents call back into healthcare only via `hooks.py`.
- Business logic and validation live server-side in doctype controllers (stated in the PR template).
