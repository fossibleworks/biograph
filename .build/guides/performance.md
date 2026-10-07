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
  - healthcare/healthcare/utils.py
  - healthcare/controllers/queries.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

# Performance-sensitive areas

- **Patient Appointment** (`patient_appointment.py`, about 2.2k lines) is the hottest path. Slot availability, overlap and capacity checks, practitioner unavailability, fee validity, and billing all run in `validate`. The portal booking flow calls slot lookups many times. Avoid adding a query per slot or per row there.
- **Scheduler jobs** in `hooks.py`:
  - `send_appointment_reminder` runs on `all`, so roughly every few minutes. It iterates appointments and calls `frappe.get_doc` for each one. Keep it O(appointments due), and don't add per-row heavy work.
  - Daily jobs: `update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables`, `update_expired_medication_requests`. These scan whole tables, so filter them in SQL.
- **`healthcare/healthcare/utils.py`** (about 1.9k lines) builds billable items for invoicing (`get_appointments_to_invoice` and similar) across many doctypes. Sales Invoice forms call it often.
- **Link-field search queries** (`controllers/queries.py`, `standard_queries`) run on every keystroke. Use `frappe.qb` with indexed filters and respect `page_len`.
- **Reports** in `healthcare/healthcare/report/` (patient appointment analytics, diagnosis trends, lab test report) aggregate large tables.
- Long-running work is already moved off the request with `frappe.enqueue` (recurring appointments, sample collection) and pushed back with `frappe.publish_realtime`. Follow that pattern for bulk operations.
- Querying: about 80 `frappe.qb` uses and 91 raw `frappe.db.sql`. Prefer `frappe.qb` and `get_all` with `fields`/`pluck` over N+1 `get_doc` loops.
- Portal: use frappe-ui `getCachedListResource`/`getCachedResource` for cached data.
