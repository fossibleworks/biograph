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

This is a single Frappe app (`healthcare`) installed into a bench next to `frappe` and `erpnext`. It also ships a separate Vue SPA for patients.

**Top-level layout**
- `healthcare/`: the Python package (app root).
  - `hooks.py`: the wiring point for everything. It declares `doctype_js`, `override_doctype_class`, `doc_events` on ERPNext doctypes (e.g. Sales Invoice, Payment Entry), `scheduler_events` (appointment reminders, daily status updates), `standard_queries`, `jinja` methods, and `on_login`.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType with `.json` (schema), `.py` (controller class), `.js` (form script), optional `_list.js` / `_dashboard.py`, and `test_<name>.py`.
    - `custom_doctype/`: overrides and extensions of ERPNext doctypes (e.g. `sales_invoice.py`, `payment_entry.py`).
    - Desk artifacts: `report/`, `page/`, `print_format/`, `workspace/`, `dashboard_chart*/`, `number_card/`, `web_form/`.
    - `api/patient_portal.py`: `@frappe.whitelist()` endpoints used by the Vue portal.
    - `utils.py`: shared helpers such as billing items and barcodes.
  - `controllers/`: shared controller logic (e.g. `service_request_controller.py`, `queries.py`).
  - `regional/india/`: country-specific code (ABDM).
  - `setup/`, `install.py`, `after_migrate.py`, `uninstall.py`: install and migrate hooks.
  - `patches/v0_0|v15_0|v16_0/` plus `patches.txt`: data migrations.
  - `public/js/`: Desk JS bundle. `public/frontend/`: the built portal.
  - `www/`: web routes, including `patient_portal.html/.py`.
  - `tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).
- `patient_portal/`: Vue/Vite source for the patient portal. It calls the backend through frappe-ui resources (`frappeProxy`) and `api/patient_portal.py`.
- `wiki/`: fork design and usage docs.
- `.github/`: CI, release, and helper scripts.

**Dependency direction:** `healthcare` imports from `frappe` and `erpnext`, never the other way round. ERPNext behaviour is changed only through hooks (doc_events, override_doctype_class, doctype_js). DocType controllers call each other directly through their module paths, e.g. `healthcare.healthcare.doctype.patient_appointment.patient_appointment`.
