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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This is a single Frappe app (`healthcare`) installed into a bench next to `frappe` and `erpnext`. There are no separate services.

**Layout**
- `healthcare/hooks.py`: the integration hub. It sets `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, plus a `*` hook that creates medical records on submit), `scheduler_events` (appointment reminders, daily status updates), jinja methods, install/migrate hooks, `on_login`, and `doctype_js` overrides.
- `healthcare/healthcare/doctype/<snake_name>/`: one folder per DocType. Each has `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (form script), optional `_list.js`, `_tree.js` and `_dashboard.py`, and `test_<name>.py`.
- `healthcare/healthcare/utils.py`, `healthcare/controllers/` (`service_request_controller.py`, `queries.py`): shared business logic and link-field queries.
- `healthcare/healthcare/custom_doctype/`: extensions of ERPNext doctypes (`sales_invoice.py`, `payment_entry.py`).
- `healthcare/healthcare/api/patient_portal.py`: `@frappe.whitelist()` endpoints used by the Vue portal.
- `healthcare/healthcare/{report,page,dashboard_chart_source,number_card,workspace,print_format,web_form}`: desk UI artifacts.
- `healthcare/regional/india/`: ABDM integration.
- `healthcare/patches/` and `patches.txt`: data migrations, versioned as `v15_0` and `v16_0`.
- `healthcare/www/patient_portal.{html,py}`: the portal entry page.
- `patient_portal/`: Vue SPA source. It is built into `healthcare/public/…` and calls the whitelisted API through frappe-ui resources and socket.io (`socket.js`).
- `healthcare/tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`).

**Dependency direction:** `patient_portal` calls `api/patient_portal.py`, which calls doctype controllers and `utils`, which call the Frappe/ERPNext APIs. ERPNext documents call back into healthcare through `hooks.py` `doc_events`. Business logic and validations belong on the server (PR template rule).
