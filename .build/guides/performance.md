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
  - healthcare/healthcare/api/patient_portal.py
---

These paths are likely performance-sensitive:

- **Appointment scheduling:** `patient_appointment.py` (~2,200 lines) contains `get_availability_data` and slot computation over practitioner schedules, service-unit capacity (`MaximumCapacityError`), overlaps and unavailability. It is called interactively from the desk and the portal booking dialog.
- **Wildcard `doc_events`:** `"*"` on_submit/on_cancel/on_update_after_submit creates or updates Patient Medical Records for **every** submitted document across ERPNext. Keep `patient_history_settings` hooks cheap and return early for irrelevant doctypes.
- **Billing hooks:** Sales Invoice validate/submit/cancel and Payment Entry submit/cancel run healthcare logic in `utils.py` (~1,900 lines) and `custom_doctype/`. Avoid per-row queries inside invoice item loops.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every tick). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. Batch queries, and use `frappe.enqueue` for heavy work (it is already used in two places).
- **Portal API:** `api/patient_portal.py` uses joined `frappe.qb` queries across appointments, encounters and practitioners.
- **Reports:** `report/` script reports (patient_appointment_analytics, diagnosis_trends, …) aggregate potentially large tables. Prefer SQL aggregation via `frappe.qb`.

There is no caching layer in use (`frappe.cache` is unused) and there are no perf tests.
