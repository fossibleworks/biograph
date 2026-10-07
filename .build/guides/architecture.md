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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

This is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Frappe app package (python module `healthcare`)
  hooks.py                  # wiring into Frappe/ERPNext: doc_events, scheduler, overrides, jinja, portal
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: <name>.json, <name>.py, <name>.js, test_<name>.py
    api/patient_portal.py   # whitelisted endpoints consumed by the Vue portal
    custom_doctype/         # ERPNext overrides (HealthcareSalesInvoice, payment_entry hooks)
    report/, page/, print_format/, web_form/, workspace/, dashboard_chart*/, number_card/
    utils.py                # shared billing/invoice helpers used by hooks
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/abdm/      # regional integration (ABDM)
  patches/v0_0|v15_0|v16_0/ # data migrations, registered in patches.txt
  public/js/                # desk JS, bundled via healthcare.bundle.js
  public/frontend/          # built portal assets (generated)
  www/patient_portal.*      # server page hosting the SPA
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData
  setup.py, install.py, after_migrate.py, uninstall.py
patient_portal/             # Vue 3 + frappe-ui SPA source, builds into healthcare/public
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the parts connect**
- **ERPNext integration goes through `hooks.py`, not by patching core:**
  - `override_doctype_class` replaces Sales Invoice with `HealthcareSalesInvoice`.
  - `doc_events` on Sales Invoice, Payment Entry, Company and Patient.
  - A wildcard `"*"` `on_submit`/`on_cancel` hook keeps Patient Medical Records in sync.
  - `doctype_js` extends ERPNext forms.
- **Scheduled jobs** (`scheduler_events`): appointment reminders, appointment-status updates, fee validity, inpatient billables, expiry of medication requests.
- **DocType controllers** live next to their JSON schema. Cross-doctype logic sits in `healthcare/healthcare/utils.py` and `controllers/`.
- **Patient Portal**: the Vue SPA calls `@frappe.whitelist()` methods in `healthcare.healthcare.api.patient_portal` through frappe-ui resources. `has_website_permission` hooks restrict what a portal user can read.
- **Schema changes ship as DocType JSON.** Data fixes ship as patches listed under `[pre_model_sync]` or `[post_model_sync]` in `patches.txt`.

**Fork policy:** `biograph-fh` is the fork's main branch. Upstream commits are cherry-picked with `-x`, and when the fork and upstream conflict, the fork's intent wins (see `wiki/upstream-sync-version-16.md`).
