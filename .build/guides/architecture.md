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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/tests/utils.py
---

The project is a single Frappe app (`healthcare`) plus a Vue SPA (`patient_portal`).

- `healthcare/hooks.py` is the integration hub. It wires `doc_events` on ERPNext doctypes (Sales Invoice, Company, Patient, and `*` for medical records), `scheduler_events` (appointment reminders, daily status and validity updates), the desk JS bundle, and the app screen.
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/` holds `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), optional `<name>_list.js` / `_calendar.js`, and `test_<name>.py`. There are about 139 doctypes.
  - `report/`, `dashboard_chart_source/`, `number_card/`, `page/`, `print_format/`, `web_form/`, and `workspace/` are standard Frappe artifacts.
  - `api/patient_portal.py` holds the whitelisted endpoints the Vue portal calls.
  - `custom_doctype/` holds overrides of ERPNext doctypes (sales_invoice, payment_entry).
  - `utils.py` holds shared server helpers, including invoice hooks.
- `healthcare/controllers/` holds shared controllers (`service_request_controller.py`, `queries.py` for link-field queries).
- `healthcare/regional/india/` holds ABDM integrations.
- `healthcare/patches/{v0_0,v15_0,v16_0}` holds data migrations, registered in `healthcare/patches.txt`.
- `healthcare/setup.py`, `install.py`, `uninstall.py`, and `after_migrate.py` handle install and lifecycle.
- `healthcare/public/js/` holds shared desk JS (observation widgets, healthcare notes, orders, quick entry).
- `healthcare/www/patient_portal.*` is the Jinja host page for the portal SPA.
- `patient_portal/` is the Vite/Vue source. It builds into `healthcare/public/...` and calls the backend through frappe-ui resources (proxied by `frappeProxy`).
- `healthcare/tests/utils.py` defines the shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).

Dependency direction: `healthcare` → `erpnext` → `frappe`. The portal → `healthcare.healthcare.api.*` over HTTP.
