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
  - healthcare/controllers/service_request_controller.py
---

This is a standard **Frappe app** layout. The Python package is `healthcare/` and the Frappe module is `healthcare/healthcare/`.

- `healthcare/hooks.py` is the integration hub. It registers:
  - `doc_events`, including `"*"` handlers that create, update and delete medical records on submit, cancel and update-after-submit, plus Sales Invoice hooks
  - `scheduler_events` (appointment reminders on `all`; daily status, validity and billing jobs)
  - jinja methods, `doctype_js` overrides for ERPNext doctypes, and `on_login`
- `healthcare/healthcare/doctype/<snake_name>/` holds one folder per DocType (about 139):
  - `<name>.json` is the schema
  - `<name>.py` is the controller (a `Document` subclass with `validate`/`on_submit`… plus `@frappe.whitelist()` functions)
  - `<name>.js` is the form script; `<name>_list.js` and `_calendar.js` are optional
  - `test_<name>.py` holds the tests
- `healthcare/healthcare/{report,dashboard_chart_source,number_card,workspace,page,print_format,web_form,custom_doctype}` hold the standard Frappe artifacts. `custom_doctype/` overrides ERPNext Sales Invoice and Payment Entry.
- `healthcare/healthcare/api/patient_portal.py` is the whitelisted API used by the Vue portal.
- `healthcare/controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/healthcare/utils.py` holds cross-doctype helpers such as billing items and barcodes.
- `healthcare/regional/india` holds region-specific logic (ABDM).
- `healthcare/patches/v0_0|v15_0|v16_0` are migrations, registered in `healthcare/patches.txt`.
- `healthcare/setup.py`, `install.py` and `after_migrate.py` handle install and seed data.
- `healthcare/public/js` holds desk JS (the bundle plus shared widgets).
- `patient_portal/` is the Vue SPA. Its `vite.config.js` writes the build to `healthcare/public/patient_portal/assets` and the HTML to `healthcare/www/patient_portal.html`, which `healthcare/www/patient_portal.py` serves.
- `healthcare/tests/utils.py` holds shared test bootstrap (`BootStrapTestData`, `HealthcareTestSuite`).

**How calls flow:**
- Desk JS calls the server with `frappe.call({method: "healthcare.healthcare.doctype..."})`.
- The portal uses frappe-ui `createResource` against `healthcare.healthcare.api.patient_portal.*`.
- Controllers import each other directly by full dotted path, for example `from healthcare.healthcare.doctype.fee_validity.fee_validity import ...`, and they import ERPNext modules.
