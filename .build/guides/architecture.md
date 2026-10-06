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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
---

Biograph is a single Frappe app (`healthcare/`) plus a separate Vue SPA source tree (`patient_portal/`).

## Layout
- `healthcare/hooks.py`: the app wiring.
  - `doctype_js` overrides for ERPNext doctypes (Sales Invoice, Healthcare Practitioner).
  - `on_login` role-based home page (`healthcare.healthcare.auth`).
  - `scheduler_events`: appointment reminders (all), plus daily status, fee validity, IP billables and medication request expiry.
  - Jinja methods.
- `healthcare/healthcare/`: the main module.
  - `doctype/`: about 139 DocTypes. Each has `<name>.json`, `<name>.py` (controller class), `<name>.js` (form script), an optional `<name>_list.js`, and `test_<name>.py`.
  - `custom_doctype/`: overrides of ERPNext doctypes such as `sales_invoice.py` and `payment_entry.py`.
  - `api/patient_portal.py`: the `@frappe.whitelist()` endpoints that the portal calls.
  - `report/`, `page/`, `dashboard_chart_source/`, `workspace/`, `print_format/`, `web_form/`.
  - `utils.py`: shared helpers, for example billing items and rates.
- `healthcare/controllers/`: cross-doctype controllers such as `service_request_controller.py` and `queries.py`.
- `healthcare/regional/india/abdm`: the ABDM integration.
- `healthcare/patches/` (`v0_0`, `v15_0`, `v16_0`) together with `patches.txt`: data migrations.
- `healthcare/setup.py`, `install.py`, `uninstall.py`, `after_migrate.py`: install and migrate hooks.
- `healthcare/public/js/`: desk JS bundled into `healthcare.bundle.js`.
- `healthcare/www/`: website routes for the patient portal.
- `patient_portal/src`: Vue components (appointments, booking, diagnostics, payment, calendar). They call the whitelisted APIs through the frappe-ui resource proxy.

## How the parts depend on each other
- DocType controllers import each other and shared helpers using absolute `healthcare.healthcare...` paths.
- They lean heavily on ERPNext documents, especially Sales Invoice for billing.
- The portal talks only to `healthcare.healthcare.api.patient_portal.*`.

## Upstream relationship
- The fork tracks upstream `earthians/marley` `version-16` by cherry-picking commits (`git cherry-pick -x`).
- Conflict policy is **fork intent wins**.
- Doctype JSON conflicts are resolved by a 3-way union of `fields` and `field_order`. `patches.txt` conflicts are resolved by union.
