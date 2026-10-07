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
  - healthcare/controllers/queries.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/tests/utils.py
---

# Architecture

This is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Frappe app package
  hooks.py                  # wiring: doc_events, override_doctype_class, scheduler_events, standard_queries, includes
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one dir per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py   # whitelisted API used by the portal
    custom_doctype/         # overrides of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                # large shared helper module (billing items, invoicing, code values)
    setup/                  # setup routines, e.g. patient_duplicate_check
  controllers/              # shared controllers (service_request_controller.py, queries.py link-field queries)
  regional/india/           # regional extensions (ABDM)
  patches/ + patches.txt    # data migrations by version (v15_0, v16_0)
  public/js/                # desk JS bundled via healthcare.bundle.js
  public/frontend/          # built portal assets
  www/                      # web routes (patient-portal, patient_portal.html)
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
  locale/main.pot           # translation template
patient_portal/             # Vue 3 + frappe-ui SPA; builds into healthcare/public + healthcare/www
```

## How the parts call each other
- ERPNext integration is set up in `hooks.py`. `doc_events` and `override_doctype_class` hook into ERPNext documents (Sales Invoice, Payment Entry, Healthcare Practitioner). `doctype_js` adds client scripts to ERPNext forms.
- DocType controllers import each other directly (for example `patient_appointment.py` imports from `fee_validity`, `healthcare_settings` and `patient_insurance_coverage`). Shared logic lives in `healthcare/healthcare/utils.py`.
- Desk JS calls Python through `frappe.call` and `@frappe.whitelist()` methods, using dotted paths like `healthcare.healthcare.doctype.<x>.<x>.<fn>`.
- The portal SPA calls Frappe REST and whitelisted methods via frappe-ui resources (`createDocumentResource`, `getCachedListResource`) and `healthcare/healthcare/api/patient_portal.py`.
- Background work runs through `scheduler_events` (appointment reminders, daily status updates, IP billables, expired medication requests) and `frappe.enqueue`.

## Conventions
- Business logic and validation belong on the server, in DocType controllers (PR template rule).
- New schema changes need a patch under `healthcare/patches/vXX_0/` registered in `patches.txt`.
