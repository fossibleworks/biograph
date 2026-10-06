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
  - healthcare/healthcare/page/patient_history/patient_history.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/report/patient_appointment_analytics/patient_appointment_analytics.py
---

Likely hot or sensitive paths:

- **Patient Appointment** (`patient_appointment.py`, about 1,800+ lines) handles slot and availability calculation, overlap and capacity checks, recurring appointments, fee validity and invoicing. Booking screens and the portal call it often. Do overlap and slot checks in the database (`frappe.qb` with selective filters), not by loading full documents in loops.
- **Wildcard `doc_events["*"]`** run on *every* submit and cancel in the site (`patient_history_settings.create_medical_record` / `delete_medical_record`). Keep them cheap, and return early for doctypes that aren't configured.
- **Scheduler jobs:**
  - `send_appointment_reminder` runs on the `all` tick, i.e. every few minutes
  - the daily jobs update appointment status, fee validity, inpatient billables and expired medication requests
  - these jobs scan large tables, so filter by date and status, and work in batches
- **Patient History feed** (`page/patient_history/patient_history.py:get_feed`) is paginated (`start`, `page_length=20`). Keep it paginated.
- **Patient portal API** (`api/patient_portal.py`) builds multi-join `frappe.qb` queries per request. Avoid calling `get_patients_with_relations()` more than once per request; `get_appointments` currently calls it twice.
- **Reports and dashboards** (`report/patient_appointment_analytics`, `diagnosis_trends`, the dashboard chart sources) aggregate over appointments and encounters. Use grouped SQL and avoid per-row Python lookups.
- **Portal bundle:** the Vite build targets es2015 with sourcemaps. Keep the dependency footprint small (frappe-ui, vue, vue-router).
