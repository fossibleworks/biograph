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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

Likely hot paths:

- **Appointment scheduling and slot computation:** `patient_appointment.py` (about 2,200 lines) handles overlap and capacity checks, practitioner availability and slot generation. The portal's `get_slots` and `make_appointment` are called on every date or practitioner change.
- **Scheduler jobs:** `send_appointment_reminder` runs on **`all`** (every few minutes). Daily jobs update appointment statuses, fee validity, inpatient occupancy billables and expired medication requests. These scan whole tables, so keep queries filtered and indexed.
- **`doc_events["*"]`:** `on_submit`/`on_cancel`/`on_update_after_submit` handlers create Patient Medical Records for **every submitted doctype on the site**, ERPNext ones included. Keep that handler cheap and return early.
- **Sales Invoice hooks:** `validate`/`on_submit`/`on_cancel` in `healthcare/healthcare/utils.py` run on every invoice.
- **Reports:** `report/` (diagnosis trends, appointment analytics, lab test report) aggregate large tables. Use `frappe.qb` with explicit filters and fields.
- **Long work** goes to `frappe.enqueue` (recurring appointment creation, sample collection). Progress is pushed with `frappe.publish_realtime`.
- No app-level caching is in use today.
