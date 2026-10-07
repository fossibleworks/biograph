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
---

This is one Frappe app (`healthcare/`) plus a standalone Vue SPA (`patient_portal/`).

**`healthcare/` (app package)**
- `hooks.py` is the integration hub. It holds `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, …), `override_doctype_class`, `scheduler_events` (appointment reminders every run; daily status, fee-validity, IP billing and medication-expiry jobs) and `app_include_js`.
- `healthcare/healthcare/` is the module:
  - `doctype/<snake_name>/` folders, each with `.json` schema, `.py` controller (a `Document` subclass), `.js` form script and `test_<name>.py`.
  - `custom_doctype/` holds overrides of ERPNext doctypes (sales_invoice, payment_entry).
  - Also `report/`, `page/`, `print_format/`, `web_form/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `setup/`.
  - `utils.py` holds shared billing and helper logic.
  - `api/patient_portal.py` is the whitelisted API used by the portal.
- `controllers/` holds cross-doctype base logic (`service_request_controller.py`, `queries.py` link-field queries).
- `patches/` (`v0_0`, `v15_0`, `v16_0`) is registered in `patches.txt` under `[pre_model_sync]` / `[post_model_sync]`.
- `regional/`, `templates/`, `www/` (portal page `patient_portal.html/.py`), `locale/main.pot`, `tests/utils.py` (shared test bootstrap).

**`patient_portal/`** is a Vite build that outputs to `healthcare/public/frontend/assets`, with its index HTML at `healthcare/www/patient_portal.html`. It calls backend methods through frappe-ui `createResource` (proxied to Frappe).

**Dependency direction:** the portal calls `healthcare.healthcare.api.*` and other whitelisted methods. Doctype controllers import each other and ERPNext (`erpnext.*`). ERPNext doctypes call back into healthcare only through `hooks.py` doc_events and overrides. Business logic and validation belong server-side in controllers.
