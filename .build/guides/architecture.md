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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - patient_portal/src/socket.js
  - healthcare/public/js/healthcare.bundle.js
---

The repo is one **Frappe app (`healthcare`)** plus a separately built Vue SPA.

```
healthcare/                  # the Frappe app package (installed via `bench get-app healthcare`)
  hooks.py                   # wiring: doc_events, scheduler_events, overrides, jinja, portal, permissions
  install.py / setup.py / uninstall.py / after_migrate.py
  patches.txt + patches/v0_0|v15_0|v16_0/   # data migrations (pre_model_sync / post_model_sync)
  controllers/               # shared controllers (queries.py, service_request_controller.py)
  healthcare/                # the "Healthcare" module (modules.txt)
    doctype/<snake_name>/    # ~138 DocTypes: <name>.json schema, <name>.py controller, <name>.js form script, test_<name>.py
    custom_doctype/          # overrides/extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py    # whitelisted API for the portal
    report/, page/, print_format/, web_form/, dashboard_chart*/, number_card/, workspace/, onboarding_step/
    utils.py, healthcare.py, auth.py
  regional/india/            # ABDM integration
  public/js/                 # desk JS bundled via healthcare.bundle.js
  public/frontend/           # built portal assets (generated)
  www/                       # website routes: patient_portal.html/.py, patient-portal/
  workspace_sidebar/*.json, desktop_icon/, templates/, locale/main.pot
  tests/                     # shared test bootstrap (utils.py, test_utils.py)
patient_portal/              # Vue 3 + frappe-ui SPA; builds into healthcare/public/... and healthcare/www/patient_portal.html
wiki/                        # design docs & user guides
```

**How the parts call each other**
- Frappe loads `hooks.py`. Hooks bind ERPNext doctypes to healthcare code: Sales Invoice (`override_doctype_class` → `HealthcareSalesInvoice`, plus validate/submit/cancel hooks), Payment Entry, Company and Patient.
- A wildcard `"*"` doc_event syncs Patient Medical Records on submit, cancel and update-after-submit for every doctype.
- Scheduler jobs live as module-level functions inside doctype controllers, for example `patient_appointment.send_appointment_reminder` and `update_appointment_status`.
- DocType controllers import each other directly by dotted path, e.g. `healthcare.healthcare.doctype.fee_validity.fee_validity`. They also call ERPNext (`erpnext.setup...`) and `healthcare.healthcare.utils`.
- The browser reaches the server through `@frappe.whitelist()` functions:
  - desk JS uses `frappe.call` / `frm.call`;
  - the portal uses frappe-ui `createResource` against `healthcare.healthcare.api.patient_portal.*`.
- Realtime: the portal opens a socket.io connection and refetches cached resources on `refetch_resource` events.
- Schema lives in DocType JSON. Data changes to existing sites go through patches listed in `patches.txt`.
