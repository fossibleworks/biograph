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
  - pyproject.toml
  - healthcare/patches.txt
---

The repo is a single **Frappe app** (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Frappe app package (installed via bench)
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, jinja, portal
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    api/patient_portal.py   # @frappe.whitelist() endpoints used by the Vue portal
    report/, page/, web_form/, workspace/, dashboard_chart*/, number_card/, print_format/
    utils.py                # shared server helpers (invoicing, service unit tree, barcodes)
  regional/india/abdm/      # regional integration (ABDM)
  controllers/              # shared controllers/queries
  patches/ + patches.txt    # data migrations, versioned v0_0 / v15_0 / v16_0
  public/js/                # desk JS (healthcare.bundle.js, shared utils/widgets)
  public/frontend/          # built Patient Portal assets (generated)
  www/                      # website routes (patient_portal.html/.py, patient-portal)
  tests/utils.py            # BootStrapTestData + HealthcareTestSuite
patient_portal/             # Vue 3 + frappe-ui SPA source, built by Vite into healthcare/
wiki/                       # design docs, usage docs, upstream-sync ledger
```

**How the pieces depend on each other**
- `healthcare` depends on **frappe** and **erpnext**. It extends ERPNext through `hooks.py`: `override_doctype_class` (HealthcareSalesInvoice), `doc_events` on Sales Invoice, Payment Entry, Company and `*` (medical record creation on submit), `doctype_js` for ERPNext forms, and `scheduler_events` (appointment reminders, daily status updates).
- DocType controllers call each other through module paths (`healthcare.healthcare.doctype.<x>.<x>`) and shared helpers in `healthcare.healthcare.utils`.
- The **Patient Portal** SPA calls whitelisted methods in `healthcare/healthcare/api/patient_portal.py` through the frappe-ui resources and proxy. Vite writes its build into the app, and `healthcare/www/patient_portal.html` serves it.
- Import order (ruff isort sections): stdlib, then third-party, then `frappe`, then `erpnext`, then `healthcare`.

Put new domain logic in the doctype controller that owns it. Wire cross-doctype or ERPNext reactions through `hooks.py` instead of changing ERPNext.
