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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

# Performance-sensitive paths

- **`doc_events["*"]`** hooks on submit, cancel and update-after-submit (patient medical record creation) run for **every submitted document in the whole ERPNext site**. Keep them cheap and return early for irrelevant doctypes.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_payment_entry_submit_cancel`, …) are on core accounting paths.
- **The scheduler's `all` event** runs `send_appointment_reminder` every few minutes. The daily jobs scan appointments, fee validity, inpatient occupancy and medication requests. Use bulk queries and avoid per-row `get_doc` where possible.
- **Patient Appointment** availability and slot calculation, plus calendar views. `patient_appointment.py` is about 1,900 lines.
- **Portal APIs** (`api/patient_portal.py`) use `frappe.qb` joins and `frappe.get_cached_value`. Follow that pattern: one query with joins rather than N+1 lookups, and avoid calling the same helper twice in a query.
- Reports under `healthcare/healthcare/report/` and dashboard chart sources aggregate large tables, so filter in SQL.
