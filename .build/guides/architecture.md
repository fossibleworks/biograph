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

The repo is one Frappe app (`healthcare`) plus a separate Vue SPA.

**`healthcare/` (app package)**
- `hooks.py` is the integration hub. It defines:
  - `doc_events`: `*` on_submit/on_cancel creates or deletes Patient Medical Records, plus hooks on Sales Invoice, Payment Entry, Company and Patient.
  - `override_doctype_class`
  - `scheduler_events`: appointment reminders, and daily status updates for appointments, fee validity, inpatient billables and medication requests.
  - `jinja` methods, `doctype_js` for ERPNext doctypes, and `on_login`.
- `healthcare/healthcare/` is the main module:
  - `doctype/`: about 138 doctypes. Each folder holds `<name>.json` (schema), `<name>.py` (controller class extending `Document`), `<name>.js` (form script), and `test_<name>.py`.
  - `api/patient_portal.py`: whitelisted endpoints for the portal.
  - `custom_doctype/`: overrides and handlers for ERPNext doctypes (sales_invoice, payment_entry).
  - `utils.py`: shared billing and invoice logic.
  - Also `report/`, `page/` (patient_history, patient_progress), `dashboard_chart*`, `number_card`, `workspace`, `print_format`, `web_form`, `setup`.
- `healthcare/controllers/`: shared controllers (service_request_controller, queries).
- `healthcare/regional/india/abdm`: regional integration.
- `healthcare/patches/` with `patches.txt`: versioned migrations (`v15_0`, `v16_0`).
- `healthcare/public/`: desk JS (`js/`) and the built portal assets (`frontend/`).
- `healthcare/www/`: website routes, including `patient-portal/`.
- `healthcare/tests/`: shared test bootstrap (`utils.py`).
- `healthcare/locale/main.pot`: translatable strings.

**`patient_portal/` (Vue SPA)** talks to the backend only through `frappe-ui` resources that call whitelisted methods in `healthcare/healthcare/api/patient_portal.py`, plus socket.io (`src/socket.js`). Vite builds it into the app's `public` folder, and it is served through a `www` HTML entry.

**Dependency direction:** `healthcare` → `erpnext` → `frappe`. Business logic belongs on the server; the PR template says *All business logic and validations must be on the server-side*.
