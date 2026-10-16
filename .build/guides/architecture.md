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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - patient_portal/src/socket.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Architecture

This is a single Frappe app (`healthcare`) that installs into an ERPNext bench, plus a separately built Vue SPA.

## Top-level layout
- `healthcare/`: the Frappe app package.
  - `hooks.py`: the integration point with Frappe/ERPNext. It declares `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical-record creation), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js`, `scheduler_events`, Jinja methods, and install/migrate hooks.
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType (about 138). Each holds `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (desk form script), optional `<name>_list.js` / `<name>_dashboard.py`, and `test_<name>.py`.
    - `api/patient_portal.py`: whitelisted endpoints that serve the Vue portal.
    - `custom_doctype/`: extensions of ERPNext doctypes (sales_invoice, payment_entry).
    - `report/`, `page/`, `dashboard_chart_source/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, `setup/`: standard Frappe artefacts.
    - `utils.py`: shared billing and service-unit helpers, called from hooks.
  - `controllers/`: shared controller logic (`service_request_controller.py`, `queries.py` link-field search queries).
  - `regional/india/abdm/`: country-specific integration.
  - `patches/` + `patches.txt`: data migrations, versioned `v0_0`, `v15_0`, `v16_0`, split into `[pre_model_sync]` and `[post_model_sync]`.
  - `public/js`: desk JS bundle and shared widgets. `public/frontend`: built portal assets.
  - `www/`: website routes (`patient_portal.html/.py` boot the SPA).
  - `tests/`: shared test bootstrap data (`utils.py`).
- `patient_portal/`: the Vue 3 + frappe-ui SPA. It calls `/api/method/healthcare.healthcare.api.patient_portal.*` through `frappeRequest` and listens on socket.io for `refetch_resource`. The build output goes into `healthcare/public/...` and `healthcare/www/patient_portal.html`.
- `wiki/`: feature design and usage notes.

## Dependency direction
Portal → whitelisted `api` → DocType controllers/utils → Frappe/ERPNext. ERPNext documents call back into healthcare through `hooks.py` `doc_events`. Put new cross-app behaviour in hooks or `custom_doctype/`. Do not edit ERPNext.

## Rules
- Server-side business logic and validation belong in the Python controller, not in form JS (PR template).
- Schema changes go in the DocType JSON. Data backfills go in a new patch module registered in `patches.txt`.
