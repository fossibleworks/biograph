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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Likely hot or heavy paths, inferred from the code's shape:

- **Appointment scheduling.**
  - `patient_appointment.py` is very large (over 1800 lines) and runs availability, overlap and capacity checks.
  - Slot generation runs in `api/patient_portal.py:get_slots`, the practitioner schedule logic and practitioner availability.
  - These run on every booking and portal slot fetch. Avoid per-slot DB queries.
- **Scheduler jobs** in `hooks.py`.
  - `send_appointment_reminder` runs on **every** scheduler tick (`all`). Keep it cheap and filtered.
  - The daily jobs are `update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables` and `update_expired_medication_requests`. They scan large tables, so use batched queries.
- **Raw queries.** There are about 171 `frappe.db.sql` / `frappe.qb` call sites. Prefer `frappe.qb` or `get_all` with `pluck` and the fields you need over looping `get_doc`.
- **Background work.** `frappe.enqueue` is already used for heavy jobs (recurring appointment creation, sample collection). Follow that pattern for bulk operations.
- **Reports and dashboards** (`report/`, `dashboard_chart_source/`) aggregate across appointments, invoices and encounters.
- **Patient portal bundle.** Vite targets es2015 with sourcemaps. The portal paginates appointment and diagnostic lists on the client.
