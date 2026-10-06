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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

# Performance-sensitive paths

- **`doc_events` on `"*"`**: `on_submit`, `on_cancel` and `on_update_after_submit` call `patient_history_settings.create/delete/update_medical_record` for **every submitted document in the whole ERPNext site**. Keep these handlers cheap and return early for doctypes that are not tracked.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_submit_cancel`, `manage_invoice_validate`, `set_paid_amount_in_healthcare_docs`) run inside ERPNext billing transactions. Avoid N+1 queries over invoice items.
- **Scheduler**: `send_appointment_reminder` runs on `all`, about every few minutes. Daily jobs scan appointments, fee validity, inpatient records and medication requests. Use filtered `frappe.db.get_all` or `frappe.qb` queries, not per-document loads.
- **Appointment slot and availability calculation** in `patient_appointment.py`, the block booking and recurring appointment handler, and practitioner schedules are hot interactive paths. Push filtering into the database.
- **Patient Portal API** (`api/patient_portal.py`) uses joined `frappe.qb` queries. Keep it that way rather than looping `get_doc`.
- **Reports** (for example `patient_appointment_analytics`, `diagnosis_trends`, `medication_item_wise_sales`) aggregate large tables. Use SQL or qb aggregation.
- Push heavy or bulk work to background jobs with `frappe.enqueue`, as `recuring_appointment_handler.py` and sample collection already do.
