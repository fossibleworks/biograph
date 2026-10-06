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
  - pyproject.toml
---

This is one Frappe app (`healthcare`) plus a Vue SPA. Everything runs inside a Frappe bench next to `frappe` and `erpnext`.

**Top-level layout**
- `healthcare/`: the Frappe app package.
  - `hooks.py`: the integration point with Frappe and ERPNext. It holds `doc_events` (a wildcard `*` hook that writes medical records, plus Sales Invoice, Payment Entry, Company and Patient hooks), `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`), `doctype_js`, and `scheduler_events` (appointment reminders, daily status, fee-validity and medication-request updates).
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType, containing `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), optional `_list.js`/`_calendar.js`, and `test_<name>.py`.
    - `custom_doctype/`: overrides and hooks for ERPNext doctypes (sales_invoice, payment_entry).
    - `api/patient_portal.py`: whitelisted endpoints for the portal SPA.
    - `utils.py`: shared billing and invoice helpers.
    - `report/`, `page/`, `print_format/`, `dashboard_chart*`, `number_card`, `workspace`, `web_form`, `setup/`.
  - `controllers/`: shared controllers (`service_request_controller.py`, `queries.py` link-field queries).
  - `regional/india/abdm/`: regional (ABDM) integration.
  - `patches/` + `patches.txt`: versioned data migrations (`v15_0`, `v16_0`).
  - `public/js/`: Desk JS bundle. `public/frontend/` and `public/patient_portal/assets`: built SPA output.
  - `www/patient_portal.{html,py}`: the server-rendered shell for the SPA.
  - `tests/utils.py`: `HealthcareTestSuite` and bootstrap master data.
  - `install.py`, `uninstall.py`, `after_migrate.py`, `permissions.py`.
- `patient_portal/`: the Vue 3 and frappe-ui SPA. It calls `healthcare.healthcare.api.patient_portal.*` through the frappe-ui proxy, and its build output goes to `healthcare/public/patient_portal/assets`.
- `wiki/`: design notes, usage docs and the upstream-sync ledger.
- `.github/`: CI workflows and helper scripts.
- `.build/`, `.claude/`, `.cursor/`, `AGENTS.md`: Interactor Build managed rule mirrors.

**Dependency direction:** `healthcare` imports from `frappe` and `erpnext`, never the other way round. ERPNext behaviour is changed only through hooks or class overrides, never by editing ERPNext. Imports follow the isort section order future → stdlib → third-party → frappe → erpnext → healthcare.
