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
  - healthcare/healthcare/doctype/lab_test/lab_test.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - patient_portal/vite.config.js
---

# Architecture

This is a single Frappe app (`healthcare`) with a separate Vue SPA in the same repo.

```
healthcare/                 # Frappe app package (python module 'healthcare')
  hooks.py                  # wiring: doc_events, scheduler_events, doctype_js, jinja, on_login, fixtures
  healthcare/               # the 'Healthcare' module
    doctype/<name>/         # one folder per DocType: <name>.json, <name>.py (controller), <name>.js (form), test_<name>.py, *_list.js, *_dashboard.py
    api/patient_portal.py   # @frappe.whitelist() endpoints consumed by the Vue portal
    utils.py                # shared business logic (invoice hooks, billing items, barcodes)
    custom_doctype/         # overrides of ERPNext doctypes (Sales Invoice, Payment Entry)
    report/, page/, print_format/, dashboard_chart*/, number_card/, workspace/, web_form/
    setup/                  # setup routines (e.g. patient_duplicate_check)
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/           # ABDM etc.
  patches/v15_0, v16_0/     # data migrations, registered in patches.txt
  public/js/                # Desk client scripts bundled via healthcare.bundle.js
  www/patient_portal.*      # portal page shell; built SPA assets under public/patient_portal
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
patient_portal/             # Vue 3 + frappe-ui SPA (src/components, src/utils)
wiki/                       # fork feature/design docs and upstream-sync ledger
```

## How the pieces call each other
- **ERPNext integration through hooks.** Some `doc_events` apply to all doctypes (`"*"`) and keep the medical record history in sync. Others hook into ERPNext doctypes, e.g. Sales Invoice `validate`/`on_submit`/`on_cancel` call `healthcare.healthcare.utils.manage_invoice_*`.
- **Scheduler jobs** live in doctype controllers. Examples: appointment reminders and status updates, fee validity, inpatient billables, expired medication requests.
- **DocType controllers** are `Document` subclasses that use lifecycle methods (`validate`, `on_submit`, `on_cancel`). They import helpers from sibling doctypes using full dotted paths (`healthcare.healthcare.doctype.x.x`). Service Request status propagates through `update_service_request_status`.
- **Patient Portal** calls whitelisted methods in `healthcare/healthcare/api/patient_portal.py` through frappe-ui resources, with the frappe proxy in dev. It uses socket.io (`src/socket.js`) for realtime updates.
- **Background work** goes through `frappe.enqueue`, e.g. recurring appointments and sample collection.
- **Upstream relationship.** The fork branch `biograph-fh` tracks `earthians/marley` `version-16` by cherry-picking commits. The wiki ledger records the conflict policy: "fork intent wins".
