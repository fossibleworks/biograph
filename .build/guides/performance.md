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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.json
  - healthcare/healthcare/api/patient_portal.py
---

Paths that are likely to be performance-sensitive, inferred from the shape of the code:

- **Appointment scheduling:** `patient_appointment.py` (about 2,200 lines) handles availability and slot computation, overlap and capacity checks, and practitioner unavailability. Slot lookups run on every booking in both Desk and the portal (`BookAppointmentModel.vue`). Avoid per-slot queries and batch-fetch schedules instead.
- **Scheduler jobs:** `send_appointment_reminder` runs on `all` (every few minutes). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. These scan large tables, so keep them filtered and indexed.
- **ERPNext hooks:** `doc_events` on Sales Invoice and Payment Entry run on every billing transaction, so keep them cheap and return early for non-healthcare documents.
- **Portal APIs** (`api/patient_portal.py`) use `frappe.qb` multi-joins. Select only the columns you need.
- **Indexes:** frequently filtered DocType fields set `"search_index": 1` in the JSON, as in Patient Appointment. Add the flag to new filter fields.
- **Reports:** `report/` (diagnosis trends, appointment analytics, etc.) aggregate over historical data.
- Background work uses `frappe.enqueue` sparingly (2 uses). Use it for heavy, non-interactive work. Caching (`frappe.cache`) is currently unused.
