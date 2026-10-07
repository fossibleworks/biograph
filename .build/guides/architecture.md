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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
---

This repo is a single Frappe app (`healthcare`) that is installed into a bench alongside frappe and erpnext.

**Python package layout (`healthcare/`):**
- `hooks.py` is the wiring hub:
  - `doc_events`, including `*` on_submit/on_cancel creating medical records
  - `scheduler_events`, such as appointment reminders
  - `doctype_js` overrides for Sales Invoice and Healthcare Practitioner
  - fixtures and website routes
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/` holds each DocType: `.json` schema, `.py` controller, `.js` form script, optional `_list.js` / `_calendar.js`, and `test_<name>.py`
  - `report/`, `page/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, and onboarding folders hold Desk metadata
  - `custom_doctype/` extends ERPNext doctypes (sales_invoice, payment_entry)
  - `api/patient_portal.py` holds the whitelisted endpoints for the portal
  - `utils.py` holds shared server helpers (billing, configuration checks, code values)
  - `setup/` holds install-time setup, such as duplicate-check rules
- `controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
- `regional/india/` holds country-specific customisations.
- `patches/` (folders `v0_0`, `v15_0`, `v16_0`) and `patches.txt` (split into `[pre_model_sync]` and `[post_model_sync]`) handle data migrations.
- `public/js/` holds the Desk JS bundle and shared form helpers.
- `www/` and `templates/` hold the portal pages.
- `locale/main.pot` holds the translatable strings.
- `tests/utils.py` holds the `HealthcareTestSuite` and test bootstrap data.

**Patient portal (`patient_portal/`):** a Vue SPA. It calls the backend only through `/api/method/healthcare.healthcare.api.patient_portal.*` using frappe-ui `createResource`. Vite builds it into `healthcare/public/frontend` (and `patient_portal/assets`) and writes `healthcare/www/patient_portal.html`.

**How the parts call each other:**
- Desk JS calls `frappe.call` against `@frappe.whitelist()` methods in controllers and utils.
- Controllers call ERPNext (Sales Invoice, POS Profile, accounts).
- Cross-doctype side effects go through `hooks.py` doc_events.
