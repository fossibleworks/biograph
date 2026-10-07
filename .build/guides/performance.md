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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
---

Paths likely to be performance-sensitive, judging by how the codebase is organised:

- **Appointment scheduling and slot computation.** This covers `patient_appointment.py` (about 2.2k lines), overlap and capacity checks, practitioner availability, block-based therapy booking, recurring appointments, and the portal `get_slots` / `make_appointment` endpoints. These run on every booking and calendar render (`patient_appointment_calendar.js`).
- **The global `doc_events["*"]` hooks** (`create_medical_record`, `update_medical_record`, `delete_medical_record`). They fire on submit, cancel and update-after-submit of **every** submittable document in the site, so keep them cheap and return early when a doctype is not configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) add work to core ERPNext accounting flows.
- **Scheduler jobs:**
  - `send_appointment_reminder` runs on the `all` (every-tick) schedule.
  - Daily jobs scan appointments, fee validity, inpatient records and medication requests. Batch these and filter in SQL.
- **Patient history and progress pages, and the reports** (`patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, …) aggregate large clinical datasets.
- **Patient duplicate checking** runs on Patient insert.

Current conventions: use `frappe.db.get_value`, `get_list(..., pluck=...)` and `frappe.qb` / `frappe.db.sql` with filters instead of loading full docs in loops. The patches note when a backfill is large (`populate_appointment_end_fields`).
