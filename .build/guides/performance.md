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
  - healthcare/healthcare/utils.py
---

Paths likely to be performance-sensitive, inferred from the shape of the code:

- **Wildcard document hooks:** `doc_events["*"]` runs `create_medical_record`, `delete_medical_record` and `update_medical_record` (from `patient_history_settings`) on **every** submit, cancel and update-after-submit of **every** doctype. Keep these early-exit and cheap. They should do no extra queries for doctypes that are not configured.
- **Scheduler:** `send_appointment_reminder` runs on the `all` tick (every few minutes). Daily jobs update appointment status and fee validity, add inpatient occupancy to billables, and expire medication requests. These scan potentially large tables, so filter in SQL and process in batches.
- **Patient Appointment** (`patient_appointment.py`, about 2.2k lines) handles availability and slot computation, overlap and capacity checks, recurring appointments, and calendar events. It is a hot interactive path in desk and the portal. Recurring appointment creation and sample collection are already pushed to background jobs with `frappe.enqueue`. Follow that pattern for bulk work.
- **Billing hooks** on Sales Invoice and Payment Entry (`validate`/`on_submit`/`on_cancel`) run inside ERPNext's accounting transactions, so avoid per-row queries (N+1).
- **`healthcare/healthcare/utils.py`** (about 1.9k lines) gets billable items for a patient across many doctypes. Prefer `frappe.get_all(..., fields=[...])` with filters over loading full docs in a loop.
- **Reports** (`report/*`, e.g. patient appointment analytics, diagnosis trends) and **dashboard charts and number cards** aggregate over large datasets. Use SQL aggregation (Query Builder or parameterised `frappe.db.sql`).
- **Portal API** (`api/patient_portal.py`) is public-facing. Keep the payloads small.
- Avoid explicit `frappe.db.commit()` in request paths; it currently appears in 9 places.
