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
  - healthcare/patches.txt
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Frappe app package (bench app root)
  hooks.py                  # wiring: doc_events, scheduler_events, doctype_js, jinja, on_login
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form, test_*.py
    api/patient_portal.py   # whitelisted endpoints used by the portal SPA
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                # shared billing/invoice helpers hooked into Sales Invoice
    auth.py                 # role-based home page on login
  controllers/              # shared controllers (service_request_controller.py, queries.py)
  regional/india/           # regional (ABDM) logic
  setup/, install.py, uninstall.py, after_migrate.py
  patches/v15_0, v16_0 + patches.txt   # data migrations
  public/js/                # desk JS bundled via healthcare.bundle.js
  www/patient_portal.*      # portal entry page (Jinja) for the SPA
  tests/utils.py            # BootStrapTestData + HealthcareTestSuite
  locale/main.pot           # translations
patient_portal/             # Vue 3 + frappe-ui SPA, builds into healthcare/public/…
wiki/                       # fork design docs and the upstream-sync ledger
```

**How the parts connect:**
- The app plugs into Frappe and ERPNext through `hooks.py`. Wildcard `doc_events` create, update and delete Patient Medical Records on submit, update-after-submit and cancel. Sales Invoice `validate`, `on_submit` and `on_cancel` call `healthcare.healthcare.utils`. `Company.after_insert` creates the service unit tree root. `scheduler_events` handle appointment reminders, status updates, fee validity, inpatient billables and expired medication requests.
- DocType controllers subclass `frappe.model.document.Document`. They call each other by dotted path and through `frappe.get_doc` / `frappe.db`. Client JS calls server methods marked `@frappe.whitelist()`.
- The SPA calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui `createResource`, and uses socket.io (`src/socket.js`).
- ERPNext is a hard dependency for items, customers, invoices, companies and stock.
