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
  - patient_portal/src/patient_portal.js
  - healthcare/patches.txt
---

This is a single Frappe app (`healthcare`) plus one Vue SPA.

```
healthcare/                 # Frappe app package
  hooks.py                  # wiring: doctype_js, doc_events, scheduler_events, fixtures, app screen
  healthcare/               # the 'Healthcare' module
    doctype/<snake_name>/   # ~139 DocTypes: <name>.json (schema), <name>.py (controller), <name>.js (form), test_<name>.py
    api/patient_portal.py   # @frappe.whitelist endpoints used by the patient portal
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry, …)
    report/ page/ print_format/ workspace/ dashboard_chart/ number_card/ web_form/ setup/
    utils.py                # shared business logic (billing items, invoicing helpers)
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/           # country-specific logic
  patches/v15_0, v16_0 + patches.txt  # data migrations
  public/js/                # desk JS (healthcare.bundle.js, sales_invoice.js, observation widgets, …)
  public/frontend/          # built patient-portal assets
  www/                      # website routes: patient_portal(.html/.py), patient-portal/
  templates/, locale/main.pot, tests/utils.py
patient_portal/             # Vue 3 + frappe-ui SPA source (src/components/*.vue)
wiki/                       # design docs and usage docs
```

**How the parts call each other**
- DocType controllers subclass `frappe.model.document.Document` and import shared helpers from `healthcare.healthcare.utils` and from ERPNext (accounts, stock).
- ERPNext documents are extended through `doc_events` in `hooks.py` and through `custom_doctype/`, never by editing ERPNext.
- Desk JS calls server methods with `frappe.call` on `@frappe.whitelist()` functions (about 182 of them).
- The patient portal calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui `createResource`/`frappeRequest`. It is served by `www/patient_portal.html`, and realtime refetch arrives over socket.io.
- Background work goes through `frappe.enqueue` and the `scheduler_events` in `hooks.py` (appointment reminders, daily status updates, fee validity, inpatient billables, expiring medication requests).
- Import order is enforced as `frappe` → `erpnext` → `healthcare` sections.
