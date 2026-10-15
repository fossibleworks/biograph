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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Likely hot or heavy paths:

- **Wildcard doc events:** `doc_events["*"]` runs `create_medical_record` / `delete_medical_record` / `update_medical_record` on **every** submittable doctype's submit, cancel or update. Keep these handlers cheap and exit early.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every few minutes). Daily jobs update appointment status, fee validity, inpatient occupancy billables and expired medication requests. They scan whole tables, so they should use bulk queries.
- **Appointment scheduling:** `patient_appointment.py` (~2.2k lines) handles overlap and capacity validation and `get_availability_data`, and the portal calls `get_slots` on every date or practitioner change. These run on each save and booking and are query-heavy.
- **Billing hooks:** Sales Invoice and Payment Entry `validate`/`on_submit` hooks in `healthcare/healthcare/utils.py` (~1.9k lines) and `custom_doctype/payment_entry.py`.
- **Reports and dashboards:** script reports (diagnosis trends, appointment analytics, lab test report, medication sales) plus number cards and dashboard chart sources aggregate across large clinical tables.
- Existing patterns: raw `frappe.db.sql` and `frappe.qb` (~185 uses), `frappe.enqueue` for long jobs (sample collection, recurring appointments), and `frappe.publish_realtime` for live updates. Caching is barely used.
