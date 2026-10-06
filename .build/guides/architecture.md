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
  - healthcare/healthcare/custom_doctype/sales_invoice.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
  - patient_portal/src/socket.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA source folder.

```
healthcare/                 # Frappe app package (python module "healthcare")
  hooks.py                  # wiring: doc_events, scheduler_events, doctype_js, fixtures, portal routes
  patches.txt + patches/    # data migrations (v0_0, v15_0, v16_0)
  setup.py / install.py / uninstall.py / after_migrate.py  # install-time setup (custom fields, roles, defaults)
  controllers/              # shared controllers (service_request_controller.py, queries.py)
  regional/india/abdm/      # regional ABDM integration
  healthcare/               # the "Healthcare" module
    doctype/<snake_name>/   # one folder per DocType: .json schema, .py controller, .js form script, test_*.py
    api/patient_portal.py   # whitelisted endpoints used by the Vue portal
    custom_doctype/         # overrides/extensions of ERPNext doctypes (sales_invoice, payment_entry)
    page/ report/ print_format/ web_form/ dashboard_chart*/ number_card/ workspace/
    utils.py, setup/        # shared helpers
  public/js/                # Desk JS bundle (healthcare.bundle.js) and shared form helpers
  public/frontend/          # built portal assets (committed)
  www/                      # website routes (patient-portal, patient_portal.html)
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData fixtures
  locale/main.pot           # translatable strings
patient_portal/             # Vue 3 + frappe-ui SPA source; builds into healthcare/public/...
wiki/                       # design docs, usage guides, upstream sync ledger
.github/                    # CI workflows, helper scripts, templates
```

**How the parts call each other**
- **DocType controllers** (`Document` subclasses in `doctype/*/*.py`) hold the business logic in `validate`, `on_submit` and `on_cancel`. Client scripts call the server through `frappe.call` / `frm.call` to `@frappe.whitelist()` functions.
- **`hooks.py`** links the app to Frappe and ERPNext:
  - wildcard `doc_events` create and delete Patient Medical Records on submit and cancel
  - Sales Invoice and Payment Entry hooks handle healthcare billing and insurance claims
  - `scheduler_events` run appointment reminders (`all`) plus daily status, fee-validity, inpatient-billable and medication-expiry jobs
- **ERPNext dependency:** the app imports `erpnext.*` directly (stock, accounts, POS profile, holidays) and extends Sales Invoice and Payment Entry.
- **Patient portal:** the Vue SPA calls `healthcare.healthcare.api.patient_portal.*` whitelisted methods through frappe-ui resources and subscribes to realtime events over socket.io. Its build output is served from `/assets/healthcare/...`.
- **Schema changes** are made through DocType JSON. Data backfills go in a patch module registered in `patches.txt` under `[pre_model_sync]` or `[post_model_sync]`.
