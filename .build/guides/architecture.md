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
  - healthcare/modules.txt
  - healthcare/controllers/service_request_controller.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

Standard **Frappe app layout**. The repo root is the app; `healthcare/` is the Python package.

- `healthcare/hooks.py` is the integration hub. It defines:
  - `doc_events`: a wildcard `*` on_submit/on_cancel hook that creates patient medical records, plus hooks on ERPNext `Sales Invoice`, `Payment Entry`, `Company`, and `Patient`
  - `override_doctype_class` (`Sales Invoice` → `HealthcareSalesInvoice`)
  - `doctype_js` for ERPNext forms
  - `scheduler_events` (appointment reminders, daily status updates)
  - `standard_queries`, jinja methods, and `on_login`
- `healthcare/healthcare/` holds the single module **Healthcare** (`modules.txt`):
  - `doctype/<snake_name>/`: each DocType has `<name>.json` (schema), `<name>.py` (Document controller class), `<name>.js` (form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`
  - `custom_doctype/`: overrides and extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
  - `report/`, `page/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, `module_onboarding/`: metadata-driven desk artefacts
  - `utils.py`: shared billing and invoicing helpers called from hooks
  - `api/patient_portal.py`: whitelisted endpoints for the portal
- `healthcare/controllers/`: shared query functions and the `ServiceRequestController` base class.
- `healthcare/regional/india/abdm`: country-specific integration.
- `healthcare/patches/v0_0|v15_0|v16_0` plus `patches.txt`: data migrations run on `bench migrate`.
- `healthcare/setup.py`, `install.py`, `uninstall.py`, `after_migrate.py`: install-time custom fields and setup.
- `healthcare/www/`: website routes (`patient_portal.html`, `patient-portal/`).
- `patient_portal/`: Vue SPA source. Vite builds it into `healthcare/public/...` and `healthcare/www/patient_portal.html`. It calls the backend through frappe-ui resources and the whitelisted `@frappe.whitelist()` methods.

The call direction is: browser (desk JS / portal) → `frappe.call` / whitelisted methods → DocType controllers → ERPNext doctypes (Sales Invoice, Payment Entry, Item, Customer). ERPNext document events call back into healthcare through hooks.
