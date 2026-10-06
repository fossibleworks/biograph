---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or sensitive paths:

- **Appointment scheduling.** `patient_appointment.py` is about 2,200 lines. It covers slot availability, overlap and capacity checks, practitioner availability, unavailability blocks and recurring appointments. Availability lookups run on every booking in Desk and the portal. Keep queries bounded by practitioner, date and service unit.
- **`doc_events["*"]` on_submit/on_cancel** runs `create_medical_record` / `delete_medical_record` for **every submittable doctype in the site, ERPNext's included**. Any added cost there multiplies across the whole system, so keep it to cheap early-exit checks.
- **Scheduler `"all"`** runs `send_appointment_reminder` on every scheduler tick. It must stay incremental and indexed.
- **Patient Portal API** (`api/patient_portal.py`) serves practitioner, slot, appointment and payment data to anonymous or patient users. Avoid N+1 lookups per slot.
- **Reports** (patient appointment analytics, diagnosis trends, lab test report, medication item-wise sales) and **dashboard charts and number cards** aggregate large tables.
- **Patient history / patient progress pages** and the **patient duplicate check** scan patient records.
- **Bulk work goes to background jobs:** follow the existing `frappe.enqueue(..., queue="long", enqueue_after_commit=True)` pattern (recurring appointments, sample collection) instead of looping synchronously.
- About 90 raw `frappe.db.sql` calls exist. Prefer `frappe.qb` / `frappe.get_all` with explicit `fields` and filters, and parameterise values.
