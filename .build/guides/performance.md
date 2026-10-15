---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

These paths are likely to be performance-sensitive, based on the code's structure:

- **Wildcard `doc_events["*"]`** (`on_submit`, `on_cancel`, `on_update_after_submit` → Patient Medical Record). This runs on every submit of **every** doctype on the site. It must return cheaply for irrelevant doctypes.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, payment-entry handlers). These run on all ERPNext billing traffic, not only healthcare documents.
- **The `scheduler_events["all"]` job `send_appointment_reminder`** runs every few minutes. Keep it query-bounded. Daily jobs scan appointments, fee validity, inpatient records, and medication requests.
- **Appointment slot and availability calculation** in `patient_appointment.py` (about 1,900 lines: overlap and capacity checks, practitioner schedules, block booking). It is called interactively from Desk and from the portal booking flow.
- **Portal APIs** (`api/patient_portal.py`) use multi-join `frappe.qb` queries over appointments, encounters, and practitioners. Avoid N+1 lookups. `get_patients_with_relations()` is called more than once in `get_appointments`.
- **Long work is offloaded with `frappe.enqueue`**. Recurring appointment creation and sample collection already do this. Follow that pattern for bulk operations.
- **Script reports and dashboard charts/number cards** (`report/`, `dashboard_chart_source/`) aggregate over large clinical tables. Push filtering into SQL or qb.
- The portal bundle targets es2015 with sourcemaps. Keep frappe-ui imports tree-shakeable.
