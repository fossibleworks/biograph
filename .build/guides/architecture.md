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
  - patient_portal/src/PatientPortal.vue
  - healthcare/tests/utils.py
  - healthcare/patches.txt
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # the Frappe app package (installed with `bench install-app healthcare`)
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, jinja, install hooks
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py   # whitelisted endpoints used by the Vue portal
    custom_doctype/         # extensions of ERPNext doctypes (HealthcareSalesInvoice, payment_entry hooks)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                # cross-doctype helpers (billing, invoice hooks, barcodes)
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/abdm/      # India ABDM integration
  patches/v0_0|v15_0|v16_0  # data migrations, registered in patches.txt
  public/js/                # desk JS (healthcare.bundle.js, sales_invoice.js, observation widgets…)
  public/frontend/          # built portal assets
  www/patient_portal.*      # Jinja shell page that boots the SPA
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
patient_portal/             # Vue 3 + frappe-ui SPA source (src/components/*.vue)
wiki/                       # fork design docs and the upstream-sync ledger
```

**How the parts call each other**
- **ERPNext → healthcare** through `hooks.py`:
  - `doc_events` on Sales Invoice, Payment Entry, Company and Patient.
  - The wildcard `*` on_submit/on_cancel creates or deletes Patient Medical Records.
  - `override_doctype_class` replaces Sales Invoice with `HealthcareSalesInvoice`.
- **Scheduler**: appointment reminders (`all`). Appointment status, fee validity, inpatient billables and expired medication requests run `daily`.
- **Desk JS → Python** through `frappe.call` / `frm.call` to `@frappe.whitelist()` methods. There are roughly 180 of them, most living in the doctype controller modules.
- **Patient Portal → Python** through frappe-ui `createResource` calls to `healthcare.healthcare.api.patient_portal.*`.
- **Healthcare → ERPNext** through direct imports (`import erpnext`, ERPNext doctypes such as Item, Sales Invoice and POS Profile).
- **Upstream relationship**: this fork tracks earthians/marley `version-16`. Upstream commits are cherry-picked with `-x`, and fork behaviour wins conflicts. See `wiki/upstream-sync-version-16.md`.
