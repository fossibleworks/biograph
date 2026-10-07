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

These paths are likely hot, judging from the shape of the code:

- **Patient Appointment.** `patient_appointment.py` is a very large controller (over 1,800 lines). It does slot and availability computation, overlap and capacity checks against `Practitioner Availability` and existing appointments, and recurring appointments (`recuring_appointment_handler.py`). Booking UIs call these paths repeatedly.
- **The `doc_events["*"]` hooks** (`create_medical_record` / `delete_medical_record` / `update_medical_record`) fire on *every* submit, cancel and update-after-submit across all doctypes. Keep them cheap and return early for doctypes that are not configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) run on each billing transaction in ERPNext.
- **Scheduler jobs**: `send_appointment_reminder` runs on `all`, so it is very frequent. Daily status sweeps cover appointments, fee validity, inpatient billables and expired medication requests. These iterate over potentially large tables.
- **Patient Portal API** (`api/patient_portal.py`) uses multi-join `frappe.qb` queries per patient.
- **Reports** (`patient_appointment_analytics`, `diagnosis_trends`, and others) aggregate across large clinical tables.

**Conventions already in use**
- Use `frappe.qb` joins and `frappe.get_all(..., fields=[...], pluck=...)` instead of per-row `get_doc` in loops.
- Use `frappe.enqueue` for heavy work (sample collection, recurring appointments).
- There are about 91 raw `frappe.db.sql` calls. Prefer the query builder for new code.
