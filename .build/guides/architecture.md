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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

Biograph is a single Frappe app (`healthcare/`) plus a Vue SPA (`patient_portal/`).

**`healthcare/` (app package)**
- `hooks.py` is where the app plugs into Frappe and ERPNext:
  - `doc_events` on `*` (medical record on submit/cancel), Sales Invoice, Payment Entry, Company and Patient
  - `override_doctype_class` for Sales Invoice → `HealthcareSalesInvoice`
  - `scheduler_events` (appointment reminders, daily status updates)
  - `doctype_js`, jinja helpers and install/migrate hooks
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/` holds each DocType: JSON schema, controller `.py`, form `.js` and `test_<name>.py`
  - `custom_doctype/` extends ERPNext doctypes (sales_invoice, payment_entry)
  - `api/patient_portal.py` has the whitelisted endpoints the portal calls
  - other folders: `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/`, `setup/`, `utils.py` (shared billing and invoice logic)
- `controllers/` holds shared controller base classes (for example `service_request_controller.py` and `queries.py`).
- `regional/india/` holds the ABDM integration.
- `patches/v0_0|v15_0|v16_0` contain data migrations, registered in `patches.txt` under `[pre_model_sync]` / `[post_model_sync]`.
- `public/js` holds desk JS; `public/frontend` and `public/patient_portal/assets` hold built portal assets.
- `www/patient_portal.{html,py}` serves the SPA.
- `templates/`, `locale/` and `tests/` (with `HealthcareTestSuite` in `tests/utils.py`) complete the package.

**`patient_portal/`:** Vue 3 and frappe-ui. Vite builds it into `healthcare/public/patient_portal/assets`, with `healthcare/www/patient_portal.html` as the index. Data comes from frappe-ui resources that call `healthcare.healthcare.api.patient_portal.*`.

**Dependency direction:** healthcare imports from frappe and erpnext, never the other way round. ERPNext behaviour is extended only through hooks, overrides and custom fields. Upstream earthians/marley changes are cherry-picked into the fork branch `biograph-fh`.
