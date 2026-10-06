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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

Likely hot paths, inferred from the code's shape:

- **`doc_events["*"]` hooks in `hooks.py`:** `create_medical_record`, `delete_medical_record` and `update_medical_record` run on submit, cancel and update-after-submit of **every doctype**. Keep them cheap and return early when a doctype isn't configured in Patient History Settings.
- **ERPNext Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) add work to core billing transactions.
- **Patient Appointment** (`patient_appointment.py`, the largest controller) handles slot availability, overlap checks and capacity checks. Its `send_appointment_reminder` runs on the `all` scheduler (every few minutes).
- **Daily schedulers** (appointment status updates, fee validity, inpatient billables, expired medication requests) scan large tables. Use filtered `frappe.qb` or `frappe.get_all` queries with the needed fields, not per-row `get_doc`.
- **Portal API** (`api/patient_portal.py`) joins appointments, encounters, practitioners and patients. Avoid calling the same helper twice in one request (for example, `get_patients_with_relations()` is evaluated twice in `get_appointments`).
- **Heavy work goes to background jobs** through `frappe.enqueue` (recurring appointments, sample collection).
- Doctype JSON uses `search_index` on frequently filtered link fields (for example, Clinical Procedure `patient` and `procedure_template`).
- **Reports** under `healthcare/healthcare/report` (appointment analytics, diagnosis trends, lab test report) aggregate large datasets.
