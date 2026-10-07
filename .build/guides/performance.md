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
---

Likely hot or expensive paths:

- **Wildcard `doc_events["*"]`** (`on_submit`/`on_cancel`/`on_update_after_submit` → `patient_history_settings`) runs on **every submitted document in the site**, ERPNext ones included. Keep it cheap and return early for doctypes it doesn't track.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) add work to every ERPNext billing transaction.
- **Patient Appointment** (~1,900-line controller): slot availability, overlap/capacity checks, recurring appointments (already pushed to `frappe.enqueue`), and the `send_appointment_reminder` scheduler job that runs on **`all`** (every tick).
- **Daily schedulers** scan appointments, fee validities, inpatient records, and medication requests.
- **Reports** (`patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, …) and dashboard chart sources aggregate over large clinical tables.
- Raw `frappe.db.sql` and `frappe.cache` appear about 90 times. Prefer `frappe.qb`/`get_all` with filters and indexed fields, and avoid N+1 `get_doc` calls inside loops.
- Long work belongs in `frappe.enqueue`, and progress goes out through `frappe.publish_realtime` (see `sample_collection`).
