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
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/page/patient_history/patient_history.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/healthcare_practitioner/healthcare_practitioner.py
---

Likely hot or expensive paths, inferred from the code's shape:

- **Patient Appointment** (`patient_appointment.py`, about 2,000 lines) handles slot availability, overlap and capacity checks, fee validity, invoicing and recurring appointments. It runs on every booking from both the desk and the portal. Avoid N+1 `frappe.get_doc` calls inside slot loops. Prefer `frappe.db.get_value`, `get_cached_value` and `frappe.qb` joins.
- **Scheduler jobs** in `hooks.py`: `send_appointment_reminder` runs on **`all`** (every scheduler tick), so it must stay cheap and well filtered. The daily jobs update appointment status, fee validity, inpatient occupied-unit billables and expired medication requests.
- **Patient portal APIs** (`api/patient_portal.py`) use single `frappe.qb` queries with joins, for example `get_appointments`. Keep them that way, and use `get_cached_value` for lookups.
- **Patient history feed** (`page/patient_history/patient_history.py`) is paginated (`start`, `page_length=20`) over a large table of patient medical records.
- **Bulk or slow work goes through `frappe.enqueue`**, for example observation creation from Sample Collection and the recurring appointment handler. Follow this pattern for anything that loops over many records.
- **Link-field search queries** (`standard_queries`, `controllers/queries.py`, the practitioner query with `page_length`) must stay paginated.
- Raw `frappe.db.sql` appears in 31 files. New queries should use `frappe.qb` with indexed filters.
