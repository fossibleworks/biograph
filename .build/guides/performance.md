---
title: Performance-sensitive areas
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/hooks.py
  - healthcare/controllers/queries.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

These paths are likely to be hot or heavy, based on the shape of the codebase.

- **Appointment scheduling** (`patient_appointment.py`, about 2.2k lines): availability and slot computation (`get_availability_data`), overlap and capacity checks against Practitioner Availability and Healthcare Service Units, and recurring appointments. The recurring-appointment handler offloads work with `frappe.enqueue`. These run on every booking and save from both the desk and the portal.
- **`doc_events` wildcard hook** in `hooks.py`: `"*"` `on_submit`/`on_cancel` calls `patient_history_settings.create_medical_record` / `delete_medical_record` for **every submittable doctype in the site**. Keep it cheap, and exit early for doctypes that are not configured.
- **Scheduler `"all"` events** (appointment reminders) run every few minutes, so queries there must be indexed and bounded.
- **Patient History / Patient Progress pages** (`healthcare/healthcare/page/`) aggregate medical records per patient and can involve large datasets.
- **Reports** (`report/`: patient_appointment_analytics, diagnosis_trends, lab_test_report, inpatient_medication_orders, ...) scan transactional tables.
- **Link search queries** (`controllers/queries.py`, `get_healthcare_service_units`) run on every keystroke in link fields.
- **Portal API** (`api/patient_portal.py`) is patient-facing and should avoid N+1 `frappe.get_doc` loops.
- **Sample Collection** uses `frappe.enqueue` for bulk work.

Conventions: put long or bulk work on `frappe.enqueue`. Prefer `frappe.get_all(..., fields=[...])` or `frappe.qb` with filters over loading full docs in loops.
