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
---

Monorepo for one Frappe app plus a Vue SPA:

- `healthcare/` is the Frappe app package.
  - `hooks.py` wires everything to Frappe/ERPNext. It holds `doc_events` (a global `*` on_submit/on_cancel hook that creates medical records, plus Sales Invoice, Payment Entry, Company and Patient hooks), `scheduler_events` (appointment reminders, daily status updates), `doctype_js` overrides and `app_include_js`.
  - `healthcare/healthcare/` is the main module.
    - `doctype/<snake_name>/` holds one folder per DocType: `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (form script), optional `_list.js`, `_dashboard.py` and `test_<name>.py`.
    - Also: `custom_doctype/` (ERPNext doc extensions such as sales_invoice and payment_entry), `api/patient_portal.py` (whitelisted endpoints for the portal), `utils.py` (shared billing and invoice helpers), `report/`, `page/`, `dashboard_chart_source/`, `workspace/`, `print_format/`, `web_form/`, `setup/`.
  - `controllers/` holds shared controllers and queries (e.g. `service_request_controller.py`, `queries.py`).
  - `regional/india/abdm` holds the ABDM integration.
  - `patches/` (v0_0, v15_0, v16_0) is listed in `patches.txt` under `[pre_model_sync]` and `[post_model_sync]`.
  - `www/` holds `patient_portal.html` and `.py` (the Jinja shell for the SPA).
  - `public/js` holds desk JS. `public/frontend` holds built portal assets.
  - `tests/utils.py` holds `HealthcareTestSuite` and the `BootStrapTestData` fixtures.
- `patient_portal/` is the Vue SPA. It calls the backend through frappe-ui `createResource` against `healthcare.healthcare.api.patient_portal.*` whitelisted methods and builds into `healthcare/public/...`.
- `wiki/` holds design docs and the upstream sync ledger.

**Dependency direction:** ERPNext and Frappe are platform dependencies. Biograph extends ERPNext doctypes through hooks and custom_doctype modules, never by editing ERPNext. The portal depends only on whitelisted API methods.
