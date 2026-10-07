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
  - healthcare/healthcare/utils.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/tests/utils.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This is a single Frappe app (`healthcare/`) that installs into a bench alongside frappe, erpnext and payments.

**Layout**
- `healthcare/hooks.py` is the integration point with Frappe and ERPNext:
  - `doc_events`: a `*` handler on submit, cancel and update-after-submit creates and updates Patient Medical Records. There are also hooks on Sales Invoice, Payment Entry, Company and Patient.
  - `scheduler_events`: appointment reminders and daily status updates (appointment, fee validity, inpatient billables, expired medication requests).
  - `doctype_js` overrides and `app_include_js`.
- `healthcare/healthcare/` is the main module.
  - `doctype/<snake_name>/` holds one folder per DocType: `<name>.json` schema, `<name>.py` controller (a `Document` subclass), `<name>.js` form script, optional `_list.js`, `_calendar.js` and `_dashboard.py`, and `test_<name>.py`.
  - There are also `report/`, `page/` (patient_history, patient_progress), `dashboard_chart*`, `number_card`, `workspace`, `print_format`, `web_form`, `setup/`, `api/patient_portal.py`, `custom_doctype/` (hooks into ERPNext Sales Invoice and Payment Entry), and a large shared `utils.py` (about 1.9k lines).
- `healthcare/controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/abdm` holds country-specific integration.
- `healthcare/patches/{v0_0,v15_0,v16_0}` holds data migrations, registered in `healthcare/patches.txt` under `[pre_model_sync]` and `[post_model_sync]`.
- `healthcare/public/js` holds Desk JS (bundle, observation widgets, clinical note UI, quick entry).
- `healthcare/www/patient_portal.{html,py}` is the server-rendered shell for the SPA.
- `patient_portal/` holds the Vue SPA source. It calls whitelisted methods in `healthcare/healthcare/api/patient_portal.py` through frappe-ui resources and socket.io (`socket.js`).
- `healthcare/tests/utils.py` holds `HealthcareTestSuite` (extends `ERPNextTestSuite`) and `BootStrapTestData` master-data fixtures.

**Call flow:** Desk forms call `@frappe.whitelist()` controller methods. Controllers use `frappe.get_doc` and `frappe.db` and create ERPNext documents (Sales Invoice, Customer). ERPNext doc events call back into `healthcare.healthcare.utils` and `custom_doctype`. Business logic and validation live on the server, as the PR template requires.
