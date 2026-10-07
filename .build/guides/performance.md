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
  - healthcare/healthcare/setup/patient_duplicate_check.py
---

Likely hot or sensitive paths, judging from the code's shape:

- **Appointment scheduling.** `patient_appointment.py` is about 1,900 lines.
  - `validate_overlaps` and `validate_practitioner_unavailability` query appointments and Practitioner Availability on every save.
  - Slot availability is computed for booking, both in Desk and in the portal (`BookAppointmentModel.vue`).
  - Recurring appointment handling lives in `recuring_appointment_handler.py`.
- **Scheduler jobs.** `send_appointment_reminder` runs on the `all` tick. Daily jobs: `update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables`, `update_expired_medication_requests`. All of these scan potentially large tables, so keep them set-based and indexed.
- **Billing hooks.** `hooks.py` doc_events on Sales Invoice and Payment Entry run on every ERPNext invoice and payment, not only healthcare ones.
- **Reports.** `report/` (diagnosis_trends, patient_appointment_analytics, lab_test_report, …) and dashboard chart sources aggregate over history.
- **Raw SQL.** About 42 non-test `frappe.db.sql` calls. Prefer parameterised queries or `frappe.qb`, and avoid N+1 `get_doc` loops.
- **Patient duplicate check.** It runs on patient creation over the full patient table.
