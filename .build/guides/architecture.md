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
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - pyproject.toml
---

This is a standard **Frappe app** layout. The Python package is `healthcare/`, and the module of the same name is `healthcare/healthcare/`.

```
healthcare/                 # app package (hooks, install, patches, permissions)
  hooks.py                  # wiring: doc_events, scheduler_events, doctype_js, fixtures, app screen
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py   # whitelisted API used by the Vue portal
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                # shared domain helpers (billing items, configuration checks)
    setup/                  # setup routines (e.g. patient duplicate check rules)
  controllers/              # shared controllers (service_request_controller, link queries)
  regional/india/           # region-specific (ABDM) customisations
  patches/ + patches.txt    # data migrations grouped v0_0 / v15_0 / v16_0, [pre_model_sync]/[post_model_sync]
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData master data
  public/js/                # desk JS bundled via healthcare.bundle.js
  public/frontend/          # built Patient Portal assets
  www/patient_portal.html   # Jinja entry page for the portal SPA
  locale/main.pot           # translation template
patient_portal/             # Vue 3 + frappe-ui source for the portal (Vite build)
wiki/                       # design docs, usage docs, sync ledgers
```

**How the parts call each other**
- Frappe loads `hooks.py`. `doc_events` (including a `"*"` hook that creates and deletes Patient Medical Records on submit and cancel) and `scheduler_events` (for example appointment reminders) point at functions in the doctype controllers by dotted path.
- Desk form scripts call server methods through `frappe.call` against `@frappe.whitelist()` functions in the doctype `.py` files (about 180 whitelisted functions).
- The portal SPA talks to the server only through frappe-ui's `frappe-request` resource fetcher, which calls `healthcare.healthcare.api.patient_portal.*`, plus socket.io realtime.
- Healthcare doctypes integrate with ERPNext accounting (Sales Invoice, POS Profile, Items) and import from `erpnext.*` directly.
- Import order is enforced by ruff isort sections: stdlib → third-party → `frappe` → `erpnext` → `healthcare`.
