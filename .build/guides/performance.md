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
---

Likely hot or sensitive paths:

- **Patient Appointment** (`patient_appointment.py`, about 2,000 lines): slot availability, overlap and capacity checks, fee validity and billing, and recurring appointments. This code runs on every booking from both desk and portal. Avoid per-slot queries inside loops.
- **Scheduler jobs:** `send_appointment_reminder` runs on **`all`** (every few minutes), so keep it cheap and indexed. The daily jobs (appointment status update, fee validity status, inpatient occupied-unit billables, expired medication requests) scan large tables.
- **Long-running work goes to the background** with `frappe.enqueue` (the recurring-appointment handler and sample collection already do this).
- **Queries:** about 91 raw `frappe.db.sql` and about 80 `frappe.qb` usages. Prefer `frappe.qb` or `frappe.get_all` with explicit fields and filters, and avoid N+1 `frappe.get_doc` calls in loops.
- **Reports** (`report/`: patient_appointment_analytics, diagnosis_trends, lab_test_report, medication_item_wise_sales, …) aggregate over large clinical datasets.
- **Portal bundle:** built with Vite (target es2015, sourcemaps on). Keep dependencies lean.
