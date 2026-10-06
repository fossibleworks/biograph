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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

Paths that are likely performance-sensitive, judging from the code:

- **Wildcard `doc_events` `"*"` on_submit/on_cancel** (`patient_history_settings.create_medical_record` / `delete_medical_record`) runs on *every* submitted document in the site, including ERPNext ones. Keep it cheap and return early.
- **Scheduler `all` event** `send_appointment_reminder` runs every few minutes. Keep its queries bounded and indexed.
- **Patient Appointment scheduling** (`patient_appointment.py`, about 1,800 lines) works out availability, overlaps, capacity, and time blocks, often inside loops over practitioner schedules. Avoid per-slot DB queries. Use `frappe.get_all` with filters or `frappe.qb`.
- **Recurring appointments and sample collection** already push bulk work to the background with `frappe.enqueue`. Do the same for any new bulk operation.
- **Reports** (`report/*`, e.g. patient_appointment_analytics, diagnosis_trends) aggregate over large tables. Prefer `frappe.qb` or SQL aggregation over Python loops.
- **Patient history and progress pages** and dashboard charts load timelines per patient.
- **The patient portal** uses frappe-ui `getCachedResource` / `getCachedListResource` to avoid refetching data.
- There are about 171 `frappe.qb` / `frappe.db.sql` call sites. Watch for N+1 `get_doc` inside loops.
