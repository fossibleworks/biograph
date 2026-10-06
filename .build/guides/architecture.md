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

This is a single Frappe app that installs into a bench next to frappe, erpnext and payments.

**Layout**
- `healthcare/hooks.py` is the integration hub. It registers:
  - `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical records);
  - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`);
  - `scheduler_events` (appointment reminders, daily status updates, inpatient billables, medication request expiry);
  - jinja methods, `has_website_permission`, standard queries, install/migrate hooks, and `on_login` role home pages.
- `healthcare/healthcare/` is the main module.
  - `doctype/<snake_name>/` holds one folder per DocType: JSON schema, `.py` controller, `.js` form script, optional `_list.js` and `_dashboard.py`, and `test_<name>.py`.
  - Other subfolders: `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart_source/`, `number_card/`, `custom_doctype/` (extensions to ERPNext's sales_invoice and payment_entry), and `api/patient_portal.py` (whitelisted endpoints for the portal).
  - `utils.py` holds shared billing and helper logic.
- `healthcare/controllers/` holds shared controllers (`service_request_controller.py`) and link queries (`queries.py`).
- `healthcare/regional/india/abdm` contains the ABDM integration.
- `healthcare/patches/` holds versioned migrations (`v15_0`, `v16_0`), registered in `healthcare/patches.txt` under `[pre_model_sync]` / `[post_model_sync]`.
- `healthcare/setup.py` and `install.py` seed master data at install time.
- `healthcare/www/patient_portal.{py,html}` serves the SPA shell, and `healthcare/public/` holds desk JS and built portal assets.
- `patient_portal/` is the Vue SPA source. It calls the server only through `healthcare.healthcare.api.patient_portal.*` whitelisted methods and builds into `healthcare/public`.
- `wiki/` contains design docs, usage docs and sync ledgers.

**Rules of thumb**
- Business logic and validation belong on the server, in DocType controllers (the PR template says so).
- Cross-app behaviour goes through hooks, not by editing ERPNext.
- Schema changes are DocType JSON edits. Data migration needs a patch.
