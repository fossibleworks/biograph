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

The repository is **one Frappe app (`healthcare`)** plus **one Vue SPA (`patient_portal`)**.

```
healthcare/                  Frappe app package (python module "healthcare")
  hooks.py                   App wiring: doc_events, scheduler_events, overrides, jinja, portal menu
  healthcare/                The "Healthcare" module
    doctype/<snake_name>/    One folder per DocType: <name>.json (schema), <name>.py (controller),
                             <name>.js (form script), optional _list.js/_tree.js/_dashboard.py, test_<name>.py
    api/patient_portal.py    @frappe.whitelist() endpoints consumed by the Vue portal
    custom_doctype/          Extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    report/, page/, print_format/, web_form/, workspace/, dashboard_chart*/, number_card/
    utils.py                 Shared billing and invoice helpers called from hooks
    setup/                   Setup routines (e.g. patient_duplicate_check)
  controllers/               Cross-doctype controllers (service_request_controller.py, queries.py)
  regional/india/abdm/       Country-specific integration
  patches/ + patches.txt     Versioned data migrations (v0_0, v15_0, v16_0)
  public/js/                 Desk JS bundle (healthcare.bundle.js) and shared widgets
  public/frontend/           Built portal assets
  www/patient_portal.*       Portal entry HTML/py served at /patient-portal
  locale/main.pot            Translatable strings
  tests/utils.py             Shared test bootstrap (HealthcareTestSuite)
patient_portal/              Vue 3 + frappe-ui SPA; builds into healthcare/public and www/patient_portal.html
wiki/                        Fork design notes and upstream-sync ledger
```

**How the parts call each other**
- Frappe loads `hooks.py`. Document events on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient, and `*` for medical records) call into `healthcare.healthcare.utils`, `custom_doctype/*`, and doctype modules.
- `override_doctype_class` replaces ERPNext's Sales Invoice with `HealthcareSalesInvoice`.
- Scheduler jobs (appointment reminders, daily status updates) live as module-level functions inside doctype controllers.
- Doctype controllers import one another directly (e.g. `healthcare.healthcare.doctype.patient_appointment.patient_appointment`) and import ERPNext (`from erpnext...`).
- The Vue portal calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources and the Frappe RPC proxy.
- Desk form scripts call controller methods through `frappe.call` / `frm.call` on `@frappe.whitelist()` functions.

The fork tracks upstream `earthians/marley` `version-16`. Merges keep fork behaviour and add upstream fixes on top (see `wiki/upstream-sync-version-16.md`).
