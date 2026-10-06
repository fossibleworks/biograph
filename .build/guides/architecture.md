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
  - healthcare/controllers/queries.py
  - patient_portal/vite.config.js
  - pyproject.toml
  - healthcare/patches.txt
---

The repo is one Frappe app, `healthcare`, plus a separate Vue SPA.

```
healthcare/                 # Frappe app package (python module `healthcare`)
  hooks.py                  # app wiring: doc_events, scheduler_events, doctype_js, fixtures, etc.
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # ~139 DocTypes: <name>.json (schema), <name>.py (controller), <name>.js (form script), test_<name>.py
    report/                 # script/query reports (diagnosis_trends, lab_test_report, patient_appointment_analytics, …)
    page/                   # desk pages (patient_history, patient_progress)
    custom_doctype/         # overrides/extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py   # whitelisted API used by the portal
    dashboard_chart*/, number_card/, workspace/, print_format/, web_form/, setup/, utils.py
  controllers/              # shared controller logic (queries.py, service_request_controller.py)
  regional/india/           # ABDM / India-specific code
  patches/vXX_0/ + patches.txt   # data migrations (pre_model_sync / post_model_sync)
  public/js/                # desk JS bundled via healthcare.bundle.js; public/frontend = built portal assets
  www/patient_portal.{html,py}  # portal entry page served by Frappe
  tests/utils.py            # shared test bootstrap (HealthcareTestSuite)
  locale/main.pot           # translation template
patient_portal/             # Vue 3 + frappe-ui SPA, builds into healthcare/public & www
wiki/                       # fork design/usage docs & upstream sync ledger
```

**How the parts call each other**
- ERPNext is a hard dependency. Healthcare imports ERPNext modules directly (`from erpnext...`) and extends ERPNext doctypes through `doctype_js` and `doc_events` in `hooks.py`, and through `custom_doctype/`.
- DocType controllers call shared helpers in `healthcare/healthcare/utils.py` and `healthcare/controllers/`. Cross-doctype functions are imported by full dotted path (`healthcare.healthcare.doctype.<x>.<x>`).
- The desk JS and the portal call server methods marked `@frappe.whitelist()` (182 of them) through `frappe.call`/`frappe-ui` resources. The portal mainly uses `healthcare.healthcare.api.patient_portal`.
- Background work is wired in `hooks.py` `scheduler_events`: appointment reminders (`all`), and daily jobs for appointment status, fee validity, inpatient billables and expired medication requests.
- Isort section order (`frappe` → `erpnext` → `healthcare`) puts the dependency direction into code: healthcare depends on erpnext, which depends on frappe.
