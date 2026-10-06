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
  - patient_portal/vite.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This is a single Frappe app (`healthcare`) installed into a bench next to `frappe`, `erpnext` and `payments`.

```
healthcare/                 # app package (module root)
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, fixtures
  healthcare/               # the "Healthcare" module
    doctype/<name>/         # one dir per DocType: <name>.json, <name>.py, <name>.js, test_<name>.py
    custom_doctype/         # extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py   # whitelisted API consumed by the Vue portal
    report/ page/ dashboard_chart*/ number_card/ workspace/ print_format/ web_form/
    utils.py                # shared billing/invoicing helpers (large, central)
    setup.py                # install-time setup
  controllers/              # shared controllers (service_request_controller.py, queries.py)
  regional/india/abdm/      # country-specific integration
  patches/ + patches.txt    # data migrations, grouped v15_0/, v16_0/
  public/js/                # desk JS bundle (healthcare.bundle.js)
  public/frontend/ public/patient_portal/  # built portal assets
  www/patient_portal.*      # portal entry route (index HTML written by Vite build)
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
  locale/                   # main.pot + .po translations
patient_portal/             # Vue 3 + frappe-ui SPA source (src/components/*.vue)
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the parts call each other**
- DocType controllers are classes that subclass `frappe.model.document.Document`. They react to lifecycle hooks (`validate`, `on_submit`, `on_cancel`).
- ERPNext integration goes through `hooks.py`: `doc_events` on Sales Invoice, Payment Entry and Company, a wildcard `*` hook for medical records, and an `override_doctype_class` for Sales Invoice (`HealthcareSalesInvoice`).
- Background work runs from `scheduler_events` (appointment reminders, daily status updates) and `frappe.enqueue`.
- The portal calls whitelisted Python methods (`@frappe.whitelist()`) in `healthcare/healthcare/api/patient_portal.py` through frappe-ui resources.
- Business logic and validation belong on the server (PR template). Client JS only drives the UI.
