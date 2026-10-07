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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

# Architecture

This is one Frappe app, `healthcare`, installed into a bench alongside `frappe`, `erpnext` and `payments`.

## Layout
- `healthcare/hooks.py` is the integration point with Frappe and ERPNext. It holds:
  - `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company) and a `*` wildcard that maintains Patient Medical Records
  - `override_doctype_class` for Sales Invoice (`HealthcareSalesInvoice`)
  - `doctype_js` for ERPNext forms
  - `scheduler_events` for appointment reminders and status updates, fee validity, IP billing, and medication-request expiry
  - install, migrate and uninstall hooks, and jinja methods
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/`: the JSON schema, Python controller, desk JS, `_list.js` and `test_<name>.py` for each doctype
  - `api/patient_portal.py`: whitelisted endpoints for the portal
  - `custom_doctype/`: hooks and overrides on ERPNext doctypes such as `sales_invoice.py` and `payment_entry.py`
  - `utils.py`: large shared billing and helper functions
  - `report/`, `page/`, `print_format/`, `workspace/`, `dashboard_chart*/`, `number_card/`, `web_form/`, `setup/`
- `healthcare/controllers/`: shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/`: ABDM integration.
- `healthcare/patches/{v0_0,v15_0,v16_0}` plus `healthcare/patches.txt`: migrations, split into `[pre_model_sync]` and `[post_model_sync]`.
- `healthcare/public/js`: desk assets.
- `healthcare/www/patient_portal.{html,py}`: portal entry point.
- `patient_portal/`: Vue source. It is built into `healthcare/public/...` and calls the `healthcare.healthcare.api.patient_portal.*` endpoints through frappe-ui resources and socket.io.
- `healthcare/tests/utils.py`: shared test bootstrap.

## Dependency direction
Doctype controllers import each other's helper functions directly, for example `patient_appointment.py` imports from `fee_validity`, `healthcare_settings` and `patient_insurance_coverage`. They also import ERPNext modules such as `erpnext.setup...`. ERPNext never imports healthcare; healthcare plugs in only through hooks.

Import sections are ordered stdlib, third-party, frappe, erpnext, healthcare. Long-running work goes through `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`.
