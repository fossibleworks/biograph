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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

These paths are likely to be performance-sensitive, judging from the code's shape:
- **Wildcard doc_events:** `"*"` → `on_submit` / `on_cancel` / `on_update_after_submit` in `hooks.py` run `patient_history_settings` medical-record logic on **every submit of every doctype**. Keep that code cheap and return early.
- **Sales Invoice / Payment Entry hooks** (`healthcare/healthcare/utils.py`, `custom_doctype/payment_entry.py`) run during ERPNext billing.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every tick). The daily jobs update appointment status, fee validity, inpatient billables and expired medication requests, all over potentially large tables. Use set-based queries, not per-row `get_doc`.
- **Patient Appointment** (`patient_appointment.py`, about 1800+ lines) does slot, overlap and capacity checks on every booking. The portal's `api/patient_portal.py` builds multi-join `frappe.qb` queries.
- **Heavy work goes to the background** with `frappe.enqueue` (recurring appointments, sample collection).
- **Reports** in `healthcare/healthcare/report/` (analytics, trends) aggregate across patients and appointments.
