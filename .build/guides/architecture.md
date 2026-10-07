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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

This is a standard Frappe app layout. The Python package is `healthcare/`.

- `healthcare/hooks.py` is the integration hub. It registers the desk JS bundle, `doctype_js` form scripts for ERPNext doctypes, `override_doctype_class` (for example `HealthcareSalesInvoice`), `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient), `scheduler_events`, jinja methods, portal menu items, website permissions, install/migrate hooks and `standard_queries`.
- `healthcare/healthcare/` is the main module. Inside it:
  - `doctype/` holds about 139 DocTypes, one folder each with `<name>.json`, `<name>.py`, an optional `<name>.js` and `test_<name>.py`.
  - `report/` holds script/query reports.
  - `api/patient_portal.py` holds the whitelisted endpoints for the portal SPA.
  - `custom_doctype/` holds overrides and extensions of ERPNext doctypes such as Sales Invoice and Payment Entry.
  - `utils.py` holds shared helpers, including billing.
  - The remaining folders hold desk artefacts: dashboards, number cards, workspaces, web forms, print formats, pages and onboarding.
- `healthcare/controllers/` holds cross-doctype controllers (`service_request_controller.py`) and link queries (`queries.py`).
- `healthcare/regional/india/` holds the ABDM integration.
- `healthcare/patches/` (`v0_0`, `v15_0`, `v16_0`) plus `patches.txt` (with a `[pre_model_sync]` section) hold data migrations.
- `healthcare/setup.py`, `install.py`, `uninstall.py` and `after_migrate.py` hold the lifecycle hooks.
- `healthcare/public/js/` holds desk JS. `healthcare/www/` holds the portal page entry (`patient_portal.html/.py`).
- `patient_portal/` holds the Vue SPA source. It calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources and socket.io. Its build output goes to `healthcare/public/patient_portal/assets`, and it renders through `healthcare/www/patient_portal.html`.
- `healthcare/tests/` holds the shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).

Dependency direction: healthcare → erpnext → frappe. ERPNext behaviour is extended through hooks and overrides, never by editing ERPNext.
