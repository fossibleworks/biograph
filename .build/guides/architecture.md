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
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Architecture

The repo is a single Frappe app (`healthcare`) plus a Vue SPA that builds into it.

```
healthcare/                 # Python package / Frappe app root
  hooks.py                  # wiring: doc_events, scheduler_events, doctype_js, jinja, on_login, fixtures
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: <name>.json, <name>.py controller, <name>.js form script, test_<name>.py
    api/patient_portal.py   # whitelisted endpoints consumed by the portal SPA
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    report/, page/, print_format/, dashboard_chart*/, number_card/, workspace/, web_form/
    utils.py, healthcare.py, auth.py
  controllers/              # shared controllers (e.g. service_request_controller, queries)
  regional/                 # country-specific code (e.g. ABDM / India)
  patches/ + patches.txt    # data migrations (v0_0, v15_0, v16_0; pre/post_model_sync)
  public/js/                # Desk bundle (healthcare.bundle.js) and shared JS controllers
  www/patient_portal.*      # server route that hosts the built SPA
  setup.py / install.py / uninstall.py / after_migrate.py  # install-time fixtures and custom fields
  tests/utils.py            # HealthcareTestSuite + bootstrap master data
  locale/main.pot           # translatable strings
patient_portal/             # Vue 3 SPA source; builds into healthcare/public/patient_portal/assets
wiki/                       # fork design docs and usage notes
```

## How the pieces call each other
- **Desk UI → server:** form scripts call `frappe.call` against `@frappe.whitelist()` methods in doctype controllers (there are about 180 whitelisted functions).
- **Portal SPA → server:** frappe-ui `createResource` calls `healthcare.healthcare.api.patient_portal.*` through the Frappe proxy.
- **ERPNext integration:** `hooks.py` `doc_events` reacts to ERPNext documents (Sales Invoice, etc.), and `doctype_js` injects scripts into ERPNext forms. Billing goes through ERPNext items, price lists, and invoices.
- **Cross-cutting hooks:** the wildcard `doc_events["*"]` creates and updates Patient Medical Records on submit, cancel, and update-after-submit. `scheduler_events` runs appointment reminders, status updates, fee validity, IP billables, and medication-request expiry.
- Schema lives in DocType JSON. Business logic and validation live in the Python controllers (`validate`, `on_submit`, etc.), not in client JS.
