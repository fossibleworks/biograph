---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/vite.config.js
---

Likely hot or expensive paths, based on the shape of the code:

- **Appointment scheduling.** `patient_appointment.py` is very large (1800+ lines). It handles availability slots, overlap and capacity checks, practitioner availability, recurring appointments (`recuring_appointment_handler.py`) and the calendar views. Slot and overlap queries run on every booking and portal request. Keep them indexed and set-based, not per-row loops.
- **Scheduler jobs** in `hooks.py`: `send_appointment_reminder` runs on **every** scheduler tick (`all`). Daily jobs scan appointments, fee validity, inpatient records and medication requests. Keep them incremental, filter by date or status, and use `frappe.enqueue` for heavy work. Only about 2 call sites use enqueue today.
- **Reports** (`report/patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, `medication_item_wise_sales`, …) and the `patient_history` / `patient_progress` desk pages aggregate across large clinical tables.
- **Raw SQL:** about 91 `frappe.db.sql` calls versus about 80 `frappe.qb` uses. Prefer `frappe.qb` / `get_all` with explicit `fields` and filters, and avoid N+1 `get_doc` inside loops.
- **Patches** that backfill data, such as `v16_0/populate_appointment_end_fields`, iterate whole tables. Batch them and handle per-row failures (they currently log and continue).
- **Patient Portal** bundle: built with Vite targeting es2015 with sourcemaps. Keep frappe-ui imports tree-shakeable.
