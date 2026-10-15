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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
---

## Hot paths, inferred from the code

- **The wildcard `doc_events["*"]`** (`on_submit`, `on_cancel`, `on_update_after_submit` → Patient History Settings medical record) runs on *every* submittable document in the site, ERPNext ones included. Keep it cheap and return early for doctypes it does not track.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`, insurance claim validation) add work to every billing transaction.
- **Patient Appointment** (`patient_appointment.py`, about 2,200 lines) covers slot availability, capacity and overlap checks, calendar events and recurring appointments. Booking and slot lookups are user-facing and latency-sensitive.
- **The scheduler** runs `send_appointment_reminder` on `all` (every few minutes). Daily jobs update appointment status, fee validity, inpatient occupancy billables and expired medication requests. These scan large tables, so use filtered `frappe.qb` or `get_all` queries with explicit fields.
- **Patient portal APIs** (`api/patient_portal.py`) run under patient sessions with multi-table joins.
- Reports: Patient Appointment Analytics, Diagnosis Trends, Lab Test Report, Medication Item-wise Sales.

## Existing techniques to reuse

- `frappe.get_cached_value` and `frappe.db.get_single_value` for settings and master lookups.
- `frappe.enqueue` for heavy or bulk work (sample collection, recurring appointment creation), with `frappe.publish_realtime` to report progress.
- `frappe.qb` joins with explicit `.select(...)` instead of per-row `get_doc` in loops.

Avoid N+1 `frappe.get_doc` calls inside loops in hooks and scheduler code, and do not call a helper twice in one query (`get_appointments` currently calls `get_patients_with_relations()` twice).
