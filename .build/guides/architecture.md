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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

## Layout
- `healthcare/` is the Frappe app package.
  - `hooks.py` is the integration wiring:
    - `doc_events`: a wildcard `on_submit`/`on_cancel` that creates Patient Medical Records, plus Sales Invoice, Payment Entry, Company and Patient hooks.
    - `scheduler_events`: appointment reminders, and daily fee-validity, appointment-status and medication-request expiry jobs.
    - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `jinja` methods, `has_website_permission`, `standard_queries`, and `on_login` role-based home page.
  - `healthcare/healthcare/` is the main module:
    - `doctype/`: 139 doctypes. Each one has its own folder: `<name>.json` schema, `<name>.py` controller, `<name>.js` form script, optional `_list.js`, `_tree.js` and `_dashboard.py`, and `test_<name>.py`.
    - `report/`, `page/`, `dashboard_chart_source/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`.
    - `custom_doctype/`: ERPNext overrides such as `sales_invoice.py` and `payment_entry.py`.
    - `api/patient_portal.py`: whitelisted endpoints for the portal.
    - `utils.py`: shared billing and helpers, ~1.9k lines.
    - `setup/`: install-time setup.
  - `controllers/`: shared controllers (`service_request_controller.py`, `queries.py`).
  - `regional/india/abdm`: country-specific code.
  - `patches/` plus `patches.txt`: migrations under `v0_0`, `v15_0` and `v16_0`, split into `[pre_model_sync]` and `[post_model_sync]`.
  - `public/js`: desk JS bundle. `public/frontend`: built portal assets.
  - `www/patient_portal.html|.py`: portal host page.
  - `tests/utils.py`: shared test bootstrap.
  - `locale/main.pot`: translatable strings.
- `patient_portal/` is the Vue SPA. It calls the `healthcare.healthcare.api.patient_portal.*` whitelisted methods through frappe-ui `frappeRequest`, and the Vite build writes into `healthcare/`.
- `wiki/` holds design, usage and parity docs.

## Dependency direction
healthcare → ERPNext → Frappe. Healthcare hooks into ERPNext documents (Sales Invoice, Payment Entry, Company, Customer) through `doc_events` and class overrides. It does not edit ERPNext. Doctypes call each other through module paths like `healthcare.healthcare.doctype.<x>.<x>`. Put business logic and validation on the **server** side, as the PR template requires.
