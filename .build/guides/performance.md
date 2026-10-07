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
  - patient_portal/vite.config.js
---

Likely hot or heavy paths, based on the codebase's shape:

- **Wildcard `doc_events` (`"*"`)**: `on_submit`, `on_cancel` and `on_update_after_submit` call `patient_history_settings.create/delete/update_medical_record` for **every submittable doctype in the whole site**. Keep those functions cheap and return early when the doctype isn't configured.
- **Sales Invoice / Payment Entry hooks** (`healthcare.healthcare.utils.manage_invoice_*`, `custom_doctype/payment_entry.py`) run on every ERPNext billing transaction, so avoid per-item queries inside loops.
- **Scheduler jobs:** `send_appointment_reminder` runs on `all`, which means every scheduler tick, so it must stay a cheap indexed query. The daily jobs (`update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables`, `update_expired_medication_requests`) scan whole tables. Batch them and use `frappe.qb` / bulk updates.
- **Appointment scheduling** (`patient_appointment.py`, 2,200+ lines; practitioner availability and schedule; slot computation for the portal and desk calendar) is called interactively and repeatedly while booking.
- **Long-running work** is pushed to background jobs with `frappe.enqueue` (recurring appointment creation in `recuring_appointment_handler.py`, `sample_collection.py`). Follow that pattern for bulk operations, and show the user a "being created in background" message.
- **Reports** (`healthcare/healthcare/report/*`: patient_appointment_analytics, diagnosis_trends, lab_test_report, and others) and dashboard chart sources aggregate over large clinical tables. Use SQL/qb aggregation, not Python loops over `get_all`.
- **Portal bundle:** Vite builds with `target: es2015` and sourcemaps. Keep frappe-ui imports tree-shakeable.

General rule: prefer `frappe.db.get_value(..., [fields])` and `pluck=` over loading full docs, and never query inside loops over child rows.
