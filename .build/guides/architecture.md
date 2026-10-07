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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/tests/utils.py
---

Biograph is one Frappe app (`healthcare/`) plus one Vue SPA (`patient_portal/`).

**`healthcare/` (app root)**
- `hooks.py` is the integration point with Frappe and ERPNext. It holds `doc_events` (a `*` hook that creates Patient Medical Records on submit; Sales Invoice, Payment Entry, Company and Patient hooks), `scheduler_events` (appointment reminders, daily status updates), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `jinja` methods, `has_website_permission`, `standard_queries`, and `on_login` (role-based home page).
- `healthcare/healthcare/` is the main module. It contains:
  - `doctype/<snake_name>/`: about 139 DocTypes. Each folder holds `<name>.json` (schema), `<name>.py` (controller, a `Document` subclass), `<name>.js` (desk form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
  - `custom_doctype/`: overrides and handlers for ERPNext doctypes (`sales_invoice.py`, `payment_entry.py`).
  - `api/patient_portal.py`: `@frappe.whitelist()` endpoints called by the portal.
  - `utils.py` (shared billing and invoice helpers), `auth.py`, `report/`, `page/`, `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/`, `onboarding_step/`.
- `controllers/`: shared controller logic (e.g. `service_request_controller.py`, `queries.py`).
- `regional/india/abdm/`: India ABDM integration.
- `patches/` + `patches.txt`: versioned data migrations (`v15_0`, `v16_0`, …).
- `setup.py` / `install.py` / `uninstall.py` / `after_migrate.py`: lifecycle hooks.
- `public/js/`: desk JS bundle and shared widgets. `public/frontend/`: built portal assets.
- `www/patient_portal.html|py`: the portal page that serves the SPA.
- `tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`, `BootStrapTestData`).

**`patient_portal/`**: the Vue SPA (`src/PatientPortal.vue`, `src/components/*Model.vue`). It calls whitelisted Python methods with frappe-ui `createResource`. The Vite build writes into `healthcare/public/...` and `healthcare/www/patient_portal.html`.

**Dependency direction:** portal → `healthcare.healthcare.api` → doctype controllers → `frappe` / `erpnext`. ERPNext documents call back into healthcare only through `hooks.py`. Do not import healthcare code from ERPNext.
