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
  - patient_portal/src/socket.js
---

Likely hot paths:
- **Wildcard `doc_events["*"]`:** `on_submit`/`on_cancel`/`on_update_after_submit` call `patient_history_settings.create/delete/update_medical_record` for *every* submitted document on the site. Keep these handlers cheap and exit early for irrelevant doctypes.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) run inside ERPNext billing transactions.
- **Scheduler:** `send_appointment_reminder` runs on `all`, which is every few minutes. The daily status updates for appointments, fee validity, inpatient billables and expired medication requests scan large tables, so they need indexed filters and batched updates.
- **Appointment booking:** slot and availability calculation, overlap and capacity checks, practitioner schedules, and recurring appointments. Recurring creation is already sent to the `long` queue with `frappe.enqueue`.
- **Patient Portal API** (`api/patient_portal.py`) and the portal's cached resources (`socket.js` uses `getCachedListResource`).
- **Reports** in `healthcare/healthcare/report` (appointment analytics, diagnosis trends, lab test report).

The codebase has about 40 raw `frappe.db.sql` calls outside tests and about 80 `frappe.qb` usages. Prefer `frappe.qb` or `get_all` with explicit `fields`, and avoid querying per row inside loops.
