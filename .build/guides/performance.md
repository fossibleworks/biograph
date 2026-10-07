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

Likely hot paths:
- **Wildcard doc_events:** `doc_events["*"]` on_submit/on_cancel runs `create_medical_record` / `delete_medical_record` for *every* submitted doctype in the site. Keep these handlers cheap and exit early.
- **Scheduler `all` event:** `send_appointment_reminder` runs on every scheduler tick. It must query narrowly.
- **Patient Appointment:** `patient_appointment.py` is a very large controller (1,900+ lines). It handles availability, overlap and capacity checks, calendar events and recurring appointments. Slot and availability queries run on every booking from the desk and the portal.
- **Long work goes to the background queue:**
  - `frappe.enqueue` is used in `recuring_appointment_handler.py` and `sample_collection.py`.
  - `frappe.publish_realtime` pushes results back to the client.
  - Follow this pattern for bulk operations.
- **Reports** under `healthcare/healthcare/report/` (appointment analytics, diagnosis trends, lab test report, …) aggregate large tables. Prefer `frappe.db.get_all` with explicit fields and filters, or the query builder, over loading full docs in loops.
- **Patient portal endpoints** paginate in the UI (department and practitioner pages). Keep `api/patient_portal.py` queries field-limited.
