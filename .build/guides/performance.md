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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

These paths are likely to be hot or performance-sensitive:

- **Appointment scheduling**: `patient_appointment.py` (about 1800+ lines). It includes `get_availability_data` (slot computation per practitioner and service unit), `get_events` (calendar feed) and the overlap and capacity checks run on every validate. Avoid per-slot queries. Batch through `frappe.qb` or `frappe.get_all` with filters.
- **The global `doc_events["*"]` hooks** (`on_submit`/`on_cancel` → patient medical record) run for every submittable doctype in the site, so keep them cheap and return early.
- **`scheduler_events["all"]` → `send_appointment_reminder`** runs every scheduler tick (a few minutes) and must use indexed filters.
- **Bulk work** already goes through `frappe.enqueue` (recurring appointments, sample collection). Follow that pattern for anything that loops over many documents.
- **Reports** (`healthcare/healthcare/report/*`, for example patient_appointment_analytics and diagnosis_trends) aggregate over large clinical tables. Use SQL or query-builder aggregation, not Python loops.
- **Patient portal** endpoints (`api/patient_portal.py`) are public-facing. Paginate and limit fields.
