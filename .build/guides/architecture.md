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
  - healthcare/tests/utils.py
---

This is a single Frappe app (`healthcare`) installed into a bench next to `frappe`, `erpnext`, and `payments`.

**Layout:**
- `healthcare/hooks.py`: the app's wiring point.
  - `doc_events`: wildcard on_submit/on_cancel creates Patient Medical Records; Sales Invoice validate/submit/cancel hooks call into `healthcare.healthcare.utils`.
  - `override_doctype_class`: Sales Invoice → `HealthcareSalesInvoice`.
  - `scheduler_events`: appointment reminders, daily status and fee-validity updates.
  - Also `standard_queries`, `app_include_js`.
- `healthcare/healthcare/` is the Frappe module:
  - `doctype/<snake_name>/`: `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (Desk form script), optional `_list.js`/`_dashboard.py`, and `test_<name>.py`.
  - `api/patient_portal.py`: `@frappe.whitelist()` endpoints the portal calls.
  - `custom_doctype/`: extensions of ERPNext doctypes (Sales Invoice, Payment Entry).
  - `report/`, `page/` (patient_history, patient_progress), `dashboard_chart*`, `number_card`, `workspace`, `print_format`, `web_form`, `setup/`.
  - `utils.py`: shared billing and invoice helpers.
- `healthcare/controllers/`: shared controllers, e.g. `service_request_controller.py` and `queries.py`.
- `healthcare/regional/india/`: regional (ABDM) code.
- `healthcare/patches/{v0_0,v15_0,v16_0}` are registered in `healthcare/patches.txt`. `install.py`, `after_migrate.py`, and `uninstall.py` are lifecycle hooks.
- `healthcare/public/js`: Desk bundle (`healthcare.bundle.js`) and shared form utilities.
- `healthcare/www/patient_portal.{html,py}`: the web route that serves the portal SPA.
- `patient_portal/`: Vue/Vite SPA.
  - Calls whitelisted Python methods through frappe-ui `createResource`.
  - Its build output goes into `healthcare/public/...` and `healthcare/www/patient_portal.html`.
- `healthcare/tests/`: shared test bootstrap (`HealthcareTestSuite`, master-data factories).
- `wiki/`: design and usage docs plus the upstream-sync ledger.

**Dependency direction:** `healthcare` → `erpnext` → `frappe`. Imports follow that order (see the isort sections). Patient Portal → whitelisted APIs → doctype controllers.
