---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

These are the paths that are likely to be performance-sensitive, judged from the shape of the code:

- **Wildcard document hooks:** `doc_events["*"]` runs `create/delete/update_medical_record` from Patient History Settings on **every** submit or cancel of **every** doctype, across the whole ERPNext site. Keep these handlers cheap and return early when the doctype is not configured.
- **Sales Invoice and Payment Entry hooks** run on every invoice or payment, including non-healthcare ones. Guard them early.
- **Scheduler jobs:**
  - `send_appointment_reminder` runs on `all`, which means every scheduler tick.
  - Daily jobs scan appointments, fee validity, inpatient records and medication requests.
  - Use filtered and indexed queries, batch the work, and avoid per-row `get_doc`.
- **Appointment booking and availability:** the practitioner schedule, availability and slot calculations in `patient_appointment.py` are large (about 1.4k+ lines) and called interactively from the calendar and the portal.
- **Patient Portal API:** joins across Patient Appointment, Encounter, Practitioner, Patient and Company built with `frappe.qb`. Keep them as single joined queries, not N+1 loops.
- **Reports** under `healthcare/healthcare/report/` (diagnosis trends, appointment analytics, lab test report and others) aggregate over large tables.

**Existing conventions**
- Heavy work is offloaded with `frappe.enqueue`, as in recurring appointment creation and sample collection.
- Prefer `frappe.qb` or `frappe.db.get_all` with explicit `fields`/`filters`/`pluck` over loading full documents.
- About 31 modules still use raw `frappe.db.sql`. Use parameterised queries if you touch them.
