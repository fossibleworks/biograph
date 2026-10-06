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
  - patient_portal/vite.config.js
  - pyproject.toml
---

Biograph is one Frappe app (`healthcare`) that ships with a separate Vue SPA.

```
healthcare/                 # Frappe app package
  hooks.py                  # wiring: doc_events, override_doctype_class, scheduler_events, doctype_js, jinja, install hooks
  healthcare/               # the 'Healthcare' module (modules.txt)
    doctype/<name>/         # DocType JSON + controller .py + form .js + test_<name>.py
    api/patient_portal.py   # whitelisted endpoints used by the Vue portal
    custom_doctype/         # overrides/extensions of ERPNext doctypes (Sales Invoice, Payment Entry)
    report/, page/, dashboard_chart_source/, number_card/, workspace/, print_format/, web_form/
    setup/                  # install-time setup (e.g. patient duplicate check rules)
    utils.py                # shared billing/helper logic
  controllers/              # shared controllers (service_request_controller, queries)
  regional/india/           # region-specific logic (ABDM)
  patches/ + patches.txt    # data migrations, run by `bench migrate`
  public/js/                # desk JS bundle (healthcare.bundle.js)
  public/frontend/          # built patient portal assets (committed)
  www/patient_portal.*      # portal host page/route
  tests/utils.py            # HealthcareTestSuite + BootStrapTestData
patient_portal/             # Vue 3 + frappe-ui SPA source, built by Vite into healthcare/public
wiki/                       # design docs, usage docs, and the upstream sync ledger
```

**How the parts call each other**

- Doctype controllers import ERPNext code directly (e.g. `erpnext.setup.doctype.employee.employee`) and each other through full dotted paths (`healthcare.healthcare.doctype.<x>.<x>`).
- Integration with ERPNext documents goes through the `doc_events` and `override_doctype_class` entries in `hooks.py`, not through edits to ERPNext.
- The Vue portal calls `@frappe.whitelist()` methods in `healthcare/healthcare/api/patient_portal.py` via frappe-ui resources.
- Background work runs from `scheduler_events` (appointment reminders and daily status updates) and from `frappe.enqueue`.
- Ruff's isort section order enforces this layering: stdlib → third-party → frappe → erpnext → healthcare.
