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
---

The repo is a single Frappe app (`healthcare`) plus a Vue SPA source folder.

```
healthcare/                  # Frappe app package
  hooks.py                   # wiring: doc_events, scheduler_events, overrides, portal, jinja, install hooks
  healthcare/                # the "Healthcare" module
    doctype/<snake_name>/    # one dir per DocType: .json schema, .py controller, .js form script, test_*.py
    custom_doctype/          # overrides/hooks for ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py    # whitelisted endpoints consumed by the Vue portal
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                 # shared billing/invoice helpers referenced from hooks
    setup/                   # install-time data (e.g. patient duplicate check rules)
  controllers/               # shared controllers (service_request_controller.py, queries.py)
  regional/india/            # ABDM integration
  patches/v*_0/ + patches.txt# data migrations
  tests/utils.py             # BootStrapTestData + HealthcareTestSuite
  www/                       # portal routes (patient-portal/, patient_portal.html)
  public/js                  # desk JS bundles; public/frontend = built SPA assets
patient_portal/src           # Vue 3 SPA source -> built into healthcare/public + www html
wiki/                        # fork feature docs, design notes, upstream sync ledger
```

**How the parts connect**
- Frappe loads all behaviour through `hooks.py`. `doc_events` attach healthcare logic to ERPNext doctypes (Sales Invoice, Payment Entry, Company) and to every submitted doc (`"*"` → medical record creation). `override_doctype_class` replaces Sales Invoice with `HealthcareSalesInvoice`. `scheduler_events` run appointment reminders and daily status updates.
- DocType controllers import each other through absolute dotted paths, e.g. `healthcare.healthcare.doctype.patient_appointment.patient_appointment`. They also import ERPNext modules directly.
- The Vue portal calls `@frappe.whitelist()` methods in `healthcare/healthcare/api/patient_portal.py` through frappe-ui resources. Vite writes the build into `healthcare/public/...` and `healthcare/www/patient_portal.html`.
- Desk form JS calls server methods with `frappe.call` / `frm.call`.
