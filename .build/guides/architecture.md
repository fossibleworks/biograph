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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

## Layout

- `healthcare/` is the Frappe app package.
  - `hooks.py` wires everything: `doc_events` (including a `*` hook for medical records on submit and cancel), `scheduler_events` (for example, appointment reminders), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js` for ERPNext forms, and the `/patient-portal` website route.
  - `healthcare/healthcare/` is the module. It contains:
    - `doctype/<snake_name>/`, one folder per doctype (139). Each holds `.json` schema, `.py` controller, `.js` form script, optional `_list.js` and `_calendar.js`, and `test_<name>.py`.
    - `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/` and `onboarding_step/`.
    - `custom_doctype/`: subclasses and overrides of ERPNext doctypes (sales_invoice.py, payment_entry.py).
    - `api/patient_portal.py`: whitelisted endpoints for the portal.
    - `utils.py`: shared billing and service helpers.
  - `controllers/`: shared controllers (`service_request_controller.py`, `queries.py` for link-field search queries).
  - `patches/v0_0`, `v15_0`, `v16_0` with `patches.txt`: data migrations run on `bench migrate`.
  - `setup.py`, `install.py`, `uninstall.py` and `after_migrate.py`: install-time fixtures and setup.
  - `public/js` (desk JS), `public/frontend` (built portal assets), `www/patient_portal.html|py` (portal shell page), `templates/` and `locale/main.pot`.
  - `tests/utils.py`: `HealthcareTestSuite` and `BootStrapTestData`, the shared test master data.
- `patient_portal/` is the Vue SPA source. It calls whitelisted Python methods through frappe-ui `createResource` and builds into the app's `public` dir.
- `wiki/` holds design docs and usage docs.

## Dependency direction

The portal (Vue) calls `@frappe.whitelist()` methods over HTTP. Desk JS calls doctype or whitelisted methods via `frappe.call`. Doctype controllers in turn use `healthcare.healthcare.utils`, the controllers and ERPNext modules. ERPNext and Frappe are hooked into, not modified. Import order puts `frappe`, then `erpnext`, then `healthcare` as separate isort sections.
