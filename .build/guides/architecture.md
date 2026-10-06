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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/tests/utils.py
---

# Architecture

This is a single Frappe app repo. Code is laid out in the standard Frappe app structure.

## Top-level
- `healthcare/`: the Python package (the Frappe app).
  - `hooks.py`: the integration surface with Frappe and ERPNext. It holds `doc_events` (including the wildcard `*` hooks that keep Patient Medical Record in sync), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js` for ERPNext doctypes, `scheduler_events`, and `required_apps`.
  - `healthcare/healthcare/`: the single module, **Healthcare** (`modules.txt`).
    - `doctype/<snake_name>/`: one folder per DocType, with `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (Desk form script), optional `_list.js`, `_tree.js` and `_dashboard.py` files, and `test_<name>.py`.
    - `custom_doctype/`: overrides and extensions of ERPNext doctypes (sales_invoice, payment_entry).
    - `api/patient_portal.py`: whitelisted endpoints used by the Vue portal.
    - `report/`, `dashboard_chart(_source)/`, `number_card/`, `workspace/`, `page/`, `print_format/`, `web_form/`, `setup/`, `utils.py`.
  - `controllers/`: shared controller logic (`service_request_controller.py`, `queries.py` for link-field search queries).
  - `regional/india/`: ABDM and regional features.
  - `patches/` and `patches.txt`: versioned migration patches (`v0_0`, `v15_0`, `v16_0`).
  - `public/js`: Desk JS bundles. `public/frontend`: built portal assets.
  - `www/patient_portal.html|.py`: the Jinja shell that boots the portal SPA.
  - `tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).
- `patient_portal/`: the Vue 3 + frappe-ui SPA. Vite builds it into `healthcare/public/...` and writes its index HTML into `healthcare/www/patient_portal.html`. It calls the backend through frappe-ui resources and `/api/method/healthcare.healthcare.api.patient_portal.*`.
- `wiki/`: design notes, usage docs and the upstream-sync ledger.

## Dependency direction
Portal → whitelisted API → doctype controllers → Frappe ORM / ERPNext. Doctypes call each other directly through `frappe.get_doc` and module imports (for example, fee_validity imports from patient_appointment). ERPNext documents are extended through hooks and class overrides, never by editing ERPNext.
