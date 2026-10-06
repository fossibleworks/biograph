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
  - patient_portal/src/PatientPortal.vue
  - healthcare/patches.txt
---

The repo is one Frappe app plus a separate SPA source folder.

- `healthcare/`: the Python package and Frappe app.
  - `hooks.py`: the app wiring. It declares `doctype_js` for ERPNext doctypes, `doc_events` (a global `*` on_submit/on_cancel hook that writes Patient Medical Records, plus Sales Invoice hooks), `scheduler_events` (appointment reminders, daily status updates), `jinja` methods, `on_login`, and fixtures.
  - `healthcare/healthcare/`: the Frappe module.
    - `doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
    - `report/`, `page/`, `dashboard_chart*/`, `custom_doctype/`.
    - `api/patient_portal.py`: whitelisted endpoints used by the portal.
    - `utils.py`: shared billing and helper logic.
  - `controllers/`: shared controllers (`service_request_controller.py`, `queries.py`).
  - `regional/india/`: region-specific logic.
  - `patches/v0_0|v15_0|v16_0/`: migration patches, registered in `patches.txt`.
  - `www/patient_portal.{html,py}`: portal page shell.
  - `public/js/`: desk scripts.
  - `public/frontend/`: built portal bundle.
  - `tests/utils.py`: shared `HealthcareTestSuite` and bootstrap data.
  - `setup.py`, `install.py`, `after_migrate.py`, `uninstall.py`: lifecycle hooks.
- `patient_portal/`: Vue 3 + frappe-ui source. It calls backend `@frappe.whitelist()` methods through `createResource`, and its Vite build writes into `healthcare/public/...`.
- `wiki/`: design and usage docs and the upstream-sync ledger.

**Dependency direction:** `healthcare` imports from `frappe` and `erpnext`, and extends ERPNext doctypes (Sales Invoice, Healthcare Practitioner via Employee and so on) through hooks. The portal talks to the backend only over Frappe RPC.
