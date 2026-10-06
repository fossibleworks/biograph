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

Likely hot or heavy paths, based on the shape of the code:

- **Patient Appointment.** `patient_appointment.py` is very large and runs on every save. `validate` does overlap checks, practitioner schedule and unavailability lookups, capacity checks, queue position, calendar events and fee validity. Slot availability and recurring or block appointments also live here. Avoid extra per-row queries in `validate` and in slot computation.
- **Scheduler jobs** (`hooks.py`):
  - `send_appointment_reminder` runs on **every scheduler tick (`all`)**, so keep it cheap and indexed.
  - The daily jobs scan appointments, fee validity, inpatient records (billables) and medication requests.
- **Long-running work is queued with `frappe.enqueue`**, for example in `recuring_appointment_handler.py` and `sample_collection.py`. Follow this pattern for bulk creation.
- **Portal API** (`api/patient_portal.py`) builds multi-join `frappe.qb` queries per patient. For example, `get_appointments` calls `get_patients_with_relations()` twice. Prefer one query with selected columns over N+1 `get_doc` calls.
- **Reports** (`report/`, such as `patient_appointment_analytics` and `diagnosis_trends`) and dashboard chart sources aggregate over large tables.
- **Raw SQL:** about 91 `frappe.db.sql` call sites. Use parameterised queries and filter on indexed columns.
- **Caching:** there is effectively no app-level caching today (`frappe.cache` is almost unused).
- **Portal bundle:** built with `target: es2015`, sourcemaps and hashed assets.
