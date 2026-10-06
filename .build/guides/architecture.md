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
  - healthcare/controllers/service_request_controller.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Frappe app package (module: Healthcare)
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, doctype_js, standard_queries, fixtures
  healthcare/               # the 'Healthcare' module
    doctype/<name>/         # 139 DocTypes: <name>.json (schema), <name>.py (controller), <name>.js (form), test_<name>.py
    custom_doctype/         # overrides/extensions of ERPNext doctypes (sales_invoice.py, payment_entry.py)
    api/patient_portal.py   # @frappe.whitelist() endpoints for the portal SPA
    page/                   # desk pages (patient_history, patient_progress)
    report/, dashboard_chart_source/, number_card/, workspace/, print_format/, web_form/
    utils.py, setup/        # shared helpers; install-time setup (e.g. patient_duplicate_check.py)
  controllers/              # cross-doctype controllers (service_request_controller.py, queries.py)
  regional/india/           # ABDM integration, hooked via doc_events
  patches/ + patches.txt    # data migrations by version (v0_0, v15_0, v16_0), pre/post model sync
  public/js/                # desk JS bundled via healthcare.bundle.js
  www/patient_portal.{html,py}  # portal entry page that serves the Vue build
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
  locale/main.pot           # translatable strings
patient_portal/             # Vue 3 + frappe-ui SPA (Vite) -> builds into healthcare/public/...
wiki/                       # fork design docs, usage docs, upstream-sync ledger
```

**How the parts call each other**
- The DocType controllers (`Document` subclasses) hold the business logic. They call ERPNext through imports (for example `erpnext.*`) and through `frappe.get_doc`/`frappe.db`/`frappe.qb`.
- ERPNext doctypes are extended through `hooks.py` (`override_doctype_class`, `doc_events`, `doctype_js`). The original files are never edited.
- The portal SPA calls whitelisted Python methods (`healthcare.healthcare.api.patient_portal.*`) with frappe-ui `createResource`.
- Background work runs through `scheduler_events` (appointment reminders, daily status updates, fee validity, inpatient billables) and through `frappe.enqueue`.
- Schema changes live in the doctype JSON. Data migrations are patch modules registered in `patches.txt`.
