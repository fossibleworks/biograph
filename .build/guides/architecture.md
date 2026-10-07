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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

## Layout
- `healthcare/` is the Frappe app package.
  - `hooks.py` is the integration hub. It defines `doc_events` on ERPNext DocTypes (Sales Invoice, Payment Entry, Company, Patient, plus a wildcard `*` hook for medical records), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js`, `scheduler_events` (appointment reminders, daily status updates), `jinja` methods, and the install/uninstall/migrate hooks.
  - `healthcare/healthcare/` holds the main module:
    - `doctype/<snake_name>/`: one folder per DocType, with `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), optional `<name>_list.js` / `<name>_dashboard.py`, and `test_<name>.py`.
    - `api/patient_portal.py`: whitelisted endpoints called by the Vue portal.
    - `custom_doctype/`: extensions of ERPNext doctypes (sales_invoice, payment_entry).
    - `utils.py`: shared billing and invoicing helpers (large; about 1.9k lines).
    - `report/`, `page/`, `print_format/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `web_form/`, `module_onboarding/`.
  - `controllers/` holds cross-doctype base logic (`service_request_controller.py`, `queries.py` for link-field search queries).
  - `regional/india/` holds the ABDM integration.
  - `patches/` (`v0_0`, `v15_0`, `v16_0`) plus `patches.txt` hold data migrations.
  - `public/js/` holds Desk JS (shared form helpers, the observation widget, quick entry).
  - `www/` holds website routes, including the `patient_portal.html` host page.
  - `tests/utils.py` holds `BootStrapTestData` and the `HealthcareTestSuite` base class.
  - `locale/main.pot` holds translatable strings.
- `patient_portal/` is the Vue 3 + frappe-ui SPA. Vite builds it into `healthcare/public/patient_portal/assets` and injects it into `healthcare/www/patient_portal.html`. It calls `healthcare.healthcare.api.patient_portal.*` over the Frappe REST/RPC proxy.
- `wiki/` holds design notes, usage docs and the upstream sync ledger.

## Dependency direction
The portal calls the whitelisted API, which uses DocType controllers and `utils`, which call frappe and erpnext. ERPNext documents call back into healthcare only through `hooks.py` doc_events and class overrides. Never edit erpnext itself.

## Fork relationship
`biograph-fh` is a fork of earthians/marley `version-16`. Upstream fixes come in through `git cherry-pick -x` with the rule **fork intent wins**. The ledger is `wiki/upstream-sync-version-16.md`.
