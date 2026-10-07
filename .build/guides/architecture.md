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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/www/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Architecture

This is a single Frappe app (`healthcare`) plus a separately built Vue portal.

## Top-level layout
- `healthcare/` is the Python package and Frappe app root.
  - `hooks.py` wires the app into Frappe/ERPNext: `override_doctype_class`, `doc_events`, `scheduler_events`, `app_include_js`, permissions.
  - `healthcare/healthcare/` is the main module.
    - `doctype/<snake_name>/`: one folder per DocType, holding `<name>.json` (schema), `<name>.py` (controller class), `<name>.js` (Desk form script), and `test_<name>.py`. There are about 139 doctypes.
    - `custom_doctype/`: overrides of ERPNext classes such as `sales_invoice.py` and `payment_entry.py`.
    - `api/patient_portal.py`: whitelisted endpoints used by the portal.
    - `report/`, `page/`, `dashboard_chart(_source)/`, `number_card/`, `workspace/`, `print_format/`, `web_form/`, `setup/`, `utils.py`: shared server helpers.
  - `controllers/`: shared controller logic (`queries.py`, `service_request_controller.py`).
  - `regional/`: country-specific code.
  - `patches/` + `patches.txt`: data migrations, versioned under `v0_0`, `v15_0` and `v16_0`.
  - `public/js`: Desk JS bundle and shared widgets (observation widget, healthcare notes, orders).
  - `www/patient_portal.{html,py}`: the web route that serves the SPA.
  - `tests/utils.py`: test bootstrap (`HealthcareTestSuite`).
  - `locale/main.pot`: translatable strings.
- `patient_portal/`: Vue 3 SPA source. Vite builds it into `healthcare/public/...` and writes the HTML shell to `healthcare/www/patient_portal.html`.
- `wiki/`: design and usage docs. `.github/`: CI, helpers and templates.

## How the pieces talk
- Doctype controllers import each other directly with absolute `healthcare.healthcare.doctype...` imports. Example: `patient_appointment` imports `fee_validity`, `healthcare_settings`, `patient_insurance_coverage` and `api.patient_portal`.
- Controllers also call into **ERPNext** (`erpnext.setup...`, `erpnext.accounts...`) for billing, stock and holidays.
- Desk JS calls server methods with `frappe.call` to `@frappe.whitelist()` functions (about 182 whitelisted functions).
- The portal reaches the backend only through Frappe REST/whitelisted methods (via the frappe-ui proxy) and socket.io (`src/socket.js`).
- Background work goes through `frappe.enqueue` and the `scheduler_events` in `hooks.py`.
- Business logic and validation live server-side, as the PR template states.
