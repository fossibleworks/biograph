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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

# Performance-sensitive paths

These hot paths are inferred from the shape of the code:

- **Wildcard `doc_events["*"]`** (`patient_history_settings.create/update/delete_medical_record`) runs on submit and cancel of **every** document on the site. Keep these handlers cheap and return early for doctypes that aren't configured.
- **Scheduler `all` event:** `send_appointment_reminder` runs every few minutes. Daily jobs update appointment status, fee validity, inpatient billables, and medication-request expiry over potentially large tables, so filter in SQL and process in batches.
- **Appointment slot and availability computation** (`patient_appointment.py`, about 1900 lines, plus practitioner schedules and recurring/block booking) is called interactively from Desk and the portal booking flow.
- **Patient Portal APIs** (`api/patient_portal.py`) are multi-join `frappe.qb` queries over appointments, encounters, and practitioners for each logged-in patient.
- **Reports** (`report/*`: appointment analytics, diagnosis trends, lab test report, medication sales) aggregate over large date ranges.
- **Patches** in `patches/v16_0` that backfill fields across all appointments.

Conventions: prefer `frappe.qb` / `frappe.get_all` with explicit `fields` and filters over per-row `frappe.get_doc` in loops. Use `frappe.enqueue` for heavy work (rarely used today), and use `db_set` for single-field updates.
