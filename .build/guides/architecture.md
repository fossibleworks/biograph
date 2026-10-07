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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/controllers/service_request_controller.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

This is a standard **Frappe app layout**. The Python package `healthcare/` is the app, and inside it `healthcare/healthcare/` is the main module.

```
healthcare/
  hooks.py            # app wiring: doc_events, scheduler_events, overrides, jinja, portal, permissions
  healthcare/         # main module
    doctype/<name>/   # one folder per DocType: <name>.json, <name>.py, <name>.js, test_<name>.py, *_list.js
    custom_doctype/   # overrides/extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py  # whitelisted API for the Vue portal
    report/, page/, dashboard_chart*/, number_card/, workspace/, web_form/, print_format/, setup/
    utils.py          # cross-doctype billing/invoice helpers (manage_invoice_submit_cancel, etc.)
  controllers/        # shared controllers (service_request_controller.py, queries.py)
  regional/india/abdm # region-specific integration (ABDM)
  patches/ + patches.txt   # data migrations (v0_0, v15_0, v16_0)
  public/js           # desk-side shared JS bundled into healthcare.bundle.js
  www/                # portal pages (patient_portal.html/.py)
  locale/main.pot     # translation template
  tests/utils.py      # HealthcareTestSuite + BootStrapTestData fixtures
patient_portal/       # Vue 3 + frappe-ui SPA, built into healthcare/public + www/patient_portal.html
wiki/                 # fork design/usage docs and upstream-sync ledger
```

**How the parts call each other**
- ERPNext calls into the app through `hooks.py`. `doc_events` hook Sales Invoice, Payment Entry, Company and Patient. `"*"` events (`on_submit`, `on_cancel`, `on_update_after_submit`) feed Patient Medical Record through `patient_history_settings`. `override_doctype_class` replaces Sales Invoice with `HealthcareSalesInvoice`.
- Scheduled jobs live in `scheduler_events`: appointment reminders run on `all`; appointment status, fee validity, IP billables and expired medication requests run `daily`.
- Doctype controllers import each other through absolute dotted paths (`from healthcare.healthcare.doctype.x.x import ...`). They import ERPNext directly (`from erpnext.accounts...`).
- The Vue portal calls `@frappe.whitelist()` methods (mainly `healthcare.healthcare.api.patient_portal`) through frappe-ui `createResource`. In dev it uses the frappe proxy.
- Desk JS calls server methods with `frappe.call` / `frm.call` on whitelisted controller methods.

Add new domain behaviour as a DocType (controller class plus whitelisted functions) and register any cross-app hooks in `hooks.py`. Do not monkey-patch.
