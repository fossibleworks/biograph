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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Biograph is a single Frappe app, `healthcare`, installed into a bench next to `frappe` and `erpnext`.

```
healthcare/                     # Frappe app package
  hooks.py                      # wiring: doc_events, scheduler_events, doctype_js, bundles, portal routes
  healthcare/                   # the "Healthcare" module
    doctype/<snake_name>/       # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py       # @frappe.whitelist endpoints used by the Vue portal
    custom_doctype/             # overrides/extensions of ERPNext docs (sales_invoice, payment_entry)
    report/ page/ dashboard_chart*/ number_card/ workspace/ print_format/ web_form/
    utils.py, healthcare.py
  controllers/                  # shared controllers (queries.py, service_request_controller.py)
  regional/india/               # country-specific logic (ABDM)
  patches/v0_0|v15_0|v16_0/     # data migrations, registered in patches.txt
  public/js/                    # desk JS, bundled through healthcare.bundle.js
  public/patient_portal/assets  # built portal output (vite outDir)
  www/patient_portal.{html,py}  # portal entry page (Jinja boot data)
  tests/utils.py                # BootStrapTestData + HealthcareTestSuite
  locale/main.pot               # translatable strings
patient_portal/                 # Vue 3 + frappe-ui SPA source, builds into healthcare/public + www
wiki/                           # fork design docs, usage docs and sync ledgers
```

**How the pieces call each other**
- DocType controllers subclass `frappe.model.document.Document` and import across doctypes by full dotted path, for example `from healthcare.healthcare.doctype.fee_validity.fee_validity import check_fee_validity`. They also import ERPNext code directly (`erpnext.setup...`).
- `hooks.py` connects these to the framework:
  - `doc_events` on `"*"` (on_submit/on_cancel) feed patient history and medical records.
  - `scheduler_events` runs, for example, appointment reminders.
  - `doctype_js` extends ERPNext forms (Sales Invoice, Healthcare Practitioner).
- The Vue portal calls whitelisted methods in `healthcare.healthcare.api.patient_portal` through frappe-ui's proxy. Vite builds into `healthcare/public/patient_portal/assets` and writes `healthcare/www/patient_portal.html`.
- Heavy work goes to background jobs with `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`.

Keep business logic and validations on the server side. The PR template requires this.
