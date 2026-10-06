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
  - healthcare/modules.txt
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This is a single Frappe app (`healthcare/`) plus a Vue SPA source tree (`patient_portal/`).

```
healthcare/                 # Frappe app package (python module "healthcare")
  hooks.py                  # wiring: doc_events, doctype_js, scheduler_events, jinja, on_login, overrides
  healthcare/               # the "Healthcare" module (modules.txt)
    doctype/<name>/         # one folder per DocType: <name>.json (schema), <name>.py (controller), <name>.js (form script), test_<name>.py
    api/patient_portal.py   # whitelisted endpoints consumed by the Vue portal
    custom_doctype/         # extensions of ERPNext doctypes (sales_invoice, payment_entry)
    report/, page/, dashboard_chart*/, number_card/, workspace/, print_format/, web_form/
    utils.py                # large shared helper module (billing, barcodes, codes)
    auth.py                 # role-based home-page redirect on login
  controllers/              # shared base controllers (service_request_controller.py, queries.py)
  regional/india/abdm/      # ABDM (India health stack) integration
  patches/v0_0|v15_0|v16_0  # data migrations, registered in patches.txt (pre/post_model_sync)
  setup.py, install.py      # install-time fixtures/custom fields
  public/js/                # desk JS bundles shared across doctypes
  public/frontend/          # committed build of the portal
  www/                      # web routes (patient_portal.html/.py)
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
  locale/main.pot           # translations source
patient_portal/src/         # Vue 3 SPA (PatientPortal.vue, components/, utils/)
```

**How the parts call each other**
- Business logic lives in DocType controllers (`validate`, `on_submit`, `on_update` and similar) and in module-level `@frappe.whitelist()` functions, about 182 of them. Form JS calls these through `frappe.call` and `frm.call`.
- ERPNext integration goes through `hooks.py` `doc_events` and overrides, and through `custom_doctype/` (Sales Invoice, Payment Entry). Tests reuse ERPNext fixtures such as `make_pos_profile`.
- The portal SPA talks to `healthcare.healthcare.api.patient_portal.*` through frappe-ui resources. Vite proxies to Frappe in dev (`frappeProxy: true`), and the build output is served from `/assets/healthcare/...`.
- Background work uses `frappe.enqueue` and `scheduler_events` (appointment reminders, daily status updates). Realtime updates use `frappe.publish_realtime`.
- The PR template states that all business logic and validation must be on the server side.
