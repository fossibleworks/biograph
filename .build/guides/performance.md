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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

These paths are likely to be performance-sensitive, based on the code's shape:

- **The global `doc_events["*"]` hooks** (`on_submit`, `on_cancel`, `on_update_after_submit` → `patient_history_settings.create/delete/update_medical_record`) run on *every* submittable document in the site. Keep them cheap and return early when a doctype is not configured.
- **Sales Invoice / Payment Entry hooks** (`healthcare.healthcare.utils.manage_invoice_*`, `custom_doctype/payment_entry.py`) run inside ERPNext's accounting transactions.
- **Appointment slot and availability calculation** in `patient_appointment.py` (`get_availability_data`, overlap and capacity checks) is called interactively from the booking UI and the portal.
- **The scheduler** runs `send_appointment_reminder` on the `all` cadence (every few minutes), plus daily status sweeps over appointments, fee validity, inpatient billables and medication requests. These need set-based queries, not per-record loads.
- **Long work goes to background queues:** recurring appointment creation uses `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`, and sample collection also enqueues. Follow this pattern for bulk operations.
- About 170 call sites use `frappe.db.sql` or `frappe.qb`. Prefer `frappe.db.get_value` / `get_all` with explicit `fields`, and add `search_index` on fields you filter by often (upstream added it on `patient` and `procedure_template`).
