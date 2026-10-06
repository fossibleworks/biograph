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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
---

These paths are likely performance-sensitive based on the code's shape:
- **The `doc_events["*"]` hooks** (`on_submit`/`on_cancel`/`on_update_after_submit` → `patient_history_settings.create/delete/update_medical_record`) run on **every submitted document in the whole site**, including ERPNext ones. Keep them cheap and exit early for doctypes that aren't configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) sit on ERPNext's hot accounting paths.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` tick (every few minutes). The daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. All of them scan potentially large tables, so filter in SQL and process in batches.
- **Appointment scheduling and availability** (`patient_appointment.py`: overlap and capacity checks, practitioner availability, block-based booking) is called interactively and from the portal.
- **Patient Portal API** (`api/patient_portal.py`) runs multi-join `frappe.qb` queries per patient and their relations.
- **Reports** (`report/` such as `patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`) aggregate over large datasets.

Conventions: prefer `frappe.qb` or single queries over per-row `frappe.get_doc` loops, and use `frappe.get_cached_doc` for settings singletons. `frappe.enqueue` is used sparingly (2 call sites); use it for heavy, non-interactive work.
