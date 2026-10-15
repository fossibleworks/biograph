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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
---

## Top-level layout
- `healthcare/` is the Frappe app package and the only Python package.
  - `hooks.py` is the integration point with Frappe and ERPNext. It holds `doc_events` (Sales Invoice, Payment Entry, Company, Patient and the wildcard `*` for medical records), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `scheduler_events` (appointment reminders, daily status updates), `jinja` methods, `on_login`, and the install, migrate and uninstall hooks.
  - `healthcare/healthcare/` is the `Healthcare` module. It contains:
    - `doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (Desk form script), optional `_list.js` / `_calendar.js` / `_dashboard.py`, and `test_<name>.py`.
    - `custom_doctype/`: overrides and handlers for ERPNext doctypes (`sales_invoice.py`, `payment_entry.py`).
    - `api/patient_portal.py`: `@frappe.whitelist()` endpoints used by the portal SPA.
    - `utils.py`: large shared helpers for invoicing and billables.
    - Desk metadata in `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/` and `onboarding_step/`.
  - `controllers/`: shared base controllers, for example `service_request_controller.py` and `queries.py`.
  - `regional/india/abdm`: country-specific integration.
  - `patches/v0_0`, `v15_0`, `v16_0` plus `patches.txt` (`[pre_model_sync]` / `[post_model_sync]`): data migrations.
  - `setup.py`, `install.py`, `uninstall.py`, `after_migrate.py`: install and fixture setup.
  - `public/js`: Desk JS bundle. `public/frontend`: built portal assets.
  - `www/`: portal HTML and Python page context (`patient_portal.html`, `patient-portal/`).
  - `locale/main.pot`: translation template.
  - `tests/`: shared test helpers.
- `patient_portal/` is the Vue SPA source. It builds into `healthcare/public/...` and `healthcare/www/patient_portal.html`.
- `public/js/` (repo root) holds a stray copy of `mark_unavailable.js`. The canonical Desk JS lives in `healthcare/public/js/`.
- `wiki/` holds design docs and usage guides.

## How the pieces call each other
- The portal SPA calls `/api/method/healthcare.healthcare.api.patient_portal.<fn>` through frappe-ui `createResource`.
- Desk JS calls whitelisted controller methods with `frappe.call` or `frm.call`.
- Controllers call ERPNext APIs, such as `erpnext.accounts.party` and customer and address helpers, and import each other through full dotted paths (`healthcare.healthcare.doctype.x.x`).
- ERPNext events reach healthcare code only through `hooks.py`. Do not monkey-patch.

To add a feature, add or extend a DocType folder, wire any cross-app behaviour in `hooks.py`, and add a patch in `patches.txt` for any data migration.
