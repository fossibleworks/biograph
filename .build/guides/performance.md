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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - patient_portal/src/components/AppointmentModel.vue
---

Paths that are likely to be performance-sensitive:

- **Appointment scheduling** in `patient_appointment.py` (about 1,900 lines). It handles slot availability, overlap and capacity checks, practitioner availability and unavailability, and recurring appointments. These run on every booking and on every portal calendar view, with several raw `frappe.db.sql` queries. Keep queries indexed and filtered by practitioner and date, and avoid N+1 `get_doc` calls inside slot loops.
- **Scheduler jobs** (`hooks.py`):
  - `send_appointment_reminder` runs on **every scheduler tick** (`all`)
  - daily jobs: appointment status update, fee validity update, inpatient service-unit billables, medication request expiry
  - these run over whole tables, so batch them and use `frappe.db.set_value(..., update_modified=False)`
- **Long work goes to the background** with `frappe.enqueue`, as in recurring appointments (`recuring_appointment_handler.py`) and sample collection.
- **Patient history / encounter loading** (`patient_encounter.py`) and the observation and diagnostic report widgets can pull large child tables.
- **Reports and dashboard chart sources** (`healthcare/healthcare/report`, `dashboard_chart_source`) aggregate over appointments, admissions and claims.
- **Patient Portal:** the bundle is built once and paginates its lists client-side (`paginatedAppointments`, `paginatedDepartments`).
