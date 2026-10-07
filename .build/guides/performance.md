---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

These paths are likely to be performance-sensitive, based on the code's shape:

- **Appointment scheduling and slot availability** (`patient_appointment`, `practitioner_availability`, block booking, recurring appointments). These do overlap and capacity checks over appointments, schedules and holidays on every booking, and the Patient Portal calls them interactively.
- **Billing hooks** on Sales Invoice and Payment Entry (`custom_doctype/`, `doc_events`). They run inside ERPNext transactions, so slow code here slows down core accounting.
- **Reports** (`healthcare/healthcare/report/*`, for example `patient_appointment_analytics`, `diagnosis_trends`) and dashboard chart sources aggregate large tables.
- **Raw SQL:** about 91 `frappe.db.sql` calls versus about 80 `frappe.qb` uses. Prefer `frappe.qb` or `frappe.get_all` with explicit `fields` and filters, and avoid N+1 `frappe.get_doc` calls in loops.
- **Heavy or bulk work** belongs on the queue: `frappe.enqueue` (recurring appointment creation, sample collection) and `scheduler_events` in `hooks.py`.
- **Patches** run over whole tables during migrate, so batch them and avoid per-row `get_doc().save()` where a bulk update works.
