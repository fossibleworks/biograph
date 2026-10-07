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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

The repository is one Frappe app (`healthcare`) plus a separately built Vue SPA.

```
healthcare/                 # Frappe app package
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, app_include_js
  healthcare/               # the 'Healthcare' module
    doctype/<snake_name>/   # DocType JSON + controller .py + form .js + test_<name>.py
    custom_doctype/         # overrides of ERPNext doctypes (HealthcareSalesInvoice, payment_entry hooks)
    api/patient_portal.py   # whitelisted endpoints used by the portal SPA
    report/, page/, dashboard_chart*/, number_card/, workspace/, web_form/, print_format/
    utils.py                # shared billing/invoice helpers (large, central)
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/abdm/      # India ABDM integration
  patches/v15_0, v16_0 + patches.txt   # data migrations
  public/js/                # desk JS bundled via healthcare.bundle.js
  public/frontend/          # built patient-portal assets (committed)
  www/patient_portal.{html,py}  # route serving the SPA
  tests/utils.py            # shared test bootstrap data + HealthcareTestSuite
  locale/main.pot
patient_portal/             # Vue 3 + frappe-ui SPA source (Vite)
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the parts call each other**
- ERPNext → healthcare: `doc_events` in `hooks.py` hang healthcare logic on ERPNext documents (Sales Invoice submit/cancel/validate → `healthcare.healthcare.utils`, Payment Entry → `custom_doctype.payment_entry`, Company → service unit tree root). The wildcard `"*"` hooks maintain medical records through `patient_history_settings`. `Sales Invoice` is replaced by `HealthcareSalesInvoice` via `override_doctype_class`.
- Doctype controllers import each other directly by full dotted path, for example `from healthcare.healthcare.doctype.patient_insurance_coverage.patient_insurance_coverage import make_insurance_coverage`.
- Background work runs through `scheduler_events` (appointment reminders, daily status updates, IP billables, medication-request expiry) and `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`.
- The Portal SPA calls `@frappe.whitelist()` methods in `healthcare/healthcare/api/patient_portal.py` through frappe-ui's proxy/resources. It is rendered from `healthcare/www/patient_portal.html` with Jinja boot data.
- Upstream relationship: the fork tracks `earthians/marley` and resolves conflicts with "fork intent wins". When a doctype JSON conflicts, take the union of `fields`/`field_order`; take the union of `patches.txt`.
