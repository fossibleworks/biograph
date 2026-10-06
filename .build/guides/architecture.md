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
  - patient_portal/vite.config.js
  - healthcare/www/patient_portal.py
  - healthcare/patches.txt
  - healthcare/controllers/service_request_controller.py
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA.

**`healthcare/` (the app package)**
- `hooks.py` is the integration point with Frappe and ERPNext. It holds:
  - `doctype_js` (adds healthcare JS to ERPNext forms)
  - `override_doctype_class` (for example, the Sales Invoice and Payment Entry overrides in `healthcare/healthcare/custom_doctype/`)
  - `doc_events` on ERPNext documents
  - `scheduler_events` (appointment reminders on `all`; daily status updates for appointments, fee validity, inpatient billables and medication requests)
  - install and uninstall hooks (`install.py`, `setup.py`, `uninstall.py`)
- `healthcare/healthcare/` is the module:
  - `doctype/<snake_name>/` holds one folder per DocType: `<name>.json` (schema), `<name>.py` (controller class that subclasses `Document`), `<name>.js` (form script), `test_<name>.py`, and optional `_list.js` and `_dashboard.py` files.
  - `api/patient_portal.py` holds the whitelisted endpoints the portal SPA calls.
  - `utils.py` holds shared billing and helper logic.
  - `report/`, `page/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `print_format/`, `web_form/` and `setup/` hold the other module content.
- `healthcare/controllers/` holds shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/` holds India-specific features.
- `healthcare/patches/v0_0`, `v15_0` and `v16_0` hold data migrations, registered in `healthcare/patches.txt`.
- `healthcare/public/js/` holds the desk JS bundle. `healthcare/public/frontend/` holds the built portal assets.
- `healthcare/www/patient_portal.{html,py}` is the portal's Jinja entry page.
- `healthcare/tests/` holds shared test bootstrapping (`utils.py` with `HealthcareTestSuite` and `BootStrapTestData`).
- `healthcare/locale/main.pot` holds the translatable strings.

**`patient_portal/` (Vue SPA)**
- Built with Vite into the app's public assets.
- Talks to the backend only through `frappe-ui` resource calls to `healthcare.healthcare.api.patient_portal.*`. It uses the Frappe proxy and Jinja boot data.

**Dependency direction:** `frappe` → `erpnext` → `healthcare`. Imports follow the same order (an isort section exists for each). DocType controllers import each other directly by full module path (for example, `patient_appointment.py` imports from `fee_validity`, `healthcare_settings` and `patient_insurance_coverage`).

**Other directories:** `wiki/` holds design and usage docs. `public/js/` at the repo root holds a stray desk script.
