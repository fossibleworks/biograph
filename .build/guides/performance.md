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

These are the likely hot paths:

- **The global `doc_events["*"]` hooks.** `on_submit`, `on_cancel` and `on_update_after_submit` call Patient History Settings for *every* submitted document in the site, so keep them cheap and return early.
- **Appointment scheduling.** `patient_appointment.py` is about 1,800+ lines. It runs availability, overlap and capacity checks, and `send_appointment_reminder` runs on the `all` scheduler (every few minutes). Daily jobs update appointment, fee-validity and medication-request status, and add inpatient billables.
- **Patient portal API.** `api/patient_portal.py` uses multi-join `frappe.qb` queries over appointments and encounters. Select only the columns you need.
- **Bulk operations go to the background queue.** Recurring appointment creation and sample collection already use `frappe.enqueue`. Follow that pattern for anything that loops over many records.
- **Reports** (`healthcare/healthcare/report/*`), such as appointment analytics and diagnosis trends, can scan large tables.

Prefer `frappe.get_all` with `pluck`/`fields` and `frappe.db.get_value` over loading full documents with `frappe.get_doc` inside loops.
