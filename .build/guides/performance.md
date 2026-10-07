---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
---

These paths are likely to be performance-sensitive:

- **Patient Portal API** (`healthcare/healthcare/api/patient_portal.py`). This is the densest query module. It runs `frappe.qb` joins across Patient Appointment, Patient Encounter, observations and the patient's relations on every portal page load. Keep queries set-based, select only the fields needed, and avoid per-row `get_doc` calls.
- **Appointment scheduling and validation** (`patient_appointment.py`). It checks overlaps, capacity and practitioner availability on every booking. The `send_appointment_reminder` scheduler job runs on the `all` (every-tick) schedule, so keep it cheap and incremental.
- **Daily scheduler jobs:** appointment status updates, fee validity, inpatient billables for occupied service units and expired medication requests. These walk potentially large tables, so batch them and filter by indexed fields.
- **Inpatient records:** billing and service-unit occupancy across long stays.
- **Reports** in `healthcare/healthcare/report/` (diagnosis trends, appointment analytics, medication sales) run aggregate queries over large date ranges.
- **`doc_events` on `'*'` and on Sales Invoice/Payment Entry** in `hooks.py` run on hot ERPNext transaction paths. Keep those handlers lightweight.
- Use `frappe.enqueue` for long-running work instead of blocking request handlers.
