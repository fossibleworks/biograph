---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

Paths likely to be performance-sensitive:

- **Wildcard doc_events:** `"*"` on_submit, on_cancel and on_update_after_submit hooks run Patient History Settings logic on *every* submitted document in the site. Keep these handlers cheap and exit early for irrelevant doctypes.
- **Sales Invoice hooks:** `manage_invoice_validate` and `manage_invoice_submit_cancel` in `healthcare/healthcare/utils.py` run on every invoice and walk the healthcare references. Avoid per-row `frappe.get_doc` and batch the `frappe.db` reads.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every few minutes). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests, scanning tables that grow over time. Filter the queries and keep them indexed.
- **Appointment availability and booking** (`patient_appointment.py`, about 1.8k lines): slot, overlap and capacity checks are hot interactive paths in the desk and portal.
- **Reports and dashboards:** `report/*` (patient_appointment_analytics, diagnosis_trends, lab_test_report, …) and dashboard chart sources aggregate large datasets. Prefer `frappe.qb` / SQL aggregates over Python loops.
- Raw `frappe.db.sql` appears in about 86 places in the module. Parameterize it and avoid N+1 patterns.
- The patient portal bundle is built with sourcemaps and an `es2015` target. Keep frappe-ui imports tree-shakeable.
