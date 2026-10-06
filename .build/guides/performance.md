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

Likely hot or heavy paths:

- **Patient Appointment.** `patient_appointment.py` is very large (around 1900 lines). Its availability and slot computation (`get_availability_data`), overlap and capacity checks, and the `send_appointment_reminder` job that runs every scheduler tick (`all`) all run frequently.
- **Global `doc_events` on `*`.** `on_submit`, `on_cancel` and `on_update_after_submit` run the patient-history medical record hooks for every submittable document, so keep them cheap.
- **Sales Invoice and Payment Entry hooks.** `manage_invoice_validate`/submit and the payment entry hooks run on ERPNext billing for every invoice.
- **Daily jobs** that update appointment, fee validity, inpatient billables and medication request statuses scan many records.
- **Reports** (`diagnosis_trends`, `patient_appointment_analytics`, `lab_test_report`, …) and 91 raw `frappe.db.sql` queries.

Conventions:
- Use `frappe.enqueue` for bulk or slow work. It is already used for recurring appointments and sample collection.
- Prefer `frappe.get_all`/`get_list` with `pluck` and restricted `fields` over loading full docs in loops.
- Caching is not used anywhere yet (no `frappe.cache` or `redis_cache`).
