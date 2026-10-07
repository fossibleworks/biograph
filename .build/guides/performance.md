---
title: Performance-sensitive paths
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - patient_portal/vite.config.js
---

These paths are likely hot or heavy:

- **Appointment availability and booking.** `get_availability_data` and related whitelisted methods in `patient_appointment.py` (about 2,200 lines, 20+ whitelisted endpoints) compute slots across practitioner schedules, service units, unavailability, block and recurring bookings, and overlap and capacity checks. They are called interactively from Desk and from the portal booking flow.
- **`doc_events` on `"*"`.** Every submit, cancel and update-after-submit of any doctype calls `patient_history_settings` medical record functions. Keep these fast and exit early when the doctype isn't configured.
- **Sales Invoice and Payment Entry hooks.** `manage_invoice_validate/submit_cancel` and `set_paid_amount_in_healthcare_docs` run on every invoice and payment, including non-healthcare ones.
- **Scheduler jobs.** `send_appointment_reminder` runs on `all` (every tick). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. They should iterate with filtered `frappe.get_all` and `pluck`, not by loading full documents.
- **Reports and dashboard chart sources** over Patient Appointment, Inpatient Record and Insurance Claim.
- **Patient Portal bundle** (`target es2015`). Keep frappe-ui imports selective.

For queries, prefer `frappe.qb` or `get_all` with explicit `fields` and filters over per-row `get_doc` in loops.
