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
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or expensive paths:

- **Wildcard `doc_events["*"]`.** `patient_history_settings.create_medical_record` / `delete_medical_record` / `update_medical_record` run on **every** submit, cancel and update-after-submit across all doctypes. Keep these handlers cheap, and exit early when the doctype isn't configured.
- **Patient Appointment.** `patient_appointment.py` is about 2200 lines. It covers slot availability, overlap/capacity checks, practitioner schedules and recurring appointments. Its `validate()` runs several DB-backed checks on every save. Scheduling queries over schedules and slots are the main hot path. Recurring appointment creation already uses `frappe.enqueue` (`recuring_appointment_handler.py`).
- **Scheduler jobs.**
  - `send_appointment_reminder` runs on the `all` schedule, every few minutes.
  - Daily jobs scan appointments, fee validity, inpatient occupancy billing and medication requests.
  - Process these in batches, and wrap each record in try/except + `log_error` so one failure doesn't abort the run.
- **Billing hooks.** Sales Invoice `validate` / `on_submit` / `on_cancel` and Payment Entry handlers run inside ERPNext's transactions.
- **Portal APIs.** `api/patient_portal.py` joins appointments, encounters, practitioners and patients. Use `frappe.qb` joins with selective columns, not per-row `get_doc`. Note: `get_appointments` calls `get_patients_with_relations()` twice.
- **Reports** (`report/diagnosis_trends`, `patient_appointment_analytics`, `medication_item_wise_sales`) aggregate over large tables. Push filtering and grouping into SQL/qb.
- **Heavy work:** use `frappe.enqueue` (as `sample_collection.py` does) instead of doing it synchronously in a request.
