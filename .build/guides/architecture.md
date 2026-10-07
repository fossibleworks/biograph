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
  - healthcare/www/patient_portal.py
  - patient_portal/vite.config.js
---

Biograph is a single **Frappe app** named `healthcare` that installs alongside ERPNext. The Patient Portal SPA lives in its own directory and its build output is placed inside the app.

**Top-level layout**
- `healthcare/hooks.py` is the integration point with Frappe and ERPNext. It declares:
  - `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company) and a `*` wildcard that maintains Patient Medical Records
  - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`)
  - `scheduler_events` (appointment reminders, daily status updates)
  - jinja methods, portal menu, `has_website_permission`, the `on_login` role-based home page, and install/migrate hooks
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/` holds `.json` schema, `.py` controller (a `Document` subclass), `.js` form script and `test_<name>.py`
  - `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/`, `onboarding_step/`
  - `custom_doctype/` holds overrides and extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
  - `api/patient_portal.py` holds the `@frappe.whitelist()` endpoints used by the portal
  - `utils.py` holds shared billing and invoice helpers
- `healthcare/controllers/` holds shared controllers, for example `service_request_controller.py` and `queries.py` (link-field search queries).
- `healthcare/regional/india/` holds ABDM integration.
- `healthcare/patches/v0_0|v15_0|v16_0/` holds data migrations, registered in `healthcare/patches.txt` under `[pre_model_sync]` or `[post_model_sync]`.
- `healthcare/setup.py` and `install.py` / `uninstall.py` / `after_migrate.py` are lifecycle hooks.
- `healthcare/www/patient_portal.{html,py}` serves the SPA shell. `healthcare/public/` holds desk JS, images and the built portal assets.
- `patient_portal/` is the Vue SPA source. It calls whitelisted Python methods through frappe-ui resources, proxied by `frappeProxy`.
- `wiki/` holds design notes, usage docs and the upstream-sync ledger.

**How the parts depend on each other**
- The portal calls `healthcare.healthcare.api.*` over HTTP.
- Desk JS calls `frappe.call` against whitelisted controller methods.
- Controllers call ERPNext (invoices, items, customers) and Frappe (`frappe.get_doc`, `frappe.qb`).
- ERPNext calls back into Biograph through `doc_events` hooks.
- Cross-doctype helpers are imported by dotted path, for example `healthcare.healthcare.doctype.patient_appointment.patient_appointment`.
