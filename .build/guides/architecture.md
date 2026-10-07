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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/src/socket.js
  - healthcare/patches.txt
---

This is a single Frappe app. `healthcare/` is the Python package and also the app root, following the standard Frappe layout.

- `healthcare/hooks.py`: the integration hub. It registers:
  - `doc_events`: a wildcard `*` on_submit/on_cancel hook that maintains Patient Medical Record history, plus hooks on ERPNext **Sales Invoice**, **Payment Entry**, **Company** and **Patient**.
  - `override_doctype_class`: `Sales Invoice` → `HealthcareSalesInvoice`.
  - `scheduler_events`: appointment reminders (`all`); daily appointment status, fee validity, inpatient billables and expired medication requests.
  - `app_include_js`.
- `healthcare/healthcare/`: the main module.
  - `doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), an optional `<name>_list.js` / `_dashboard.py`, and `test_<name>.py`.
  - `report/`, `page/`, `dashboard_chart_source/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`: other Frappe metadata.
  - `custom_doctype/`: extensions of ERPNext doctypes (sales_invoice, payment_entry).
  - `api/patient_portal.py`: `@frappe.whitelist()` endpoints used by the portal SPA.
  - `utils.py`: a large shared module covering billing/invoicing helpers, service-unit tree setup and code values.
- `healthcare/controllers/`: shared controllers (e.g. `service_request_controller.py`, `queries.py`).
- `healthcare/regional/`: country-specific code (e.g. India ABDM).
- `healthcare/patches/{v0_0,v15_0,v16_0}` + `healthcare/patches.txt`: data migrations, run in the order listed.
- `healthcare/www/patient_portal.{html,py}`: the Jinja host page for the SPA.
- `patient_portal/`: the Vue SPA source. It calls whitelisted Python methods via frappe-ui `createResource` and receives realtime updates over socket.io (`src/socket.js`). Built output lands under `healthcare/public/`.
- `healthcare/tests/utils.py`: the shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).

**Dependency direction:** healthcare depends on frappe and erpnext. Nothing upstream depends on healthcare. The portal depends only on the whitelisted API.
