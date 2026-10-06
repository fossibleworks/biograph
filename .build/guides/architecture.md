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
  - healthcare/modules.txt
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

The app follows the standard Frappe app layout. Everything lives in the single module `Healthcare` (`healthcare/modules.txt`).

```
healthcare/                  # Frappe app package (app_name = healthcare)
  hooks.py                   # wiring: doc_events, scheduler_events, doctype_js, overrides, portal menu, jinja
  healthcare/                # the "Healthcare" module
    doctype/<snake_name>/    # one dir per DocType: <name>.json (schema), <name>.py (controller), <name>.js (form), test_<name>.py
    api/patient_portal.py    # whitelisted endpoints used by the Vue portal
    custom_doctype/          # extensions of ERPNext doctypes (HealthcareSalesInvoice, payment_entry hooks)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    setup/                   # setup helpers (e.g. patient_duplicate_check.py)
    utils.py                 # shared billing/invoice helpers used by doc_events
  controllers/               # shared controllers (service_request_controller.py, queries.py)
  regional/india/            # ABDM integration
  patches/ + patches.txt     # data migrations (v0_0, v15_0, v16_0), [pre_model_sync]/[post_model_sync]
  public/js/                 # desk JS bundled via healthcare.bundle.js
  public/frontend/           # built patient-portal assets
  www/patient_portal.{html,py}  # portal entry page
  tests/utils.py             # HealthcareTestSuite + BootStrapTestData
patient_portal/              # Vue 3 + frappe-ui SPA source (builds into healthcare/public + www)
wiki/                        # fork design/usage docs and upstream-sync ledger
```

**How the pieces connect:**
- `hooks.py` subscribes Healthcare code to ERPNext documents. Sales Invoice, Payment Entry and Company events go to `healthcare.healthcare.utils` and `custom_doctype/*`. A `"*"` doc_event mirrors submitted records into Patient Medical Record. Sales Invoice is replaced with `HealthcareSalesInvoice`.
- DocType controllers import each other directly, for example `patient_appointment.py` imports `fee_validity` and `api.patient_portal`. They call ERPNext modules such as `erpnext.setup...is_holiday`.
- The Vue portal reaches the backend only through `@frappe.whitelist()` methods, mostly in `healthcare/healthcare/api/patient_portal.py`, using frappe-ui `createResource`.
- Scheduled jobs (appointment reminders, daily status and validity updates, IP billables, expired medication requests) live as functions inside DocType controller modules and are registered in `scheduler_events`.
- Schema changes are made in DocType JSON. Data migrations go in `healthcare/patches/vXX_0/*.py` and are listed in `patches.txt`.
