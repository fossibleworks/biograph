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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/www/patient_portal.py
  - patient_portal/src/patient_portal.js
---

This is a single Frappe app, `healthcare`, installed into a bench next to frappe, erpnext and payments.

Top-level layout:
- `healthcare/hooks.py` is the integration hub. It holds `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, plus a `*` wildcard that maintains Patient Medical Records), `override_doctype_class` (Sales Invoice is replaced by `HealthcareSalesInvoice`), `scheduler_events` (appointment reminders, daily status updates, fee validity, IP billables, expired medication requests), and `standard_queries`.
- `healthcare/healthcare/` is the single module, "Healthcare" (`modules.txt`):
  - `doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (form script), optional `_list.js` / `_calendar.js`, and `test_<name>.py`. There are about 139 doctypes.
  - `custom_doctype/`: extensions of ERPNext doctypes (sales_invoice, payment_entry).
  - `api/patient_portal.py`: `@frappe.whitelist()` endpoints used by the Vue portal.
  - `utils.py`, `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/`, and onboarding.
- `healthcare/controllers/`: shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/abdm`: India-specific integration, wired in through hooks.
- `healthcare/patches/v15_0`, `v16_0` with `patches.txt`: data migrations.
- `healthcare/public/js`: desk JS bundled into `healthcare.bundle.js`. `healthcare/public/frontend`: the built portal bundle.
- `healthcare/www/patient_portal.{py,html}`: the Jinja shell that boots the SPA.
- `patient_portal/`: Vue source. It calls the whitelisted Python APIs through frappe-ui resources and uses socket.io (`socket.js`).
- `wiki/`: design docs and the upstream-sync ledger.

Dependency direction: healthcare imports from `erpnext` and `frappe`, never the reverse. Cross-doctype logic is called by dotted path from hooks, or imported as `healthcare.healthcare.doctype.<x>.<x>`.
