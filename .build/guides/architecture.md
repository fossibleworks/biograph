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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - patient_portal/vite.config.js
  - healthcare/www/patient_portal.py
  - healthcare/patches.txt
---

The repo holds one Frappe app (`healthcare`) and a separate Vue SPA (`patient_portal`).

**`healthcare/`** is the app package:
- `hooks.py` is the wiring hub. It contains `doc_events`, which hook into ERPNext `Sales Invoice`, `Payment Entry`, `Company` and `Patient`, plus a wildcard `*` hook that writes Patient Medical Records. It also holds `scheduler_events` (appointment reminders, daily status updates), `override_doctype_class` (`HealthcareSalesInvoice`), Jinja methods, install/migrate hooks, portal permissions and standard queries.
- `healthcare/healthcare/` is the main module:
  - `doctype/<snake_name>/`: about 139 doctypes. Each has `.json` metadata, a `.py` controller, a `.js` form script and a `test_*.py`.
  - `api/patient_portal.py`: whitelisted endpoints that the SPA calls.
  - `custom_doctype/`: extensions of ERPNext doctypes.
  - `report/`, `page/`, `web_form/`, `print_format/`, `workspace/`, `dashboard_chart/`, `number_card/`, `onboarding_step/`.
  - `utils.py`: shared billing and invoice helpers.
- `controllers/` holds shared controllers such as `service_request_controller.py` and `queries.py`.
- `regional/india/abdm` holds the ABDM integration.
- `patches/v0_0|v15_0|v16_0` plus `patches.txt` hold data migrations that run on `bench migrate`.
- `setup.py` / `install.py` / `uninstall.py` / `after_migrate.py` handle the install lifecycle.
- `public/js` holds desk scripts. `public/frontend` and `public/patient_portal` hold the built SPA assets.
- `www/patient_portal.{py,html}` is the server-rendered shell for the SPA.
- `tests/utils.py` holds the shared test bootstrap.

**`patient_portal/`** is a Vite/Vue app. It builds into `healthcare/public/patient_portal/assets` and writes its HTML into `healthcare/www/patient_portal.html`. It talks to the backend through frappe-ui resources (`/api/method/...`) and Socket.IO (`socket.js`).

**How dependencies flow:**
- The SPA calls whitelisted Python methods.
- Desk JS calls `frappe.call` on controller methods.
- Controllers use the Frappe ORM (`frappe.get_doc`, `frappe.db`, `frappe.qb`) and ERPNext APIs.
- ERPNext documents call back into healthcare through `doc_events`.
