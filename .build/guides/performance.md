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
  - healthcare/healthcare/report/patient_appointment_analytics/patient_appointment_analytics.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or sensitive paths:

- **Global `doc_events` on `"*"`:** `on_submit`/`on_cancel`/`on_update_after_submit` call `patient_history_settings.create/delete/update_medical_record` for **every submitted document in the whole site**, including ERPNext ones. Keep these handlers cheap and return early when the doctype is not configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) run on every ERPNext billing transaction.
- **Scheduler:** `send_appointment_reminder` runs on the `all` schedule, every few minutes. Daily jobs scan appointments, fee validity, inpatient records and medication requests. Query with filters and indexes, and avoid loading full documents in loops.
- **Patient Appointment** (≈1900-line controller) handles slot availability, overlap/capacity checks and block-based booking. These run on every booking and from the portal.
- **Reports** (`patient_appointment_analytics`, `diagnosis_trends`, lab and medication reports) aggregate over large tables. Prefer `frappe.qb`/SQL aggregation to Python loops.
- **Patient history / encounter loading** (`patient_encounter.py`, `page/patient_history`) grows with each patient's record count. Paginate.
- **Portal API** (`api/patient_portal.py`) uses `frappe.db.get_all` with explicit `fields`. Keep that style rather than fetching whole documents.
