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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
---

# Performance-sensitive areas

- **Global `doc_events["*"]`.** `on_submit`/`on_cancel`/`on_update_after_submit` run `patient_history_settings` medical-record hooks on **every submitted document in the site**, including ERPNext ones. Keep them cheap and return early.
- **Sales Invoice hooks** (`manage_invoice_validate`/`submit_cancel`) run on every invoice.
- **The `"all"` scheduler** runs `send_appointment_reminder` every few minutes. The daily jobs scan appointments, fee validity, inpatient records and medication requests, so query them in bulk with filters and not row by row.
- **Appointment booking and availability** (`patient_appointment.py`, about 1900 lines; `practitioner_availability`). Slot, overlap and capacity checks run on every booking. Prefer `frappe.qb` aggregate queries (e.g. `Max(position_in_queue)`) over loops of `get_doc`.
- **Patient portal API** (`api/patient_portal.py`) is called on every portal page load, for appointments and patient relations.
- **Long-running work** goes to the background with `frappe.enqueue`, e.g. recurring appointment creation and sample collection.
- Patches should be idempotent and batch-friendly. They run during `bench migrate` on large production datasets.
