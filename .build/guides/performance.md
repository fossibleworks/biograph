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
  - healthcare/healthcare/api/patient_portal.py
---

Paths that are likely to be performance-sensitive, based on the codebase:

- **`doc_events["*"]` on_submit/on_cancel/on_update_after_submit** (`patient_history_settings.create_medical_record`) runs on **every submittable document in the site**, including ERPNext ones. Keep it cheap and exit early for irrelevant doctypes.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) sit in the ERPNext billing hot path.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` scheduler (every few minutes). The daily jobs `update_appointment_status`, `update_validity_status`, inpatient occupancy billing and `update_expired_medication_requests` scan large tables. Use bulk queries and filters, not per-row `get_doc` loops.
- **Appointment availability and slot calculation** (`patient_appointment.py`, practitioner schedules, block-based therapy booking, recurring appointments). Heavy work there is already moved to `frappe.enqueue` (`recuring_appointment_handler.py`, `sample_collection.py`).
- **Reports** (`healthcare/healthcare/report`) and dashboard charts and number cards aggregate clinical data. There are about 91 raw `frappe.db.sql` or cache call sites. Prefer `frappe.qb` or `get_all` with indexed filters.
- **Patient Portal API** (`api/patient_portal.py`) is called by external patients. Keep it paginated and limited to the logged-in patient.

Recommendations that follow the existing code: use `frappe.enqueue` for long-running or bulk work, `frappe.db.get_value` or `pluck` instead of loading full docs, and batch inserts in patches.
