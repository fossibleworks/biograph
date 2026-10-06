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
  - healthcare/public/js/healthcare.bundle.js
  - healthcare/patches.txt
---

This is a single Frappe app (`healthcare`) that runs inside a bench next to `frappe`, `erpnext`, and `payments`.

**Top-level layout**
- `healthcare/`: the Python package (Frappe app root)
  - `hooks.py`: registers everything with Frappe: `doc_events` (including the wildcard `*` on_submit/on_cancel that creates medical records), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js`, `scheduler_events` (e.g. appointment reminders), and `app_include_js = healthcare.bundle.js`.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/` folders hold each DocType's `.json` schema, `.py` controller, `.js` form script, optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
    - Also here: `report/`, `page/` (patient_history, patient_progress), `dashboard_chart*`, `number_card`, `workspace`, `print_format`, `web_form`, `custom_doctype/` (overrides and extensions of ERPNext doctypes such as sales_invoice and payment_entry), `api/patient_portal.py` (whitelisted portal endpoints), `utils.py`, and `setup.py`.
  - `controllers/`: shared base controllers (`service_request_controller.py`, `queries.py`).
  - `regional/india/`: ABDM and India-specific code.
  - `patches/v0_0|v15_0|v16_0` plus `patches.txt`: data migrations.
  - `public/js`: desk JS, bundled through `healthcare.bundle.js`. `public/frontend`: built portal assets.
  - `www/`: website routes (`patient_portal.html/.py`, `patient-portal/`).
  - `tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).
  - `locale/main.pot`: translation template.
- `patient_portal/`: Vue 3 + frappe-ui SPA. It calls `healthcare.healthcare.api.patient_portal.*` whitelisted methods through frappe-ui resources, and is built into `healthcare/public` with its entry HTML at `healthcare/www/patient_portal.html`.
- `public/js`: one extra script at the repo root.
- `wiki/`: design docs and usage docs.

**How the pieces depend on each other**
- Controllers subclass `frappe.model.document.Document` and import ERPNext modules (accounts, stock) for billing and stock.
- Frappe calls into the app through hooks.
- Client JS calls server methods marked `@frappe.whitelist()` (182 in the package) with `frappe.call`.
- Background work goes through `frappe.enqueue`.

**Adding a new DocType:** create `healthcare/healthcare/doctype/<name>/` with `__init__.py`, `<name>.json`, `<name>.py`, `<name>.js`, and `test_<name>.py`, usually generated through the Frappe desk.
