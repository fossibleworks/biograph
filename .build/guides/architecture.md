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
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
  - healthcare/healthcare/api/patient_portal.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Biograph is a single Frappe app (`healthcare`) installed into a bench next to `frappe`, `erpnext` and `payments`.

**Layout**
- `healthcare/hooks.py` wires everything together:
  - `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical records)
  - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`)
  - `scheduler_events` (appointment reminders, daily status updates)
  - `jinja` methods, `has_website_permission`, `standard_queries`, the `on_login` role-based home page, and install/migrate hooks
- `healthcare/healthcare/` is the module package:
  - `doctype/<snake_name>/`: one folder per DocType with `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (desk form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`
  - also `report/`, `page/`, `print_format/`, `web_form/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `custom_doctype/` (extensions of ERPNext doctypes such as `sales_invoice.py` and `payment_entry.py`), `api/patient_portal.py` (portal API), `utils.py` (shared server helpers) and `auth.py`
- `healthcare/controllers/`: cross-doctype controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/abdm`: region-specific integration.
- `healthcare/patches/v{0_0,15_0,16_0}/` plus `healthcare/patches.txt` (split into `[pre_model_sync]`/`[post_model_sync]`): data migrations.
- `healthcare/public/js`: desk JS that is shared or that extends ERPNext forms (`doctype_js` in hooks).
- `healthcare/www/patient_portal.*` with `patient_portal/` (Vue source): the patient SPA. It calls whitelisted Python methods through frappe-ui resources.
- `healthcare/tests/utils.py`: test bootstrap (`BootStrapTestData`, `HealthcareTestSuite`).

**Call flow:** desk JS and the portal call `@frappe.whitelist()` Python methods (182 of them), which use the Frappe ORM (`frappe.get_doc`, `frappe.db.*`) and ERPNext APIs. Healthcare documents create and link ERPNext Sales Invoices and Payment Entries through hooks in `utils.py`/`custom_doctype`. Business logic and validation belong on the server, as the PR template states.
