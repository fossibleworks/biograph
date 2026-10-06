---
title: Performance-sensitive areas
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

Paths likely to be hot, based on the code's shape:

- **Wildcard doc_events**: `hooks.py` runs `create_medical_record`, `delete_medical_record` and `update_medical_record` on submit, cancel and update-after-submit of **every** doctype (`"*"`). Keep these handlers cheap and return early for doctypes that are not tracked.
- **Appointment scheduling**: `patient_appointment.py` (~2.2k lines) handles availability, slots, overlap and capacity checks, and recurring appointments (`recuring_appointment_handler.py` uses `frappe.enqueue`). `send_appointment_reminder` runs on the **`all`** scheduler tick.
- **Billing hooks** on Sales Invoice and Payment Entry validate, submit and cancel (`healthcare/healthcare/utils.py`, `custom_doctype/`). They run inside ERPNext transactions.
- **Daily schedulers** scan whole tables: fee validity status, appointment status, inpatient occupied-unit billables and expired medication requests.
- **Patient portal API** (`api/patient_portal.py`) builds multi-join `frappe.qb` queries over appointments, encounters and practitioners.

Conventions: use `frappe.qb` or `get_list(pluck=...)` over N+1 `get_doc` loops, and move long work into a background job with `frappe.enqueue` (as `sample_collection.py` and the recurring appointment handler do). Add `search_index` to frequently filtered link fields in doctype JSON; 35 doctype JSON files already do.
