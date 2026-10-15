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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

Biograph is a single Frappe app, `healthcare`, plus a separate Vue SPA.

**Top level**
- `healthcare/` is the Python package and Frappe app root:
  - `hooks.py` wires everything into Frappe: `doc_events` on ERPNext DocTypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical-record sync), `scheduler_events` (appointment reminders, daily status updates), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js`, jinja methods, website permissions, and install/migrate hooks.
  - `healthcare/healthcare/` is the Frappe module **Healthcare**. It contains `doctype/<snake_name>/` (`.json` schema, `.py` controller, `.js` form script, `test_*.py`), `report/`, `page/`, `dashboard_chart_source/`, `number_card/`, `workspace/`, `web_form/`, `print_format/`, `custom_doctype/` (ERPNext DocType extensions), `api/patient_portal.py` (whitelisted portal API), `setup/`, and a large shared `utils.py`.
  - `controllers/` holds cross-DocType base logic (`service_request_controller.py`, `queries.py`).
  - `regional/india/abdm/` is country-specific integration.
  - `patches/` and `patches.txt` are versioned data migrations (`v15_0`, `v16_0`, …).
  - `public/js/` holds desk JS assets bundled via `healthcare.bundle.js`. `public/frontend/` holds built portal assets.
  - `www/` serves the portal page (`patient_portal.html` / `.py`). `templates/` holds Jinja pages.
  - `locale/main.pot` holds translatable strings.
- `patient_portal/` is the Vue 3 SPA. It calls whitelisted methods in `healthcare.healthcare.api.patient_portal` through the frappe-ui proxy and builds into the app's public assets.
- `wiki/` holds design and usage docs for larger features.

**Dependency direction:** `healthcare` depends on `frappe` and `erpnext`; never the reverse. ERPNext behaviour is extended only through hooks (`doc_events`, `override_doctype_class`, custom fields in patches/setup), never by editing ERPNext. Business logic lives in DocType controllers and `utils.py`. JS form scripts call server methods marked `@frappe.whitelist()`.
