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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/controllers/service_request_controller.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

## Layout

- `healthcare/`: the Frappe app package.
  - `hooks.py`: the wiring hub. It registers `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical records), `scheduler_events` (appointment reminders, daily status updates, fee validity, IP billables, expired medication requests), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), jinja methods, web-form permissions, `standard_queries`, `on_login`, and install/uninstall/migrate hooks.
  - `healthcare/healthcare/`: the module.
    - `doctype/<snake_name>/`: one directory per DocType with `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (Desk form), optional `_list.js`/`_tree.js`/`_dashboard.py`, and `test_<name>.py`.
    - `custom_doctype/`: ERPNext overrides (sales_invoice, payment_entry).
    - `api/patient_portal.py`: whitelisted API for the portal.
    - `utils.py`: shared billing and service helpers.
    - Also: `report/`, `page/`, `web_form/`, `print_format/`, `dashboard_chart*`, `number_card`, `workspace/`, `module_onboarding/`.
  - `controllers/`: shared base logic such as `service_request_controller.py` and `queries.py`.
  - `regional/india/abdm`: region-specific code.
  - `patches/` plus `patches.txt`: versioned migrations (`v0_0`, `v15_0`, `v16_0`).
  - `public/js`: Desk assets. `public/frontend`: built portal assets.
  - `www/patient_portal.{html,py}`: portal entry page.
  - `tests/utils.py`: shared test bootstrap.
- `patient_portal/`: Vue SPA. It calls the backend through `frappeRequest`/frappe-ui resources (`frappeProxy`). Its build output goes into `healthcare/public/...` and `healthcare/www/patient_portal.html`.
- `wiki/`: feature design and usage docs, plus the upstream sync ledger.

## Dependency direction

The portal calls the `healthcare` whitelisted methods. Healthcare doctypes depend on Frappe and ERPNext; they extend ERPNext through hooks and overrides and never edit ERPNext itself. Doctype controllers import each other by full dotted path, e.g. `healthcare.healthcare.doctype.patient_appointment.patient_appointment`.

Business logic and validation belong on the server, as the PR template requires.
