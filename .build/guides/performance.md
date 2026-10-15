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

# Performance-sensitive paths

- **Global `doc_events["*"]`:** `on_submit`, `on_cancel`, and `on_update_after_submit` run `patient_history_settings.create/delete/update_medical_record` for **every submitted document on the site**. Keep these handlers cheap and exit early for doctypes that are not tracked.
- **Scheduler:** `send_appointment_reminder` runs on the `all` event, every few minutes. Daily jobs update appointment status, fee validity, inpatient occupancy billables, and expired medication requests. All of them scan large tables, so use filtered `frappe.get_all` or `frappe.qb` queries and avoid loading full documents in loops.
- **Appointment slot computation** (`patient_portal.get_slots`, availability and overlap checks in `patient_appointment.py`) is the hottest interactive path for the portal and front desk.
- **Sales Invoice submit/cancel hooks** (`healthcare.healthcare.utils.manage_invoice_submit_cancel`) add work to billing.
- Data access mixes `frappe.db.sql` (about 105 calls) and `frappe.qb` (about 80). Prefer `frappe.qb` or `get_all` with explicit `fields`, and avoid N+1 `get_doc` calls.
