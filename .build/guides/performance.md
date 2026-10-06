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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot paths, judged from the shape of the code:

- **Appointment scheduling** (`patient_appointment.py`, about 1,900 lines): slot availability, overlap and capacity checks, block-based booking, unavailability and calendar events. These run on every booking and on the portal's slot views. Keep queries indexed and filtered by practitioner/date, and avoid per-slot DB round trips.
- **Scheduler jobs:** `send_appointment_reminder` runs on **every `all` tick**. The daily jobs (`update_appointment_status`, `update_validity_status`, inpatient billables, expired medication requests) scan whole tables, so keep them set-based.
- **The `"*"` doc_events:** `create/delete/update_medical_record` run on **every** submit, cancel and update-after-submit across all DocTypes, so they must return early cheaply for unrelated doctypes.
- **Sales Invoice / Payment Entry hooks** add work to ERPNext billing transactions.
- **Portal API** (`api/patient_portal.py`): uses joined `frappe.qb` queries. Some helpers such as `get_patients_with_relations()` are called more than once per request, so cache the result locally.
- **Long work goes to the background** with `frappe.enqueue`, as in recurring appointment creation and sample collection.
- About 90 raw `frappe.db.sql` calls exist. Prefer `frappe.qb` or `get_all` with explicit fields and limits.
