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
---

Likely hot paths, inferred from the codebase's shape:

- **Wildcard `doc_events["*"]`:** on_submit/on_cancel/on_update_after_submit run `patient_history_settings` medical-record hooks for **every submitted document in the whole ERPNext site**. Keep them cheap and return early for irrelevant doctypes.
- **ERPNext invoice and payment hooks:** `manage_invoice_validate`, `manage_invoice_submit_cancel`, and the payment-entry handlers run inside accounting transactions. Avoid per-row queries.
- **Scheduler:**
  - `send_appointment_reminder` runs on `all` (every tick), so it must be indexed/filtered and idempotent
  - the daily jobs update appointment status, fee validity, inpatient billables, and expired medication requests over potentially large tables
- **Appointment scheduling:** `patient_appointment.py` (about 2,200 lines) computes availability slots, overlaps, capacity, and recurring and block bookings. This path is called interactively from desk and the patient portal.
- **Heavy work goes to background jobs via `frappe.enqueue`.** Recurring appointment creation and sample collection already do this.
- There are about 300 `frappe.db.sql`/`get_all`/`get_list` call sites. Prefer filtered `get_all` with explicit `fields`, `pluck`, and batching over looping `get_doc` calls.
- Reports (`report/` such as patient_appointment_analytics and diagnosis_trends) aggregate over large clinical datasets.
