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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

This is a single Frappe app named `healthcare`, laid out the standard Frappe way.

- `healthcare/hooks.py` is the integration hub. Everything wires into Frappe and ERPNext here:
  - `doc_events`: a wildcard on_submit/on_cancel hook creates the Patient Medical Record. There are also hooks on Sales Invoice, Payment Entry, Company and Patient.
  - `override_doctype_class`: Sales Invoice is replaced by `HealthcareSalesInvoice`.
  - `doctype_js`, `scheduler_events` (appointment reminders and daily status updates), `jinja` methods, `has_website_permission`, `standard_queries`, `on_login`, and install, migrate and uninstall hooks.
- `healthcare/healthcare/` is the main module:
  - `doctype/`: ~139 doctypes, one folder each, holding the JSON definition, Python controller, JS form script and `test_*.py`.
  - `custom_doctype/`: overrides and extensions of ERPNext doctypes such as Sales Invoice and Payment Entry.
  - Also: `report/` (script reports), `page/` (patient_history, patient_progress), `web_form/`, `dashboard_chart*`, `number_card`, `workspace`, `print_format`.
  - `utils.py` holds shared billing and invoice logic. `api/patient_portal.py` holds the whitelisted endpoints for the SPA.
- `healthcare/controllers/` holds shared controllers, for example `service_request_controller.py` and link `queries.py`.
- `healthcare/regional/india/` holds the ABDM integration.
- `healthcare/patches/` (`v0_0`, `v15_0`, `v16_0`) holds data migrations, registered in `healthcare/patches.txt`.
- `healthcare/public/js/` holds desk JS shared across forms and is bundled via `healthcare.bundle.js`.
- `patient_portal/` is the Vue SPA source. Its built output goes to `healthcare/public/frontend/` (and `healthcare/public/patient_portal/assets`). It is served by `healthcare/www/patient-portal` / `patient_portal.html|py` and calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui's `frappeRequest`.
- `healthcare/tests/utils.py` holds the shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).

**Dependency direction:** healthcare → ERPNext → Frappe. Business rules live server-side in doctype controllers and `utils.py`. JS form scripts call whitelisted Python methods via `frappe.call`.
