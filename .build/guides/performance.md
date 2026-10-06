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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or expensive paths, judged from the shape of the code:

- **Patient Appointment** (`patient_appointment.py`, about 1,900+ lines) runs on every booking. It handles overlap validation (`validate_overlaps`), practitioner unavailability checks, slot and capacity checks, queue position, calendar event creation and invoicing. Availability and slot lookups through practitioner schedules and `practitioner_availability` run per request from the desk and the portal booking flow.
- **Scheduler jobs:** `send_appointment_reminder` runs on **every scheduler tick (`all`)**. The daily jobs update appointment status, fee-validity status, inpatient occupied-unit billables and expired medication requests. These scan whole tables, so keep queries indexed and filtered.
- **Heavy or batch operations** are already offloaded with `frappe.enqueue` (recurring appointment creation, sample collection). Follow that pattern for bulk work.
- **Billing** (`healthcare/healthcare/utils.py` billables helpers, Sales Invoice hooks in `custom_doctype/`) aggregates across many clinical doctypes.
- **Reports** (`report/patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report` and others) cover large date ranges.
- **Raw SQL:** about 91 `frappe.db.sql` calls. Prefer `frappe.qb` or `get_all` with explicit `fields` and filters, and avoid per-row queries inside loops.
- **Portal:** `api/patient_portal.py` endpoints are called by unauthenticated-to-patient traffic. Keep payloads small by returning explicit fields from `frappe.db.get_all`.
