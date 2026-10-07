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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/fee_validity/fee_validity.py
---

Paths where performance is likely to matter:

- **Patient Appointment** (`patient_appointment.py`, about 2.2k lines): slot availability, overlap and capacity checks, block bookings, and `send_appointment_reminder`, which runs on the **`all`** scheduler tick (every few minutes).
- **Wildcard doc_events (`*`)** on submit, cancel, and update_after_submit create and update Patient Medical Records for *every* submitted doctype. Keep that handler cheap.
- **Daily schedulers** iterate appointments, fee validities, inpatient records, and medication requests.
- **Patient portal API** (`api/patient_portal.py`) runs multi-join `frappe.qb` queries per request.
- **`healthcare/healthcare/utils.py`** (about 1.9k lines) handles billables and invoicing lookups.

Existing conventions: use `frappe.get_cached_value` and `frappe.get_single` for settings and master lookups, and `frappe.qb` joins instead of per-row `get_doc` loops.
