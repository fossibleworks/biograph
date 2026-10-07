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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.json
  - healthcare/healthcare/api/patient_portal.py
---

Paths that are likely to be performance-sensitive:

- **Global `doc_events` on `"*"`:** `on_submit`, `on_cancel` and `on_update_after_submit` call the `patient_history_settings` medical-record functions for **every submitted doctype on the site**, ERPNext ones included. Keep these handlers cheap and return early when the doctype is not configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_submit_cancel`, `manage_invoice_validate`, `set_paid_amount_in_healthcare_docs`) run inside ERPNext accounting transactions.
- **Scheduler:** `send_appointment_reminder` runs on the `all` tick, about every few minutes. Daily jobs update appointment, fee validity, inpatient billables and medication request statuses, and they iterate over large tables.
- **Appointment slot and availability calculation** (`patient_appointment.py`, about 1,900 lines, practitioner availability and schedules) runs on every booking in both Desk and the portal.
- **Patient Portal API** (`api/patient_portal.py`) uses multi-join `frappe.qb` queries across appointments, encounters, practitioners and companies.
- **Reports** in `healthcare/healthcare/report/*` (diagnosis trends, appointment analytics, lab test report and others) scan over date ranges.

Conventions that already exist: `frappe.enqueue` for heavy work (recurring appointment creation, sample collection), `search_index: 1` on frequently filtered doctype fields, and `frappe.qb` joins instead of query-per-row loops.
