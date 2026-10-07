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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

Likely hot or sensitive paths:

- **Patient Appointment** (`patient_appointment.py`, over 1,800 lines): slot availability, overlap checks, and recurring appointments. Recurring creation is already offloaded with `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`.
- **Scheduler jobs:** `send_appointment_reminder` runs on `all` (every few minutes). Daily jobs update appointment status, fee validity, inpatient occupancy billables, and expired medication requests. These scan large tables, so keep queries indexed and batched.
- **`doc_events['*']`** for patient medical records fires on submit, cancel, and update-after-submit for **every** doctype. Any cost added there multiplies across the system.
- **Sales Invoice hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`) sit on the billing path.
- **Patient portal API** (`api/patient_portal.py`) is public-facing.
- **Reports** (patient_appointment_analytics, diagnosis_trends, lab_test_report, …) run over large datasets. Prefer `frappe.qb` aggregations to Python loops.

Use `frappe.enqueue` for long-running work. Avoid N+1 `frappe.get_doc` calls inside loops.
