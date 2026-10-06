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
  - patient_portal/src/PatientPortal.vue
---

The repo is a single Frappe app. The Python package is `healthcare/`, and its one module is also called `healthcare` (`healthcare/healthcare/`, see `modules.txt`).

**Top-level layout**
- `healthcare/hooks.py`: the integration hub. It defines:
  - `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical records)
  - `scheduler_events` (appointment reminders, daily status updates)
  - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`)
  - `jinja` methods, `has_website_permission`, `standard_queries`, `global_search_doctypes`
  - `on_login` (role-based home page)
  - install/uninstall/migrate hooks
- `healthcare/healthcare/doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller class plus `@frappe.whitelist()` functions), `<name>.js` (Desk form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
- `healthcare/healthcare/custom_doctype/`: extensions of ERPNext doctypes (sales_invoice, payment_entry).
- `healthcare/healthcare/api/patient_portal.py`: whitelisted endpoints used by the Vue portal, mostly `frappe.qb` queries.
- `healthcare/healthcare/{report,page,web_form,print_format,workspace,dashboard_chart,number_card,module_onboarding}`: standard Frappe artefacts.
- `healthcare/healthcare/utils.py`: shared helpers called from hooks (invoice submit/cancel, barcodes, and so on).
- `healthcare/controllers/`: shared base controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/abdm`: India ABDM integration.
- `healthcare/patches/{v0_0,v15_0,v16_0}` with `patches.txt`: data migrations.
- `healthcare/setup.py` and `install.py`: domain setup and fixtures.
- `healthcare/public/js`: Desk JS bundle. `healthcare/public/frontend`: built portal assets.
- `healthcare/www/patient_portal.{html,py}`: the portal entry page.
- `patient_portal/`: Vue/Vite source for the portal. It calls `/api/method/healthcare.healthcare.api.patient_portal.*` through frappe-ui `createResource`.
- `wiki/`: design notes and the upstream-sync ledger.

**Dependency direction:** `healthcare` imports from `frappe` and `erpnext`, never the reverse. ERPNext behaviour is changed only through hooks and overrides. Cross-doctype logic calls other doctype modules directly (for example, `api/patient_portal.py` imports from `doctype/observation`).
