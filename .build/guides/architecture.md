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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/tests/utils.py
---

This is one Frappe app (`healthcare`) that is installed on a bench alongside frappe and erpnext. It has a separate Vue front end.

**Top level**
- `healthcare/` is the Python package (the app root).
  - `hooks.py` wires everything together: `doc_events` (for example, every submit or cancel creates or deletes a Patient Medical Record; Sales Invoice, Payment Entry, Company and Patient hooks), `scheduler_events` (appointment reminders, daily status updates), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `jinja` methods, `on_login`, portal permissions and `standard_queries`.
  - `healthcare/healthcare/` is the main module. It contains `doctype/<snake_name>/` (JSON schema, Python controller, JS form script and `test_*.py` per doctype), `report/`, `page/`, `print_format/`, `web_form/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `custom_doctype/` (ERPNext overrides such as `sales_invoice.py` and `payment_entry.py`), `api/patient_portal.py` (whitelisted portal API), `utils.py` (shared billing and invoice helpers) and `auth.py`.
  - `controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
  - `regional/` holds country-specific code (for example, India ABDM).
  - `patches/v15_0`, `patches/v16_0` and `patches.txt` hold data migrations.
  - `setup.py`, `install.py`, `uninstall.py` and `after_migrate.py` handle app lifecycle.
  - `public/` holds Desk JS (`healthcare.bundle.js`, `js/*`) and the built portal assets (`public/frontend`).
  - `www/` holds the Jinja pages that host the portal (`patient_portal.html`, `patient-portal/`).
  - `tests/utils.py` holds the shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).
  - `locale/` holds translations.
- `patient_portal/` is the Vue 3 and frappe-ui SPA. It calls whitelisted methods in `healthcare.healthcare.api.patient_portal` through `createResource`, and Vite builds it into `healthcare/public/...` with the HTML entry at `healthcare/www/patient_portal.html`.
- `wiki/` holds feature design and usage docs and the upstream-sync ledger.

**Dependency direction:** `healthcare` → `erpnext` → `frappe`. Healthcare extends ERPNext doctypes through hooks and overrides and never edits them. Doctype controllers import helpers from `healthcare.healthcare.utils` and from each other by full dotted path, for example `healthcare.healthcare.doctype.patient_appointment.patient_appointment`.
