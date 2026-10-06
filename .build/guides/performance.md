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

These paths are likely performance-sensitive, judging by the codebase's shape:

- **The wildcard `doc_events["*"]` hooks** (`on_submit`, `on_cancel`, `on_update_after_submit` → `patient_history_settings.create/delete/update_medical_record`) run on *every* submittable document in the site. Keep them cheap and return early.
- **Sales Invoice hooks** (`manage_invoice_validate` / `manage_invoice_submit_cancel` in `healthcare/healthcare/utils.py`) sit on ERPNext's billing hot path.
- **Patient Appointment** (`patient_appointment.py`, about 2000 lines) is the hottest flow. It handles availability, overlap and capacity checks, slot computation, unavailability calendar events, and the `send_appointment_reminder` job, which runs on the `all` scheduler tick.
- **Daily scheduler jobs** scan large tables: appointment status updates, fee validity, inpatient occupancy billables and medication request expiry.
- **Portal API** (`api/patient_portal.py`) uses multi-join `frappe.qb` queries per patient.
- **Long-running work** goes through `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`, e.g. recurring appointment creation and sample collection.

Guidance: prefer `frappe.qb` or `frappe.get_all` with explicit `fields`/`pluck` over loading full docs in loops. Move bulk work to `frappe.enqueue`. Avoid adding per-document work to wildcard hooks.
