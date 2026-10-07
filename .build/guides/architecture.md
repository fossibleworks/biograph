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
  - healthcare/www/patient_portal.py
  - healthcare/patches.txt
  - patient_portal/vite.config.js
---

This is a single Frappe app that installs into a bench next to `frappe` and `erpnext`.

```
healthcare/                      # Python package = Frappe app root
  hooks.py                       # wiring: doc_events, scheduler_events, overrides, js includes, standard_queries
  modules.txt                    # single module: "Healthcare"
  patches.txt + patches/v0_0|v15_0|v16_0   # data migrations ([pre_model_sync]/[post_model_sync])
  install.py / setup.py / uninstall.py / after_migrate.py
  controllers/                   # shared controllers (queries.py, service_request_controller.py)
  healthcare/                    # the "Healthcare" module
    doctype/<snake_name>/        # one folder per DocType: .json schema, .py controller, .js form, test_*.py
    custom_doctype/              # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    api/patient_portal.py        # whitelisted API used by the portal
    report/, page/, print_format/, web_form/, workspace/, dashboard_chart*/, number_card/, onboarding*
    utils.py                     # cross-doctype helpers (invoicing hooks, service unit tree, etc.)
    setup/                       # install-time setup (e.g., patient duplicate check rules)
  regional/india/abdm/           # India ABDM integration
  public/js/                     # desk JS bundled via healthcare.bundle.js
  public/frontend/               # built patient-portal assets (committed)
  www/patient_portal.{py,html}   # portal route + boot
  locale/main.pot                # translations source
  tests/utils.py                 # HealthcareTestSuite + bootstrap test data
patient_portal/                  # Vue 3 + frappe-ui SPA source, built into healthcare/public & www
wiki/                            # design docs, usage docs, upstream sync ledger
```

**How the pieces connect**
- **Hooks are the integration seam with ERPNext.** `doc_events` attaches healthcare logic to ERPNext documents: Sales Invoice submit/cancel/validate, Payment Entry, Company, Patient. A wildcard `"*"` hook maintains Patient Medical Records on submit/cancel. `override_doctype_class` swaps in `HealthcareSalesInvoice`.
- **DocType controllers** (classes extending `Document`) hold the business logic. Cross-document actions are module-level `@frappe.whitelist()` functions in the same file, called from form JS with `frappe.call`. There are about 180 whitelisted endpoints.
- **Scheduler jobs** are module-level functions in DocType files: appointment reminders (all), plus daily status updates for appointments, fee validity, inpatient billables, and medication requests.
- **Patient Portal** talks to the backend only over Frappe REST/RPC, through frappe-ui resources and `healthcare/healthcare/api/patient_portal.py` / `healthcare/www/patient_portal.py`. Realtime updates go through `socket.js`.
- **Patches** keep data in step with schema changes. Add new ones to `patches.txt` under the right section and version folder.

Put new domain logic in the owning DocType's controller. Hook ERPNext doctypes through `hooks.py` / `custom_doctype/` rather than editing ERPNext.
