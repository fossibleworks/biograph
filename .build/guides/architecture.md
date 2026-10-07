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
  - patient_portal/vite.config.js
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/tests/utils.py
  - healthcare/patches.txt
---

The repo root is the Frappe app `healthcare`, and it is installed into a bench next to frappe and erpnext.

```
healthcare/                 # Python package (app root)
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, standard_queries, doctype_js
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py   # whitelisted endpoints used by the portal
    custom_doctype/         # overrides of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    report/, page/, dashboard_chart_source/, number_card/, workspace/, print_format/, web_form/
    utils.py                # shared helpers (billing, settings lookups)
  controllers/              # cross-doctype controllers (queries.py, service_request_controller.py)
  regional/                 # country-specific logic
  patches/ + patches.txt    # data migrations (v15_0, v16_0 ...)
  setup.py, install.py, after_migrate.py, uninstall.py
  public/js/                # desk JS bundle and doctype_js includes
  www/                      # web routes (patient_portal.html/.py, patient-portal)
  tests/utils.py            # BootStrapTestData + HealthcareTestSuite
  locale/main.pot           # translations source
patient_portal/             # Vue 3 + frappe-ui SPA; Vite builds into healthcare/public/patient_portal/assets, served via healthcare/www/patient_portal.html
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the parts call each other:**
- DocType controllers import each other directly by module path, for example `patient_appointment.py` imports from `fee_validity`, `healthcare_settings` and `api.patient_portal`.
- ERPNext integration goes through `hooks.py`: `doc_events` and `override_doctype_class` (for example Sales Invoice) plus ERPNext imports such as `erpnext.setup.doctype.employee.employee`.
- The Vue portal calls whitelisted Python methods through frappe-ui resources and uses a socket.io client (`src/socket.js`).
- Background work runs through `frappe.enqueue` and `scheduler_events`.
