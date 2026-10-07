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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/controllers/service_request_controller.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

This is a single Frappe app, `healthcare`, installed into a bench next to `frappe` and `erpnext`. All integration with the platform goes through `healthcare/hooks.py`.

**Layout**
- `healthcare/hooks.py`: the wiring point. It holds:
  - `doc_events`: Sales Invoice, Payment Entry and Company hooks, plus wildcard `*` hooks for the Patient Medical Record
  - `override_doctype_class`: Sales Invoice is replaced by `HealthcareSalesInvoice`
  - `scheduler_events`: appointment reminders, and daily status and validity updates
  - Jinja methods, portal menu, website permissions, `standard_queries`, install, migrate and uninstall hooks
- `healthcare/healthcare/`: the module itself.
  - `doctype/`: about 139 DocTypes. Each folder holds `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (desk form script), and optionally `<name>_list.js` and `test_<name>.py`.
  - `api/patient_portal.py`: whitelisted endpoints for the Vue portal.
  - `custom_doctype/`: extensions to ERPNext doctypes (`sales_invoice.py`, `payment_entry.py`).
  - `utils.py`: shared billing and invoice helpers, called from hooks.
  - Also `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/` and `setup/`.
- `healthcare/controllers/`: shared controllers (`service_request_controller.py`) and link-field queries (`queries.py`).
- `healthcare/regional/india/`: ABDM integration, hooked from the Patient `after_insert` event.
- `healthcare/patches/` and `patches.txt`: versioned data migrations (`v15_0`, `v16_0`) under `[post_model_sync]`.
- `healthcare/public/js/`: desk bundle and shared widgets (observation, healthcare notes, orders).
- `patient_portal/`: Vue SPA source. It builds into `healthcare/public/...` and is served by `healthcare/www/patient_portal.html`.
- `healthcare/tests/utils.py`: shared test bootstrap.
- `wiki/`: design notes and the upstream-sync ledger.

**Dependencies between parts**
- DocType controllers call each other directly through Python imports. For example, `patient_appointment.py` imports from `fee_validity`, `healthcare_settings`, `patient_insurance_coverage` and `api.patient_portal`.
- ERPNext is extended through hooks and class overrides, never by editing ERPNext.
- The portal calls whitelisted methods under `healthcare.healthcare.api.patient_portal` through frappe-ui's proxy.
- The fork tracks upstream `earthians/marley` `version-16`. Upstream commits are cherry-picked with `-x` under a "fork intent wins" policy.
