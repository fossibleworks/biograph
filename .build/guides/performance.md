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
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot paths, based on the code's shape:

- **`doc_events["*"]` hooks** in `hooks.py` (`create_medical_record`, `delete_medical_record`, `update_medical_record`) run on submit, cancel and update-after-submit of **every** doctype on the site. Keep them cheap, and return early when the doctype is not configured in Patient History Settings.
- **Sales Invoice / Payment Entry hooks** (`healthcare.healthcare.utils.manage_invoice_*`, `custom_doctype.payment_entry.*`) run inside every ERPNext billing transaction.
- **Patient Appointment** (`patient_appointment.py`, about 2,200 lines with about 26 `get_all`/`get_value` calls): slot availability, overlap/capacity checks, practitioner unavailability and recurring appointments. Recurring creation is already moved to `frappe.enqueue(queue="long", enqueue_after_commit=True)`, and other bulk work should follow that pattern.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` event (every few minutes). The daily jobs scan appointments, fee validity, inpatient records and medication requests. Use filtered queries and indexes, not full-table loops.
- **Patient Portal API** (`api/patient_portal.py`): public-facing whitelisted endpoints that serve slot lists and orders.
- **Reports** (`report/` such as patient_appointment_analytics and diagnosis_trends) aggregate over large clinical tables. Prefer `frappe.qb`/SQL aggregates over per-row `get_doc`. There are about 171 `frappe.db.sql`/`frappe.qb` uses in the codebase.
