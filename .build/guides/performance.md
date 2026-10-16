---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or heavy paths, judging by how the code is laid out:

- **Patient Appointment** (`patient_appointment.py`, ~1800+ lines). It handles slot availability, overlap and capacity checks, practitioner availability and recurring appointments (`recuring_appointment_handler.py`, which uses `frappe.enqueue`). Its calendar view runs on every booking. Slot lookups should batch their queries and avoid per-slot DB calls.
- **Scheduler jobs** in `hooks.py`. `send_appointment_reminder` runs on the `all` (every-few-minutes) schedule. Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. These scan large tables, so filter in SQL and process in bulk.
- **ERPNext `doc_events`** on Sales Invoice and Payment Entry run on every billing transaction, so keep them cheap.
- **Reports** (`report/patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, ...) run aggregate queries over big tables.
- **Patient portal API** (`api/patient_portal.py`) is called by an unauthenticated-to-patient-scale audience. Use `frappe.db.get_all` with explicit `fields`.
- **Long-running work:** move it to `frappe.enqueue`, as `sample_collection.py` and the recurring appointments handler do.
- **Patches:** migrations over large tables, such as `populate_appointment_end_fields`, should work in batches.
