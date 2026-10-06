---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Likely hot or sensitive paths, inferred from the code:

- **Patient Appointment** (`patient_appointment.py`, about 2.2k lines): slot and availability calculation (`get_availability_data`), overlap and capacity checks, and recurring appointments. The scheduler runs `send_appointment_reminder` on **every tick (`all`)**, so keep it cheap.
- **The wildcard `doc_events["*"]`** (on_submit, on_cancel and on_update_after_submit run Patient Medical Record maintenance on *every* submitted document site-wide). Anything added there runs on all doctypes, so return early when the doctype is not configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) run inside ERPNext's billing transactions.
- **The portal API** (`api/patient_portal.py`) uses joined `frappe.qb` queries over appointments and encounters. Note that `get_appointments` calls `get_patients_with_relations()` twice.
- **Daily jobs:** appointment status updates, fee validity, inpatient billables and expiry of medication requests.

**Existing conventions to follow:**
- Use `frappe.get_cached_value` and `frappe.db.get_value` for single fields, not full `get_doc`.
- Use `frappe.qb` joins or `get_all(fields=...)` instead of N+1 loops, with `pluck` where possible.
- Mark frequently filtered Link fields with `search_index` in the doctype JSON (about 35 doctypes do).
- Run long or bulk work through `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`, as recurring appointments and sample collection do.
