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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/healthcare/api/patient_portal.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Biograph is a single Frappe app installed into a bench next to `frappe`, `erpnext` and `payments`.

**Top-level layout**
- `healthcare/` is the Python package (the app).
  - `hooks.py` wires everything into Frappe: `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `scheduler_events` (appointment reminders, daily status updates), jinja methods, portal permissions, standard queries, and install/migrate hooks.
  - `healthcare/healthcare/` is the main module.
    - `doctype/` holds about 139 doctypes. Each is a folder containing `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
    - Also here: `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, dashboard charts and number cards, `custom_doctype/` (extensions to ERPNext doctypes), `api/patient_portal.py` (whitelisted portal API), `utils.py` (shared billing and invoice helpers), and `setup.py`.
  - `controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
  - `regional/india/` holds ABDM integration.
  - `patches/` holds versioned migration patches (`v0_0`, `v15_0`, `v16_0`), registered in `patches.txt` with `[pre_model_sync]` and `[post_model_sync]` sections.
  - `public/js` holds desk JS. `public/frontend` holds the built portal assets.
  - `www/patient_portal.{html,py}` is the portal entry page.
  - `tests/utils.py` provides `HealthcareTestSuite` and bootstrap data.
- `patient_portal/` is the Vue SPA source. It builds into `healthcare/public/...` and talks to the backend over Frappe REST/whitelisted methods and socket.io.
- `wiki/` holds fork design and usage docs.

**Dependency direction:** `healthcare` imports from `frappe` and `erpnext`, never the reverse. ERPNext behaviour is extended only through hooks, `custom_doctype/` and custom fields. Business logic and validations belong on the server, in doctype controllers. Desk JS and the portal only call whitelisted methods.
