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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
---

# Performance-sensitive areas

These are inferred from the shape of the code. No benchmarks exist.

- **Patient Appointment** (`patient_appointment.py`, ~2,200 lines) handles slot availability (`get_availability_data`), overlap and capacity checks, recurring and block-based booking, and fee validity. Its queries run on every booking and on portal `get_slots`. Avoid per-slot DB queries inside loops.
- **The wildcard `doc_events["*"]` hooks** (Patient Medical Record create/update/delete) run on submit/cancel of **every** submittable doctype, including ERPNext's. Keep them cheap and return early.
- **Sales Invoice hooks** (`manage_invoice_validate`, submit/cancel in `healthcare/healthcare/utils.py`, ~1,900 lines) are on ERPNext's billing hot path.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` scheduler (every few minutes). Daily jobs scan appointments, fee validity, inpatient records, and medication requests. All of these scan whole tables, so filter in SQL.
- **Long work is enqueued** with `frappe.enqueue` (recurring appointments, sample collection). Follow that pattern for bulk operations.
- **Portal API** (`api/patient_portal.py`) list endpoints are paginated on the client. Keep server queries bounded.
- Upstream adds `search_index` to commonly filtered Link fields such as `patient` and `procedure_template`. Do the same on new heavily filtered fields.
