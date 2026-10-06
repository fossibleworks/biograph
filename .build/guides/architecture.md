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
  - healthcare/controllers/service_request_controller.py
---

The repo is a single Frappe app (`healthcare/`) plus a Vue SPA (`patient_portal/`).

**`healthcare/` (Python package / Frappe app)**
- `hooks.py`: the integration point with Frappe and ERPNext. It holds `doc_events` (a wildcard `on_submit`/`on_cancel` that maintains Patient Medical Record, and Sales Invoice validate/submit/cancel hooks), `scheduler_events` (appointment reminders, daily status updates, fee validity, inpatient billables, medication request expiry), `doctype_js` overrides for ERPNext forms, jinja methods and `on_login`.
- `healthcare/healthcare/`: the main module.
  - `doctype/<snake_name>/`: about 139 DocTypes. Each folder holds `<name>.json` (the schema), `<name>.py` (the controller), `<name>.js` (the form script), optional `_list.js`/`_dashboard.py`, and `test_<name>.py`.
  - `api/patient_portal.py`: whitelisted endpoints the portal SPA calls (frappe.qb queries).
  - `custom_doctype/`: overrides of ERPNext doctypes (Sales Invoice, Payment Entry).
  - `report/`, `page/`, `dashboard_chart_source/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, `setup/`.
  - `utils.py`: shared billing and invoice helpers.
- `controllers/`: base controllers (`service_request_controller.py`) and link queries (`queries.py`).
- `regional/india/abdm`: country-specific integration.
- `patches/` and `patches.txt`: data migrations, versioned `v0_0`/`v15_0`/`v16_0`, split into `[pre_model_sync]` and `[post_model_sync]`.
- `public/js`: Desk JS bundled via `healthcare.bundle.js`. `public/frontend`: portal static shell.
- `www/patient_portal.py` and `.html`: the server route that hosts the SPA.
- `tests/utils.py`: `HealthcareTestSuite` and the master-data bootstrap.

**`patient_portal/`**: the Vue SPA. Vite builds it into `healthcare/public/patient_portal/assets` and writes the index to `healthcare/www/patient_portal.html`. It calls the backend through frappe-ui resources and socket.io (`src/socket.js`).

**Dependency direction:** the portal calls `healthcare.healthcare.api.*`. Doctype controllers import from `healthcare.healthcare.utils` and from other doctype modules. Everything builds on `frappe` and `erpnext`. ERPNext behaviour is extended via hooks and `custom_doctype`, never by editing ERPNext itself.
