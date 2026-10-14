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
---

# Architecture

This is a single Frappe app (`healthcare`) plus a separately built Vue SPA.

```
healthcare/                 Frappe app package (python module "healthcare")
  hooks.py                  App wiring: doc_events, scheduler_events, doctype_js, overrides, portal routes
  healthcare/               The "Healthcare" module (modules.txt)
    doctype/<snake_name>/   One folder per DocType: <name>.json (schema), <name>.py (controller),
                            <name>.js (Desk form script), *_list.js / *_tree.js, test_<name>.py
    api/patient_portal.py   @frappe.whitelist() endpoints consumed by the Vue portal
    custom_doctype/         Overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    utils.py                Shared billing/invoice helpers wired via hooks (manage_invoice_*)
    report/, page/, print_format/, dashboard_chart*/, number_card/, workspace/, web_form/
  controllers/              Shared base controllers (service_request_controller.py, queries.py)
  regional/india/           Region-specific logic (ABDM)
  patches/ + patches.txt    Data migrations (v0_0, v15_0, v16_0)
  public/js/                Desk JS bundle (healthcare.bundle.js) and shared form helpers
  public/frontend/          Built patient-portal assets (generated)
  www/                      Website routes (patient_portal.html/.py, patient-portal/)
  tests/utils.py            Shared test bootstrap (HealthcareTestSuite / BootStrapTestData)
  locale/main.pot           Translatable strings
patient_portal/             Vue 3 + frappe-ui SPA source; builds into healthcare/public + www
public/js/                  Misc legacy JS
wiki/                       Fork design docs, usage docs, upstream-sync ledgers
```

## How the parts depend on each other
- `healthcare` depends on **frappe** and **erpnext**. Imports are grouped in that order: frappe → erpnext → healthcare.
- ERPNext doctypes are extended through `hooks.py` `doc_events` (for example, Sales Invoice submit/cancel/validate → `healthcare.healthcare.utils`), `doctype_js`, and `custom_doctype/`. Do not edit ERPNext itself.
- A wildcard `doc_events["*"]` hook creates and updates Patient Medical Records on submit/cancel. Every submittable doctype goes through it.
- Background jobs are declared in `scheduler_events`: appointment reminders, and daily status updates for appointments, fee validity, IP billables, and medication requests.
- The Vue portal reaches the server only through `frappe-ui` resources that call whitelisted methods in `healthcare/healthcare/api/patient_portal.py`. The portal holds no business logic. The PR template says all validation must stay server-side.
- Doctype modules import each other directly. Tests also import factory helpers from other doctypes' tests (for example, `create_appointment` from `test_patient_appointment`).
