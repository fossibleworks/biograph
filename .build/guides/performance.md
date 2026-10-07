---
title: Performance-sensitive paths
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
---

Based on the code's shape, these paths need care:

- **The wildcard `doc_events['*']` hook** (`patient_history_settings.create_medical_record` / delete / update) runs on submit, cancel and update-after-submit of **every** submittable doctype. Keep it cheap and return early for doctypes that aren't configured.
- **Sales Invoice and Payment Entry hooks** (`healthcare.healthcare.utils.manage_invoice_*`, `custom_doctype/payment_entry.py`) sit on ERPNext's billing hot path.
- **Appointment scheduling:** `patient_appointment.py` (about 2,200 lines) computes slots, overlaps, capacity, holidays and practitioner availability. The portal hits the same code through `get_slots`/`make_appointment`.
- **Scheduler jobs:** `send_appointment_reminder` runs on **every scheduler tick (`all`)**. The daily jobs scan appointments, fee validity, inpatient records and medication requests. Use filtered, indexed queries and batching.
- **Portal data endpoints:** `get_orders`, `build_order_map`, `get_data_from_service_requests` and `get_data_from_invoices` aggregate across patients and child observations. Avoid N+1 `frappe.get_doc` calls in loops.
- **Reports and pages:** `patient_history`, `patient_progress`, `patient_appointment_analytics` and `diagnosis_trends` work over large clinical tables.
- Data access: prefer `frappe.qb` or `frappe.get_all` with `fields`/`pluck` over full doc loads. About 91 raw `frappe.db.sql` calls exist; keep new ones parameterized. `frappe.enqueue` is rarely used today (2 calls); use it for long-running work.
