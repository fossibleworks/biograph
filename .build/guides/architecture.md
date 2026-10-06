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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Biograph is one Frappe app (`healthcare/`) plus a Vue SPA (`patient_portal/`).

```
healthcare/                 # Python package installed into a Frappe bench
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, doctype_js, standard_queries, fixtures
  install.py / uninstall.py / after_migrate.py / setup.py
  patches.txt + patches/    # data migrations ([pre_model_sync]/[post_model_sync]; patches/v0_0, v15_0, v16_0)
  controllers/              # shared controllers (queries.py, service_request_controller.py)
  regional/india/           # ABDM integration
  www/                      # website routes (patient_portal.html/.py, patient-portal/)
  public/js/                # Desk JS bundled via healthcare.bundle.js; frontend/ holds built portal assets
  tests/utils.py            # BootStrapTestData + HealthcareTestSuite
  healthcare/               # the 'Healthcare' module
    doctype/<snake_name>/   # <name>.json + <name>.py + <name>.js + test_<name>.py (+ _list.js, _dashboard.py, _calendar.js)
    custom_doctype/         # overrides of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py   # whitelisted endpoints used by the SPA
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/, setup/, utils.py
patient_portal/             # Vue 3 + frappe-ui SPA (src/components/*.vue, socket.js, utils/formatters.js)
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the parts call each other**
- The Frappe framework loads `hooks.py`. Generic `doc_events` (`"*"` on_submit/on_cancel) create medical records. Scheduler jobs such as appointment reminders run here. `override_doctype_class` swaps ERPNext's Sales Invoice for `HealthcareSalesInvoice`.
- Doctype controllers call each other directly with Python imports, for example `from healthcare.healthcare.doctype.patient_appointment.patient_appointment import ...`. They depend on `erpnext.*` for accounting and stock.
- Desk JS calls Python through `frappe.call` / `frm.call` on `@frappe.whitelist()` methods.
- The Patient Portal SPA calls `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources. It is served from `healthcare/www/patient_portal.html`, and its build output is written into `healthcare/public/`.
- Long-running work goes through `frappe.enqueue` (for example recurring appointments and sample collection).
