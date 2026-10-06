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
---

The repo is a single Frappe app (`healthcare`) plus a separate Vue SPA.

```
healthcare/                 # Python package = Frappe app
  hooks.py                  # wiring: doc_events, scheduler_events, override_doctype_class, jinja, portal menus, permissions
  install.py / setup.py / uninstall.py / after_migrate.py   # lifecycle hooks
  patches/ + patches.txt    # data migrations (v0_0, v15_0, v16_0)
  controllers/              # shared controllers (service_request_controller, queries)
  healthcare/               # the 'Healthcare' module
    doctype/<name>/         # <name>.json (schema), <name>.py (controller), <name>.js (form script), test_<name>.py
    custom_doctype/         # extensions of ERPNext doctypes (HealthcareSalesInvoice, payment_entry)
    api/patient_portal.py   # whitelisted endpoints consumed by the SPA
    report/, page/, dashboard_chart*/, number_card/, workspace/, web_form/, print_format/
    utils.py, setup/        # shared helpers and setup routines
  regional/india/abdm/      # regional integration
  public/js/                # desk JS, healthcare.bundle.js
  public/frontend/          # built Patient Portal assets (committed)
  www/patient_portal.html|.py  # portal entry page (Jinja boot data)
  locale/main.pot           # translation template
  tests/utils.py            # HealthcareTestSuite and bootstrap test data
patient_portal/             # Vue 3 + frappe-ui SPA source (src/components, src/utils)
wiki/                       # fork design and usage docs, upstream-sync ledger
```

**How the pieces connect**
- `hooks.py` is the integration point. Cross-cutting behaviour goes there rather than into monkey-patches: `doc_events` on ERPNext doctypes (Sales Invoice, Payment Entry, Company, Patient), the `"*"` events that build Patient Medical Records, `scheduler_events` (appointment reminders, daily status updates), and `override_doctype_class` for Sales Invoice.
- Doctype controllers call each other through direct Python imports (`from healthcare.healthcare.doctype.X.X import ...`). They depend on `frappe` and `erpnext`.
- The SPA calls `@frappe.whitelist()` methods in `healthcare/healthcare/api/patient_portal.py` (and doctype modules) through the frappe-ui resource proxy. It also opens a realtime socket (`src/socket.js`).
- Imports are grouped per ruff isort sections in this order: stdlib → third-party → `frappe` → `erpnext` → `healthcare`.
