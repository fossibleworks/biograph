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
  - healthcare/patches.txt
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/www/patient_portal.py
---

# Architecture

This is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Python package = Frappe app
  hooks.py                  # app wiring: doc_events, scheduler_events, override_doctype_class, jinja, install hooks
  modules.txt               # single module: Healthcare
  patches.txt, patches/     # data migrations (v0_0, v15_0, v16_0), pre/post_model_sync
  controllers/              # shared controllers (queries.py, service_request_controller.py)
  regional/india/           # ABDM integration
  config/, desktop_icon/, workspace_sidebar/
  www/patient_portal.{py,html}  # web route serving the SPA shell
  public/js/                # desk JS bundle + shared form helpers
  public/frontend/          # built SPA assets
  tests/                    # BootStrapTestData master-data fixtures
  healthcare/               # module "Healthcare"
    doctype/<snake_name>/   # DocType: <name>.json, <name>.py, <name>.js, test_<name>.py
    custom_doctype/         # overrides for ERPNext docs (HealthcareSalesInvoice, payment_entry)
    api/patient_portal.py   # @frappe.whitelist RPC used by the SPA
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    setup/, utils.py, auth.py
patient_portal/             # Vue 3 + frappe-ui SPA (src/components/*.vue)
wiki/                       # feature design + usage docs
```

## How the pieces call each other
- **ERPNext integration** goes through `hooks.py`. `doc_events` on Sales Invoice, Payment Entry, Company and Patient call into `healthcare.healthcare.utils` / `custom_doctype`. A `"*"` handler on submit, cancel and update-after-submit keeps Patient Medical Records in sync. `override_doctype_class` swaps in `HealthcareSalesInvoice`.
- **Scheduler** jobs live on DocType modules: appointment reminders and status, fee validity, inpatient billables, medication request expiry.
- **DocType controllers** subclass `frappe.model.document.Document`. Module-level `@frappe.whitelist()` functions are the RPC surface that desk JS (`frappe.call`) and the SPA call.
- The **Patient Portal SPA** calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources. Its build output feeds `healthcare/www/patient_portal.html`.
- **Schema changes** are made in DocType JSON. Data migrations go in a patch module listed in `patches.txt`.
