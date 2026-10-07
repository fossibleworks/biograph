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
  - patient_portal/vite.config.js
  - healthcare/patches.txt
---

This is a single Frappe app (`healthcare`) plus one Vue SPA.

```
healthcare/                  # Frappe app package
  hooks.py                   # wiring: doc_events, scheduler_events, overrides, jinja, portal, permissions
  healthcare/                # the "Healthcare" module
    doctype/<snake_name>/    # one folder per DocType (~139): .json schema, .py controller, .js form script, test_*.py
    custom_doctype/          # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    api/patient_portal.py    # whitelisted API used by the SPA
    report/, page/, print_format/, web_form/, dashboard_chart*/, number_card/, workspace/
    utils.py                 # shared billing/service helpers
    setup/                   # install-time setup data
  controllers/               # cross-doctype controllers (service_request_controller, queries)
  regional/india/abdm        # region-specific (ABDM) integration
  patches/v0_0|v15_0|v16_0 + patches.txt   # data migrations
  public/js/                 # desk JS (bundle, ERPNext doctype extensions)
  public/frontend/           # built Patient Portal assets (committed)
  www/patient_portal.html|py # SPA host page
  locale/main.pot            # translation source
  tests/utils.py             # shared test bootstrap
patient_portal/              # Vue 3 + frappe-ui SPA source; builds into healthcare/public
public/js/                   # misc root JS
wiki/                        # fork design docs and sync ledgers
```

**How the parts talk to each other:**
- ERPNext integration goes through **hooks**, not ERPNext edits. `override_doctype_class` replaces Sales Invoice with `HealthcareSalesInvoice`. `doc_events` on Sales Invoice, Payment Entry, Company, and Patient call into `healthcare.healthcare.utils` / `custom_doctype`. A wildcard `"*"` on_submit/on_cancel hook maintains Patient Medical Records.
- Background work runs through `scheduler_events` (appointment reminders, daily status updates, IP billables, medication request expiry) and `frappe.enqueue`.
- The SPA calls whitelisted Python methods through frappe-ui `createResource`. `www/patient_portal.py` serves its HTML shell.
- Doctype controllers import each other's helpers directly, e.g. `patient_appointment` imports from `healthcare.healthcare.utils`.
