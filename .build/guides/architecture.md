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
  - pyproject.toml
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Architecture

The repo is one Frappe app named `healthcare`, plus a separate Vue SPA for the patient portal.

## Top-level layout
- `healthcare/`: the Python package for the Frappe app.
  - `hooks.py`: the integration point with Frappe and ERPNext. It declares:
    - `doc_events` on `*`, Sales Invoice, Payment Entry, Company and Patient
    - `scheduler_events` (appointment reminders, daily status updates, fee validity, inpatient billables, expired medication requests)
    - `override_doctype_class` (Sales Invoice → `HealthcareSalesInvoice`)
    - jinja methods, portal menu items, website permissions, standard queries, and install/migrate hooks
  - `healthcare/healthcare/`: the main module.
    - `doctype/<snake_name>/`: one folder per DocType (139 of them) holding `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (form script), and optional `<name>_list.js`, `<name>_tree.js`, `<name>_dashboard.py` and `test_<name>.py`.
    - `report/`, `page/` (patient_history, patient_progress), `print_format/`, `web_form/`, `workspace/`, `dashboard_chart*/`, `number_card/` and onboarding folders.
    - `api/patient_portal.py`: the whitelisted endpoints the Vue portal calls.
    - `custom_doctype/`: extensions to ERPNext doctypes (Sales Invoice, Payment Entry).
    - `utils.py`: shared billing and invoice logic used by many doctypes and hooks.
  - `controllers/`: shared controllers such as `service_request_controller.py` and `queries.py`.
  - `regional/india/abdm`: India-specific ABDM integration.
  - `patches/` plus `patches.txt`: versioned data migrations (`v15_0`, `v16_0`).
  - `setup.py`, `install.py`, `uninstall.py`, `after_migrate.py`: lifecycle code.
  - `public/js`: Desk JS (`healthcare.bundle.js`, shared form helpers, observation widgets).
  - `public/frontend`: the built portal assets.
  - `www/patient_portal.*`: the portal page shell.
  - `tests/utils.py`: test bootstrap data and `HealthcareTestSuite`.
  - `locale/main.pot`: translatable strings.
- `patient_portal/`: the Vue 3 and frappe-ui SPA. It calls `healthcare.healthcare.api.patient_portal.*` through `frappeRequest` and builds into `healthcare/public` and `healthcare/www/patient_portal.html`.
- `wiki/`: fork design docs and usage docs.
- `.github/`: CI workflows and helper scripts.

## Dependency direction
- `healthcare` depends on `frappe` and `erpnext`. Imports are sectioned in the order frappe → erpnext → healthcare.
- Doctype controllers import helpers from other doctypes' modules, for example `patient_appointment` imports from `patient_insurance_coverage` and `healthcare.healthcare.utils`.
- Cross-cutting behaviour goes through `hooks.py` rather than by monkey-patching ERPNext.
- Business logic and validation live on the server, in controllers and whitelisted functions. JS only handles UI behaviour; the PR template says this.
- Schema changes go in the doctype JSON. Data fixes go in a patch registered in `patches.txt`.
