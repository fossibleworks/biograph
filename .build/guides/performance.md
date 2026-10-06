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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
---

Paths that are likely to be performance-sensitive:

- **Patient Appointment** (`patient_appointment.py`, about 2.2k lines). Slot availability, overlap and capacity checks, recurring and block appointments, and calendar events all run on every booking. The `all` scheduler also runs `send_appointment_reminder`, so keep that job cheap.
- **Wildcard `doc_events["*"]`.** Every submit, cancel and update-after-submit of *any* DocType calls the patient-history medical-record hooks. Any added cost multiplies across the whole system.
- **Billing hooks** on Sales Invoice and Payment Entry (`healthcare/healthcare/utils.py`, about 1.9k lines) run during ERPNext accounting flows.
- **Daily schedulers:** appointment status updates, fee validity, inpatient occupied-unit billables, expiring medication requests. These are batch jobs over large tables.
- **Portal API** (`api/patient_portal.py`). Multi-join `frappe.qb` queries for each logged-in patient.
- **Reports** such as Patient Appointment Analytics and Diagnosis Trends.

Existing practice: use a single `frappe.qb` join query instead of per-row `get_doc` calls, and move bulk work to `frappe.enqueue` (recurring appointments, sample collection).
