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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

This is a single Frappe app, `healthcare`, installed onto a bench site alongside frappe and erpnext.

**Top-level layout**
- `healthcare/`: the Python package (the app root).
  - `hooks.py`: the integration hub. It holds `doc_events` on ERPNext doctypes (Sales Invoice, Company, Patient, and `*` for medical records), `scheduler_events` (appointment reminders, daily status updates), `doctype_js` overrides, and the JS bundle include.
  - `healthcare/healthcare/`: the module itself.
    - `doctype/<snake_name>/` holds `<name>.json` (metadata), `<name>.py` (controller class extending `Document`), `<name>.js` (desk form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
    - Other module folders: `report/`, `page/`, `print_format/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `web_form/`, `custom_doctype/` (extensions of ERPNext doctypes such as `sales_invoice.py` and `payment_entry.py`), `api/patient_portal.py` (whitelisted portal API), `setup/`, and `utils.py` (shared billing/invoice helpers).
  - `controllers/`: shared controllers (`service_request_controller.py`, `queries.py` for link-field queries).
  - `regional/india/abdm`: country-specific integration.
  - `patches/v0_0|v15_0|v16_0` + `patches.txt`: data migrations, split into `[pre_model_sync]` and `[post_model_sync]`.
  - `public/js`: desk JS bundle. `public/frontend` holds the built portal assets.
  - `www/patient_portal.html|.py`: the Jinja host page for the SPA.
  - `templates/`, `locale/`, `config/`, `install.py`/`setup.py`/`uninstall.py`/`after_migrate.py`.
  - `tests/utils.py`: `HealthcareTestSuite` and bootstrap test data.
- `patient_portal/`: the Vue SPA source. It calls `healthcare.healthcare.api.patient_portal.*` via frappe-ui `createResource`. Vite outputs to `healthcare/public/...` and writes the index into `healthcare/www/patient_portal.html`.
- `public/js/`: a small root-level JS asset (`mark_unavailable.js`).
- `wiki/`: fork design docs and the upstream sync ledger.

**Dependency direction:** `healthcare` depends on `erpnext` and `frappe`, never the reverse. Doctypes import helpers from `healthcare.healthcare.utils` and from each other by full dotted path (e.g. `healthcare.healthcare.doctype.patient_appointment.patient_appointment`). ERPNext behaviour is extended through hooks and `custom_doctype`, never by editing ERPNext.

**Upstream relationship:** this repo tracks earthians/marley `version-16`. Upstream commits are cherry-picked with `-x` under a "fork intent wins" conflict policy (see `wiki/upstream-sync-version-16.md`).
